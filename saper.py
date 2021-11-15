import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo

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
                temp.append(button)
            self.buttons.append(temp)

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
                            1 <= next_button.y <= MineSweeper.COLUMNS and next_button not in queue) :
                            queue.append(next_button)

    def click(self, clicked_button:MyButton):
        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_cells()
            self.print_buttons()

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

    def create_widgets(self):
        count = 1
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                button = self.buttons[i][j]
                button.number = count
                button.grid(row=i, column=j)
                count += 1

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