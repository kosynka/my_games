import pygame
import time
import sys

pygame.font.init()

white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (204, 204, 0)
blue = (50, 255, 255)
black = (0, 0, 0)

(width, height) = (900, 600)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Quadro table game")
screen.fill(white)
pygame.display.flip()

myfont = pygame.font.SysFont('Times New Roman', 20)

board = [['  ' for i in range(8)] for i in range(8)]

class Piece:
    def __init__(self, name, image, pos):
        self.name = name
        self.image = image
        self.pos = pos


# Figures
chwh = Piece('chwh', 'chwh.png', (700, 30))
chwn = Piece('chwn', 'chwn.png', (720, 30))
chbh = Piece('chbh', 'chbh.png', (740, 30))
chbn = Piece('chbn', 'chbn.png', (760, 30))

clwh = Piece('clwh', 'clwh.png', (700, 50))
clwn = Piece('clwn', 'clwn.png', (720, 50))
clbh = Piece('clbh', 'clbh.png', (740, 50))
clbn = Piece('clbn', 'clbn.png', (760, 50))

shwh = Piece('shwh', 'shwh.png', (700, 70))
shwn = Piece('shwn', 'shwn.png', (720, 70))
shbh = Piece('shbh', 'shbh.png', (740, 70))
shbn = Piece('shbn', 'shbn.png', (760, 70))

slwh = Piece('slwh', 'slwh.png', (700, 90))
slwn = Piece('slwn', 'slwn.png', (720, 90))
slbh = Piece('slbh', 'slbh.png', (740, 90))
slbn = Piece('slbn', 'slbn.png', (760, 90))

global gameObjectList
gameObjectList = [chwh, chwn, chbh, chbn, clwh, clwn, clbh, clbn, shwh, shwn, shbh, shbn, slwh, slwn, slbh, slbn]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    label = myfont.render("Привет. Чтобы начать играть перетасивайте фигуры мышкой по очереди", 1, black)
    screen.blit(label, (100, 10))

    for indx,_ in enumerate(gameObjectList):
        curObj = gameObjectList[indx]
        screen.blit(curObj.image, curObj.pos)

    pygame.display.update()