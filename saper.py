from random import shuffle
import tkinter as tk

class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
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
        count = 1
        for i in range(MineSweeper.ROWS):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                button = MyButton(MineSweeper.window, x=i, y=j, number=count)
                temp.append(button)
                count += 1
            self.buttons.append(temp)
    
    def create_widgets(self):
        for i in range(MineSweeper.ROWS):
            for j in range(MineSweeper.COLUMNS):
                button = self.buttons[i][j]
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
        for row_button in self.buttons:
            for button in row_button:
                if button.number in index_mines:
                    button.is_mine = True
    
    def start_game(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()

        MineSweeper.window.mainloop()



game = MineSweeper()
game.start_game()