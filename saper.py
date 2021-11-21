import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo, showerror

colors = {
    1: '#00ff00',
    2: '#00ffff',
    3: '#0000ff',
    4: '#ff00ff',
    5: '#c3ff00',
    6: '#ff9d00',
    7: '#ff0000',
    8: '#6e0a19',
}

class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master,  width=3, font='Calibri 16 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'MyButton{self.x}{self.y} {self.number} {self.is_mine}'



class MineSweeper:

    window = tk.Tk()
    window.title("Сапер")
    ROWS = COLUMNS = 10
    MINES = 10
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROWS+2):
            temp = []
            for j in range(MineSweeper.COLUMNS + 2):
                button = MyButton(MineSweeper.window, x=i, y=j)
                button.config(command=lambda btn=button: self.click(btn))
                button.bind('<Button-3>', self.right_click)
                temp.append(button)
            self.buttons.append(temp)

    def right_click(self, event):
        cur_button = event.widget
        if cur_button['state'] == 'normal':
            cur_button['state'] = 'disable'
            cur_button['text'] = '🚩'
            cur_button['disabledforeground'] = 'red'
        elif cur_button['text'] == '🚩':
            cur_button['text'] = ''
            cur_button['state'] = 'normal'

    def breadth_first_sort(self, button: MyButton):
        queue = [button]
        while queue:
            cur_button = queue.pop()
            color = colors.get(cur_button.count_bomb, 'black')
            if cur_button.count_bomb:
                cur_button.config(text=cur_button.count_bomb, disabledforeground=color)
            else:
                cur_button.config(text='', disabledforeground=color)
            cur_button.is_open = True
            cur_button.config(state='disabled')
            cur_button.config(relief=tk.SUNKEN)

            if cur_button.count_bomb == 0:
                x, y = cur_button.x, cur_button.y
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        next_button = self.buttons[x + dx][y + dy]
                        if not next_button.is_open and (1 <= next_button.x <= MineSweeper.ROWS and \
                            1 <= next_button.y <= MineSweeper.COLUMNS and next_button not in queue):
                            queue.append(next_button)

    def click(self, clicked_button:MyButton):
        if MineSweeper.IS_GAME_OVER:
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_cells()
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'Вы проиграли')
            for i in range(1, MineSweeper.ROWS + 1):
                for j in range(1, MineSweeper.COLUMNS + 1):
                    button = self.buttons[i][j]
                    if button.is_mine:
                        button['text'] = '*'
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_sort(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def reload(self):
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Настройки')

        tk.Label(win_settings, text='количество строк').grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.grid(row=0, column=1, padx=20, pady=10)
        row_entry.insert(0, MineSweeper.ROWS)

        tk.Label(win_settings, text='количество колонок').grid(row=1, column=0)
        column_entry = tk.Entry(win_settings)
        column_entry.grid(row=1, column=1, padx=20, pady=10)
        column_entry.insert(0, MineSweeper.COLUMNS)

        tk.Label(win_settings, text='количество мин').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1, padx=20, pady=10)
        mines_entry.insert(0, MineSweeper.MINES)

        save_button = tk.Button(win_settings, text='Сохранить', \
            command=lambda: self.change_settings(row_entry, column_entry,mines_entry))
        save_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
        try:
            int(row.get()), int(column.get()), int(mines.get())
        except ValueError:
            showerror('Ошибка ввода', 'Вы ввели неправильные значения')

        MineSweeper.ROWS = int(row.get())
        MineSweeper.COLUMNS = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()

    def create_widgets(self):

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки', command=self.create_settings_win)
        settings_menu.add_command(label='Выход', command=self.window.destroy)
        menubar.add_cascade(label='Меню', menu=settings_menu)

        count = 1
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                button = self.buttons[i][j]
                button.number = count
                button.grid(row=i, column=j, stick='NWES')
                count += 1

        for i in range(1, MineSweeper.ROWS + 1):
            tk.Misc.grid_rowconfigure(self.window, i, weight=1)
            
        for i in range(1, MineSweeper.ROWS + 1):
            tk.Misc.grid_columnconfigure(self.window, i, weight=1)

    def open_all_buttons(self):
        for i in range(MineSweeper.ROWS + 2):
            for j in range(MineSweeper.COLUMNS + 2):
                button = self.buttons[i][j]
                if button.is_mine:
                    button.config(text='*', background='red', disabledforeground='black')
                elif button.count_bomb in colors:
                    color = colors.get(button.count_bomb, 'black')
                    button.config(text=button.count_bomb, fg=color)

    def print_buttons(self):
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                button = self.buttons[i][j]
                if button.is_mine:
                    print('B', end=' ')
                else:
                    print(button.count_bomb, end=' ')
            print()
    
    @staticmethod
    def get_mines_places(excluded_number: int):
        indexees = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROWS + 1))
        print(f'исключаем кнопку номер {excluded_number}')
        indexees.remove(excluded_number)
        shuffle(indexees)
        return indexees[:MineSweeper.MINES]

    def insert_mines(self, number: int):
        index_mines = self.get_mines_places(number)
        print(index_mines)
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                button = self.buttons[i][j]
                if button.number in index_mines:
                    button.is_mine = True

    def count_mines_in_cells(self):
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                button = self.buttons[i][j]
                count_bomb = 0
                if not button.is_mine:
                    for row_dx in (-1, 0, 1):
                        for col_dx in (-1, 0, 1):
                            neighbour = self.buttons[i + row_dx][j + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                button.count_bomb = count_bomb
    
    def start_game(self):
        self.create_widgets()
        # self.open_all_buttons()

        MineSweeper.window.mainloop()



game = MineSweeper()
game.start_game()