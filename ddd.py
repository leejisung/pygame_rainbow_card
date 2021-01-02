import pygame as pg
import random

clock = pg.time.Clock()
board = pg.display.set_mode((800,800))

back = pg.image.load("gray_back.png")

red_ = pg.image.load("red.png")
orange_ = pg.image.load("orange.png")
yellow_ = pg.image.load("yellow.png")
green_ = pg.image.load("green.png")
blue_ = pg.image.load("blue.png")
indigo_ = pg.image.load("indigo.png")
pupple_ = pg.image.load("pupple.png")

gray_ = pg.image.load("gray.png")

insert_ = pg.image.load("insert.png")
reverse_ = pg.image.load("reverse.png")
change_ = pg.image.load("change.png")



class icon():
    def __init__(self, c):
        self.img = c
    def loc(self, a,b):
        self.xy = (a,b)
        self.col_xy = self.img.get_rect(topleft= (a,b))
    def bh(self, a):
        self.g= a

red = icon(red_)
orange = icon(orange_)
yellow = icon(yellow_)
green = icon(green_)
blue = icon(blue_)
indigo = icon(indigo_)
pupple = icon(pupple_)

g0 = icon(gray_)
g1 = icon(gray_)
g2 = icon(gray_)
g3 = icon(gray_)
g4 = icon(gray_)
g5 = icon(gray_)
g6 = icon(gray_)
g7 = icon(gray_)

change = icon(change_)
reverse = icon(reverse_)
insert = icon(insert_)

colors = [red, orange ,yellow, green, blue, indigo,pupple]
grays = [g0,g1,g2,g3,g4, g5, g6, g7]

for i in range(8):
    grays[i].bh(i)

def shuffle():
    random.shuffle(colors)


def board_update():
    board.blit(back, (0,0))
    Y = 200
    for xx in range(8):
        X = xx*80+70
        grays[xx].loc(X,Y)
        board.blit(grays[xx].img, grays[xx].xy)
    for xx in range(7):
        X = xx*80+100
        colors[xx].loc(X,Y)
        board.blit(colors[xx].img, colors[xx].xy)
    change.loc(100,400)
    reverse.loc(300,400)
    insert.loc(500,400)
    board.blit(change.img, change.xy)
    board.blit(reverse.img, reverse.xy)
    board.blit(insert.img, insert.xy)   
    
    pg.display.update()

def card_change(a, b):
    a_switch = colors.index(a)
    b_switch = colors.index(b)
    colors[a_switch] = b
    colors[b_switch] = a
def card_reverse(a, b):
    global colors
    aa = colors.index(a)
    bb = colors.index(b)
    card_change(a, b)
    print(aa,bb)
    if abs(aa-bb)>2:
        card_reverse(colors[min(aa,bb)+1],colors[max(aa,bb)-1])
def card_insert(c, g):
    global colors
    cs = colors.index(c)
    ss = colors[cs]
    colors[cs] = 0
    ncs = colors[:g]+[c]+colors[g:]
    ncs.remove(0)
    print(ncs)
    colors = ncs
    
    
shuffle()
board_update()

event_click = 0
select_card = 0
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            if event_click ==0:
               if change.col_xy.collidepoint(mouse):
                   event_click = 1
               if reverse.col_xy.collidepoint(mouse):
                   event_click = 2
               if insert.col_xy.collidepoint(mouse):
                   event_click = 3
        if event_click==1:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                for xx in colors:
                    if xx.col_xy.collidepoint(mouse):
                        if select_card==0:
                            select_card = xx
                        else:
                            card_change(select_card, xx)
                            board_update()
                            event_click = 0
                            select_card = 0
        if event_click==2:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                for xx in colors:
                    if xx.col_xy.collidepoint(mouse):
                        if select_card==0:
                            select_card = xx
                        else:
                            card_reverse(select_card, xx)
                            board_update()
                            event_click = 0
                            select_card = 0
        if event_click==3:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                if select_card==0:
                    for xx in colors:
                        if xx.col_xy.collidepoint(mouse):
                            select_card=xx
                else:
                    for xx in grays:
                        if xx.col_xy.collidepoint(mouse):
                            card_insert(select_card, xx.g)
                            board_update()
                            event_click = 0
                            select_card = 0
                    

