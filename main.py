import pygame
import time
import sys

pygame.font.init()

white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (204, 204, 0)
blue = (50, 255, 255)
black = (0, 0, 0)

(WIDTH, HEIGHT) = (900, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Quadro table game")
screen.fill(white)
pygame.display.flip()

myfont = pygame.font.SysFont('Times New Roman', 20)

class Piece:
    def __init__(self, name, image, pos):
        self.name = name
        self.image = image
        self.pos = pos

# Figures
chwh = Piece('chwh', 'img/chwh.png', (750, 30))
chwn = Piece('chwn', 'img/chwn.png', (780, 30))
chbh = Piece('chbh', 'img/chbh.png', (810, 30))
chbn = Piece('chbn', 'img/chbn.png', (840, 30))

clwh = Piece('clwh', 'img/clwh.png', (750, 90))
clwn = Piece('clwn', 'img/clwn.png', (780, 90))
clbh = Piece('clbh', 'img/clbh.png', (810, 90))
clbn = Piece('clbn', 'img/clbn.png', (840, 90))

shwh = Piece('shwh', 'img/shwh.png', (750, 150))
shwn = Piece('shwn', 'img/shwn.png', (780, 150))
shbh = Piece('shbh', 'img/shbh.png', (810, 150))
shbn = Piece('shbn', 'img/shbn.png', (840, 150))

slwh = Piece('slwh', 'img/slwh.png', (750, 210))
slwn = Piece('slwn', 'img/slwn.png', (780, 210))
slbh = Piece('slbh', 'img/slbh.png', (810, 210))
slbn = Piece('slbn', 'img/slbn.png', (840, 210))

global gameObjectList
gameObjectList = [chwh, chwn, chbh, chbn, clwh, clwn, clbh, clbn, shwh, shwn, shbh, shbn, slwh, slwn, slbh, slbn]

'''
# ячейки
class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.occupied = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

# нарисовать таблицу
def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j)%2 ==1:
                grid[i][j].colour = grey
    return grid

# сделать ход
def Do_Move(OriginalPos, FinalPosition, screen):
    starting_order[FinalPosition] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None
'''

running = True
while running:
    ### grid = make_grid(4, screen) ###

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # если произошло событие - нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_pos = event.pos
            curObj.followMouse = True
            curObj.followMouseOffset = [mouse_pos[0] - curObj.pos[0], mouse_pos[1] - curObj.pos[1]]
    
    # надпись наверху окна
    label = myfont.render("Привет. Чтобы начать играть перетасивайте фигуры мышкой по очереди", 1, black)
    screen.blit(label, (100, 10))

    # добавление фигур на окно
    for indx,_ in enumerate(gameObjectList):
        curObj = gameObjectList[indx]
        curObjImage = pygame.image.load(curObj.image)
        curObjPos = curObj.pos
        screen.blit(curObjImage, curObjPos)


    pygame.display.update()