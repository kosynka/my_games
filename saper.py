
import tkinter as tk

class MyButton(tk.Button):

    def __repr__(self):
        return 'mb'



class MineSweeper:

    window = tk.Tk()
    ROWS = COLUMNS = 8

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROWS):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                button = MyButton(MineSweeper.window, width=4, font='Calibri 15 bold')
                temp.append(button)
            self.buttons.append(temp)
    
    def create_widgets(self):
        for i in range(MineSweeper.ROWS):
            for j in range(MineSweeper.COLUMNS):
                button = self.buttons[i][j]
                button.grid(row=i, column=j)

    def print_buttons(self):
        for row_button in self.buttons:
            print(row_button)

    def start_game(self):
        self.create_widgets()
        self.print_buttons()
        MineSweeper.window.mainloop()



game = MineSweeper()
game.start_game()