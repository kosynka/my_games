from random import shuffle
import tkinter as tk

class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master,  width=4, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton{self.x}{self.y} {self.number} {self.is_mine}'



class MineSweeper:

    window = tk.Tk()
    ROWS = COLUMNS = 5
    MINES = 5

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROWS+2):
            temp = []
            for j in range(MineSweeper.COLUMNS+2):
                button = MyButton(MineSweeper.window, x=i, y=j)
                button.config(command=lambda btn=button: self.click(btn))
                temp.append(button)
            self.buttons.append(temp)

    def click(self, clicked_button:MyButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
        else:
            clicked_button.config(text=clicked_button.number, disabledforeground='black')
        clicked_button.config(state='disabled')

    def create_widgets(self):
        for i in range(MineSweeper.ROWS+2):
            for j in range(MineSweeper.COLUMNS+2):
                button = self.buttons[i][j]
                button.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(MineSweeper.ROWS+2):
            for j in range(MineSweeper.COLUMNS+2):
                button = self.buttons[i][j]
                if button.is_mine:
                    button.config(text='*', background='red', disabledforeground='black')
                else:
                    button.config(text=button.number, disabledforeground='black')
                button.grid(row=i, column=j)

    def print_buttons(self):
        for row_button in self.buttons:
            print(row_button)
    
    @staticmethod
    def get_mines_places():
        indexees = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROWS + 1))
        shuffle(indexees)
        return indexees[:MineSweeper.MINES]

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, MineSweeper.ROWS+1):
            for j in range(1, MineSweeper.COLUMNS+1):
                button = self.buttons[i][j]
                button.number = count
                if button.number in index_mines:
                    button.is_mine = True
                count += 1
    
    def start_game(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        self.open_all_buttons()

        MineSweeper.window.mainloop()



game = MineSweeper()
game.start_game()