import pygame as pg
import random

board = pg.display.set_mode((500,500))
blue = pg.image.load("blue_back.png")
white_circle = pg.image.load("white_circle.png")
red_circle = pg.image.load("red_circle.png")


all_loc = []
board.blit(blue, (0,0))
for i in range(100,500,100):
    pg.draw.line(board,(255,255,255),(i,100),(i,400),5)
    for j in range(100,500,100):
        pg.draw.line(board,(255,255,255),(100, j),(400, j),5)
        if (i!= 400 and j!=400):
            all_loc.append((i, j))
five_loc  = random.sample(all_loc, 5)
cc = []
cs =[]
for i in range(5):
    circle = random.choice([red_circle, white_circle])
    c=(circle.get_rect(topleft=five_loc[i]))
    cs.append(circle)
    cc.append(c)
    board.blit(circle, c)
pg.display.update()

def board_update(cc, cs):
    board.blit(blue, (0,0))
    for i in range(100,500,100):
        pg.draw.line(board,(255,255,255),(i,100),(i,400),5)
        for j in range(100,500,100):
            pg.draw.line(board,(255,255,255),(100, j),(400, j),5)
            if (i!= 400 and j!=400):
                all_loc.append((i, j))
    for i in range(len(cc)):
        circle = random.choice([red_circle, white_circle])
        board.blit(cs[i], cc[i])
    pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            for point in range(len(cc)):
                if cc[point].collidepoint(mouse):
                    del cc[point]
                    del cs[point]
                    board_update(cc, cs)
                    break
        
