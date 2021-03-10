# Setup Functions ------------------------------------- #
import json
import os
import random
import sys

import pygame
from pygame.locals import *

# Setup pygame and window ------------------------------------- #
pygame.init()
click = False


# loadimg and loadtransimg are better ways to load an image, use def loadtransimg if the image has transparent parts!!

def loadimg(imgname) -> object:
    return pygame.image.load(imgname).convert()


def loadtransimg(imgname):
    return pygame.image.load(imgname).convert_alpha()


screenx = 1920
screeny = 1080
Clock = pygame.time.Clock()
pygame.display.set_caption('Prototype 2')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((screenx, screeny), pygame.NOFRAME)
fullscreen = False
menublock = loadtransimg('images/menu block.png')
menublock2 = loadtransimg('images/menu block2.png')

# Fonts ------------------------------------- #

PixelFontB = pygame.font.Font('Fonts/Bold Pixel Font.otf', 70)
PixelFont = pygame.font.Font('Fonts/Pixel Font.otf', 50)
PixelFontTall = pygame.font.Font('Fonts/Tall Pixel Font.otf', 50)
Mainfont = pygame.font.Font('Fonts/Perfect DOS VGA 437.ttf', 30)


def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# Images

startbuttonimg = loadtransimg('images/Start button.png')
startbuttonimgbig = loadtransimg('images/Start button big.png')

settingsbuttonimg = loadtransimg('images/Settings button.png')
settingsbuttonimgbig = loadtransimg('images/settingsbuttonimgbig.png')

aboutbuttonimg = loadtransimg('images/About button.png')
aboutbuttonimglarge = loadtransimg('images/About button large.png')

quitbuttonimg = loadtransimg('images/Quit button.png')
quitbuttonimglarge = loadtransimg('images/Quitimglarge.png')

returnbuttonimg = loadtransimg('images/Returnbutton.png')
returnbuttonimglarge = loadtransimg('images/Returnbuttonlarge.png')

demobuttonimg = loadtransimg('images/Demo.png')
demobuttonimglarge = loadtransimg('images/Demolarge.png')

buttonr = startbuttonimg.get_rect()
buttonr.centerx = screen.get_rect().centerx

turncircle = loadtransimg('images/Turn Circle.png')

# Sounds
selectsound1 = pygame.mixer.Sound('sounds/select1.wav')
hoversound1 = pygame.mixer.Sound('sounds/hover1.wav')
menublockcenter = menublock.get_rect()
menublockcenter.centerx = screen.get_rect().centerx

# Cursor image

cursorimg = loadtransimg('images/cursor.png')

# Backrounds

Dungeon1 = loadimg('images/Dungeon1.png')

# Still Frames

ArcherFrame = loadtransimg('Still Frames test/archer skeleton.png')
SpearFrame = loadtransimg('Still Frames test/Spear skeleton.png')
MageFrame = loadtransimg('Still Frames test/Mage skeleton.png')
BossFrame = loadtransimg('Still Frames test/Boss skeleton.png')

# Unit Hud

UnitHud = loadtransimg('images/Empty unit gui.png')

# Animated Menu Backround


menubackround1 = loadimg('images/Lake Backround.png')
menubackround2 = loadimg('images/Mountain Backround.png')
backroundx = 0
foregroundtopx = 0
foregroundmidx = 0

randombackroundnum = random.randrange(0, 2)
if randombackroundnum == 0:
    menubackround = menubackround1
if randombackroundnum == 1:
    menubackround = menubackround2

pygame.mouse.set_cursor(0)

# Menu buttons become big
button1img = startbuttonimg
button1x = screenx / 2 - 66.5
button2img = settingsbuttonimg
button2x = screenx / 2 - 109
button3img = aboutbuttonimg
button3x = screenx / 2 - 66.5
button4img = quitbuttonimg
button4x = screenx / 2 - 52.5
button5img = returnbuttonimg
button5x = screenx / 2 - 81
button6img = demobuttonimg
button6x = screenx / 2 - 53.5

playselectsound1 = True
playselectsound2 = True
playselectsound3 = True
playselectsound4 = True


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image


# Load NPC's

default = []
skeleton_mage_idle = []
skeleton_mage_attack = []
skeleton_mage_hit = []
skeleton_mage_death = []


def load_image(dirr=None, name="None"):
    if dirr == None:
        image = pygame.image.load(name)
        return image
    else:
        image = pygame.image.load(dirr + "/" + name)
        return image


def loadedimg(dirr, var):
    character_quantity = [name for name in os.listdir(dirr)]
    for name in character_quantity:
        var.append(name)


class Unit:
    def __init__(self, attack, hitpoints, speed, stillframe):
        self.attack = attack
        self.hitpoints = hitpoints
        self.speed = speed
        self.stillframe = stillframe
        if stillframe == BossFrame:
            self.xpos = stillframe.get_width() / 2 - 60
        else:
            self.xpos = stillframe.get_width() / 2

            self.ypos = stillframe.get_height() / 2


SkeletonArcher = Unit(9224, 900, 103, ArcherFrame)
SkeletonSpear = Unit(11040, 834, 105, SpearFrame)
SkeletonMage = Unit(7020, 549, 106, MageFrame)
SkeletonBoss = Unit(11700, 725, 95, BossFrame)

test1 = Unit(9224, 900, 100, BossFrame)
test2 = Unit(9224, 900, 99, BossFrame)
test3 = Unit(9224, 900, 98, BossFrame)
test4 = Unit(9224, 900, 97, ArcherFrame)
test5 = Unit(9224, 900, 96, ArcherFrame)
test6 = Unit(9224, 900, 95, ArcherFrame)


def main_menu():
    running = True
    while running == True:
        global backroundx
        global foregroundmidx
        global foregroundtopx
        # Menu buttons become big
        global button1img
        global button1x
        global button2img
        global button2x
        global button3img
        global button3x
        global button4img
        global button4x
        global playselectsound1
        global playselectsound2
        global playselectsound3
        global playselectsound4
        global SkeletonBossIdleIndex
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))

        rel_x = backroundx % menubackround.get_rect().width

        screen.blit(menubackround, (rel_x - menubackround.get_rect().width, 0))

        if rel_x < screenx:
            screen.blit(menubackround, (rel_x, 0))
        backroundx -= .30

        draw_text('Main Menu', PixelFontB, (255, 255, 255), screen, screenx / 2, 50)
        mx, my = pygame.mouse.get_pos()

        screen.blit(menublock, (screenx / 2 - 200, 450))
        menubutton_1 = screen.blit(button1img, (button1x, 550))
        menubutton_2 = screen.blit(button2img, (button2x, 650))
        menubutton_3 = screen.blit(button3img, (button3x, 750))
        menubutton_4 = screen.blit(button4img, (button4x, 850))

        # GAME

        if not menubutton_1.collidepoint(mx, my):
            button1img = startbuttonimg
            button1x = screenx / 2 - 66.5
            playselectsound1 = True

        if menubutton_1.collidepoint((mx, my)):
            button1img = startbuttonimgbig
            button1x = screenx / 2 - 73
            if playselectsound1 == True:
                hoversound1.play()
                playselectsound1 = False
            if click:
                selectsound1.play()
                game()

        # SETTINGS

        if not menubutton_2.collidepoint(mx, my):
            button2img = settingsbuttonimg
            button2x = screenx / 2 - 109
            playselectsound2 = True

        if menubutton_2.collidepoint((mx, my)):
            button2img = settingsbuttonimgbig
            button2x = screenx / 2 - 119.5
            if playselectsound2 == True:
                hoversound1.play()
                playselectsound2 = False
            if click:
                selectsound1.play()
                settings()

        # ABOUT

        if not menubutton_3.collidepoint(mx, my):
            button3img = aboutbuttonimg
            button3x = screenx / 2 - 66.5
            playselectsound3 = True

        if menubutton_3.collidepoint((mx, my)):
            button3img = aboutbuttonimglarge
            button3x = screenx / 2 - 73
            if playselectsound3 == True:
                hoversound1.play()
                playselectsound3 = False
            if click:
                selectsound1.play()
                about()

        # QUIT

        if not menubutton_4.collidepoint(mx, my):
            button4img = quitbuttonimg
            button4x = screenx / 2 - 52.5
            playselectsound4 = True

        if menubutton_4.collidepoint((mx, my)):
            button4img = quitbuttonimglarge
            button4x = screenx / 2 - 57.5
            if playselectsound4 == True:
                hoversound1.play()
                playselectsound4 = False
            if click:
                pygame.quit()
                sys.exit()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    pass

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))
        pygame.display.update()

        Clock.tick(120)


def settings():
    running = True
    while running == True:
        global backroundx

        screen.fill((0, 0, 0))

        rel_x = backroundx % menubackround.get_rect().width
        screen.blit(menubackround, (rel_x - menubackround.get_rect().width, 0))
        if rel_x < screenx:
            screen.blit(menubackround, (rel_x, 0))
        backroundx -= .30

        draw_text('Settings', PixelFontB, (255, 255, 255), screen, screenx / 2, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        pygame.display.update()
        Clock.tick(120)


def game():
    global button6img
    global button6x
    global button5img
    global button5x
    global playselectsound1
    global playselectsound2
    running = True
    while running == True:
        global backroundx

        screen.fill((0, 0, 0))

        rel_x = backroundx % menubackround.get_rect().width
        screen.blit(menubackround, (rel_x - menubackround.get_rect().width, 0))
        if rel_x < screenx:
            screen.blit(menubackround, (rel_x, 0))
        backroundx -= .30

        screen.blit(menublock2, (screenx / 2 - 360, 120))

        #  Title
        mx, my = pygame.mouse.get_pos()

        draw_text('Game', PixelFontB, (255, 255, 255), screen, screenx / 2, 50)

        menubutton_6 = screen.blit(button6img, (button6x, 300))

        menubutton_5 = screen.blit(button5img, (button5x, 800))

        if not menubutton_6.collidepoint(mx, my):
            button6img = demobuttonimg
            button6x = screenx / 2 - 53.5
            playselectsound2 = True

        if menubutton_6.collidepoint((mx, my)):
            button6img = demobuttonimglarge
            button6x = screenx / 2 - 58.5
            if playselectsound2 == True:
                hoversound1.play()
                playselectsound2 = False
            if click:
                selectsound1.play()
                demo()

        if not menubutton_5.collidepoint(mx, my):
            button5img = returnbuttonimg
            button5x = screenx / 2 - 81
            playselectsound1 = True

        if menubutton_5.collidepoint((mx, my)):
            button5img = returnbuttonimglarge
            button5x = screenx / 2 - 89
            if playselectsound1 == True:
                hoversound1.play()
                playselectsound1 = False
            if click:
                selectsound1.play()
                running = False

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        pygame.display.update()
        Clock.tick(120)


def about():
    global button5img
    global button5x
    running = True
    while running == True:
        global backroundx

        screen.fill((0, 0, 0))

        rel_x = backroundx % menubackround.get_rect().width
        screen.blit(menubackround, (rel_x - menubackround.get_rect().width, 0))
        if rel_x < screenx:
            screen.blit(menubackround, (rel_x, 0))
        backroundx -= .30

        screen.blit(menublock2, (screenx / 2 - 360, 120))

        # screen.blit(menublock, (screenx / 2 - 200, 450))

        draw_text('About', PixelFontB, (255, 255, 255), screen, screenx / 2, 50)

        draw_text("Made by Ruben Smith", Mainfont, (255, 255, 255), screen, screenx / 2, 300)
        draw_text("A project for Saxion", Mainfont, (255, 255, 255), screen, screenx / 2, 400)
        draw_text("university of applied sciences,", Mainfont, (255, 255, 255), screen, screenx / 2, 450)
        draw_text("Creative Media and Game Technologies", Mainfont, (255, 255, 255), screen, screenx / 2, 500)
        draw_text("2021", Mainfont, (255, 255, 255), screen, screenx / 2, 600)

        mx, my = pygame.mouse.get_pos()

        menubutton_5 = screen.blit(button5img, (button5x, 800))

        if not menubutton_5.collidepoint(mx, my):
            button5img = returnbuttonimg
            button5x = screenx / 2 - 81
            playselectsound1 = True

        if menubutton_5.collidepoint((mx, my)):
            button5img = returnbuttonimglarge
            button5x = screenx / 2 - 89
            if playselectsound1 == True:
                hoversound1.play()
                playselectsound1 = False
            if click:
                selectsound1.play()
                running = False

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        pygame.display.update()
        Clock.tick(120)


rollfortwo = random.randrange(2)
rollforthree = random.randrange(3)

turninit = False
recieveinput = False


def demo():
    global unit1attackbar, unit2attackbar, unit3attackbar, unit4attackbar, unit5attackbar, unit6attackbar, turninit
    global turn
    running = True
    combatants = [test1, False, test3, test4, test5, test6]

    unit1attackbarbool = False
    unit2attackbarbool = False
    unit3attackbarbool = False
    unit4attackbarbool = False
    unit5attackbarbool = False
    unit6attackbarbool = False

    if combatants[0] != False:
        unit1attackbarbool = True
    if combatants[1] != False:
        unit2attackbarbool = True
    if combatants[2] != False:
        unit3attackbarbool = True
    if combatants[3] != False:
        unit4attackbarbool = True
    if combatants[4] != False:
        unit5attackbarbool = True
    if combatants[5] != False:
        unit6attackbarbool = True

    if combatants[0] == False:
        unit1attackbar = False
    if combatants[1] == False:
        unit2attackbar = False
    if combatants[2] == False:
        unit3attackbar = False
    if combatants[3] == False:
        unit4attackbar = False
    if combatants[4] == False:
        unit5attackbar = False
    if combatants[5] == False:
        unit6attackbar = False

    if unit1attackbarbool == True:
        unit1attackbar = 0
    if unit2attackbarbool == True:
        unit2attackbar = 0
    if unit3attackbarbool == True:
        unit3attackbar = 0
    if unit4attackbarbool == True:
        unit4attackbar = 0
    if unit5attackbarbool == True:
        unit5attackbar = 0
    if unit6attackbarbool == True:
        unit6attackbar = 0
    while running == True:

        screen.fill((0, 0, 0))

        screen.blit(Dungeon1, (screenx / 2 - 1620, 0))

        def speedpercentage(unitspeed):
            speedquotient = unitspeed / 1400
            percentspeed = speedquotient * 100
            return percentspeed

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT + 1:
                if not turninit:
                    if combatants[0]:
                        unit1attackbar += speedpercentage(combatants[0].speed)
                    if combatants[1]:
                        unit2attackbar += speedpercentage(combatants[1].speed)
                    if combatants[2]:
                        unit3attackbar += speedpercentage(combatants[2].speed)
                    if combatants[3]:
                        unit4attackbar += speedpercentage(combatants[3].speed)
                    if combatants[4]:
                        unit5attackbar += speedpercentage(combatants[4].speed)
                    if combatants[5]:
                        unit6attackbar += speedpercentage(combatants[5].speed)
            if unit1attackbar >= 100:
                print('unit 1 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit1attackbar = 0
                            print('unit 1 turn end')
                            recieveinput = True
                            turninit = False
            elif unit2attackbar >= 100:
                print('unit 2 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit2attackbar = 0
                            print('unit 2 turn end')
                            recieveinput = True
                            turninit = False
            elif unit3attackbar >= 100:
                print('unit 3 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit3attackbar = 0
                            print('unit 3 turn end')
                            recieveinput = True
                            turninit = False
            elif unit4attackbar >= 100:
                print('unit 4 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit4attackbar = 0
                            print('unit 4 turn end')
                            recieveinput = True
                            turninit = False
            elif unit5attackbar >= 100:
                print('unit 5 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit5attackbar = 0
                            print('unit 5 turn end')
                            recieveinput = True
                            turninit = False
            elif unit6attackbar >= 100:
                print('unit 6 turn')
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit6attackbar = 0
                            print('unit 6 turn end')
                            recieveinput = True
                            turninit = False

        def combatimages(list):

            if list[0] != False:
                leftactortop = list[0].stillframe
            if list[1] != False:
                leftactormiddle = list[1].stillframe
            if list[2] != False:
                leftactorbottom = list[2].stillframe
            if list[3] != False:
                rightactortoppreflip = list[3].stillframe
            if list[4] != False:
                rightactormiddlepreflip = list[4].stillframe
            if list[5] != False:
                rightactorbottompreflip = list[5].stillframe
            if list[0] == False:
                leftactortop = False
            if list[1] == False:
                leftactormiddle = False
            if list[2] == False:
                leftactorbottom = False
            if list[3] == False:
                rightactortoppreflip = False
            if list[4] == False:
                rightactormiddlepreflip = False
            if list[5] == False:
                rightactorbottompreflip = False

            leftactortopplacement = False
            leftactormiddleplacement = False
            leftactorbottomplacement = False
            rightactortopplacement = False
            rightactormiddleplacement = False
            rightactorbottomplacement = False
            rightactortopimg = rightactortoppreflip
            rightactormidimg = rightactormiddlepreflip
            rightactorbotimg = rightactorbottompreflip

            if leftactortop != False and leftactormiddle != False and leftactorbottom == False:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 500, screeny / 2 - 50))
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 700, screeny / 2 + 50))
                leftactortopplacement = True
                leftactormiddleplacement = True
            if leftactortop != False and leftactorbottom != False and leftactormiddle == False:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 500, screeny / 2 - 50))
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50))
                leftactortopplacement = True
                leftactorbottomplacement = True
            if leftactormiddle != False and leftactorbottom != False and leftactortop == False:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 500, screeny / 2 - 50))
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50))
                leftactormiddleplacement = True
                leftactorbottomplacement = True

            elif leftactortop != False and leftactormiddle == False and leftactorbottom == False:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 600, screeny / 2))
                leftactortopplacement = True
            elif leftactormiddle != False and leftactortop == False and leftactorbottom == False:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 600, screeny / 2))
                leftactormiddleplacement = True
            elif leftactorbottom != False and leftactortop == False and leftactormiddle == False:
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 600, screeny / 2))
                leftactorbottomplacement = True

            if leftactortop != False and leftactortopplacement != True:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 450, screeny / 2 - 100))
            if leftactormiddle != False and leftactormiddleplacement != True:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 600, screeny / 2))
            if leftactorbottom != False and leftactorbottomplacement != True:
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 750, screeny / 2 + 100))

            rightactortop = rightactortoppreflip
            rightactormid = rightactormiddlepreflip
            rightactorbot = rightactorbottompreflip

            if rightactortoppreflip != False and rightactormiddlepreflip != False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 700, screeny / 2 + 50))
                rightactortopplacement = True
                rightactormiddleplacement = True
            if rightactortoppreflip != False and rightactorbottompreflip != False and rightactormiddlepreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50))
                rightactortopplacement = True
                rightactorbottomplacement = True
            if rightactormiddlepreflip != False and rightactorbottompreflip != False and rightactortoppreflip == False:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50))
                rightactormiddleplacement = True
                rightactorbottomplacement = True

            elif rightactortoppreflip != False and rightactormiddlepreflip == False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 600, screeny / 2))
                rightactortopplacement = True
            elif rightactormiddlepreflip != False and rightactortoppreflip == False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 600, screeny / 2))
                rightactormiddleplacement = True
            elif rightactorbottompreflip != False and rightactortoppreflip == False and rightactormiddlepreflip == False:
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 600, screeny / 2))
                rightactorbottomplacement = True

            if rightactortoppreflip != False and rightactortopplacement != True:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 450, screeny / 2 - 100))
            if rightactormiddlepreflip != False and rightactormiddleplacement != True:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 600, screeny / 2))
            if rightactorbottompreflip != False and rightactorbottomplacement != True:
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 750, screeny / 2 + 100))

        def combat(lst):
            global turninit
            global recieveinput
            global circleY
            global circleX
            global unit1attackbar, unit2attackbar, unit3attackbar, unit4attackbar, unit5attackbar, unit6attackbar

            # combatantsspeedindex = []
            # combatantsspeed = []
            #
            # for i, x in enumerate(combatants):
            #     if x == False:
            #         continue
            #     combatantsspeed.append(combatants[i].speed)
            #     combatantsspeedindex.append(i)
            #
            # fastestinindex = max(combatantsspeed)
            #
            # fastestinindexpos = combatantsspeed.index(fastestinindex)
            #
            # x = combatantsspeedindex[fastestinindexpos]
            #
            # turn = combatants[x]

            allyteam = combatants[0:3]
            enemyteam = combatants[3:6]

            # if turn in allyteam:
            #    allyturn = True

            pygame.time.set_timer(pygame.USEREVENT + 1, 1)

            top_left_3 = (358, 690)
            mid_left_3 = (194, 786)
            bot_left_3 = (44, 890)

            top_left_2 = (312, 740)
            bot_left_2 = (90, 842)

            mid_left_1 = (210, 792)

            top_right_3 = (1330, 688)
            mid_right_3 = (1478, 794)
            bot_right_3 = (1630, 888)

            top_right_2 = (1376, 742)
            bot_right_2 = (1576, 842)

            mid_right_1 = (1480, 792)

            if unit1attackbar >= 100:
                turn = 0
            elif unit2attackbar >= 100:
                turn = 1
            elif unit3attackbar >= 100:
                turn = 2
            elif unit4attackbar >= 100:
                turn = 3
            elif unit5attackbar >= 100:
                turn = 4
            elif unit6attackbar >= 100:
                turn = 5

            else:
                turn = None

            lefttwo = False
            leftsolomid = False
            leftthree = False

            if combatants[0] == False and combatants[1] == False:
                leftsolomid = True
            if combatants[1] == False and combatants[2] == False:
                leftsolomid = True
            if combatants[0] == False and combatants[2] == False:
                leftsolomid = True
            if combatants[0] != False and combatants[1] != False and combatants[2] == False:
                lefttwo = True
            if combatants[0] != False and combatants[1] == False and combatants[2] != False:
                lefttwo = True
            if combatants[0] == False and combatants[1] != False and combatants[2] != False:
                lefttwo = True
            if combatants[0] != False and combatants[1] != False and combatants[2] != False:
                leftthree = True

            righttwo = False
            rightsolomid = False
            rightthree = False

            if combatants[3] == False and combatants[4] == False:
                rightsolomid = True
            if combatants[4] == False and combatants[5] == False:
                rightsolomid = True
            if combatants[3] == False and combatants[5] == False:
                rightsolomid = True
            if combatants[3] != False and combatants[4] != False and combatants[5] == False:
                righttwo = True
            if combatants[3] != False and combatants[4] == False and combatants[5] != False:
                righttwo = True
            if combatants[3] == False and combatants[4] != False and combatants[5] != False:
                righttwo = True
            if combatants[3] != False and combatants[4] != False and combatants[5] != False:
                rightthree = True

            if rightsolomid == True and turn == 3:
                screen.blit(turncircle, mid_right_1)
            elif rightsolomid == True and turn == 4:
                screen.blit(turncircle, mid_right_1)
            elif rightsolomid == True and turn == 5:
                screen.blit(turncircle, mid_right_1)

            if righttwo == True and turn == 3 and combatants[5] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 4 and combatants[5] == False:
                screen.blit(turncircle, bot_right_2)

            elif righttwo == True and turn == 5 and combatants[4] == False:
                screen.blit(turncircle, bot_right_2)

            elif righttwo == True and turn == 3 and combatants[4] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 4 and combatants[3] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 5 and combatants[3] == False:
                screen.blit(turncircle, bot_right_2)

            if rightthree == True and turn == 3:
                screen.blit(turncircle, top_right_3)
            elif rightthree == True and turn == 4:
                screen.blit(turncircle, mid_right_3)
            elif rightthree == True and turn == 5:
                screen.blit(turncircle, bot_right_3)

            if leftsolomid == True and turn == 0:
                screen.blit(turncircle, mid_left_1)
            elif leftsolomid == True and turn == 1:
                screen.blit(turncircle, mid_left_1)
            elif leftsolomid == True and turn == 2:
                screen.blit(turncircle, mid_left_1)

            if lefttwo == True and turn == 0 and combatants[2] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 1 and combatants[2] == False:
                screen.blit(turncircle, bot_left_2)

            elif lefttwo == True and turn == 2 and combatants[1] == False:
                screen.blit(turncircle, bot_left_2)

            elif lefttwo == True and turn == 0 and combatants[1] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 1 and combatants[0] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 2 and combatants[0] == False:
                screen.blit(turncircle, bot_left_2)

            if leftthree == True and turn == 0:
                screen.blit(turncircle, top_left_3)
            elif leftthree == True and turn == 1:
                screen.blit(turncircle, mid_left_3)
            elif leftthree == True and turn == 2:
                screen.blit(turncircle, bot_left_3)

            if rightsolomid == True and turn == 3:
                screen.blit(turncircle, mid_right_1)
            elif rightsolomid == True and turn == 4:
                screen.blit(turncircle, mid_right_1)
            elif rightsolomid == True and turn == 5:
                screen.blit(turncircle, mid_right_1)

            if righttwo == True and turn == 3 and combatants[5] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 4 and combatants[5] == False:
                screen.blit(turncircle, bot_right_2)

            elif righttwo == True and turn == 5 and combatants[4] == False:
                screen.blit(turncircle, bot_right_2)

            elif righttwo == True and turn == 3 and combatants[4] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 4 and combatants[3] == False:
                screen.blit(turncircle, top_right_2)

            elif righttwo == True and turn == 5 and combatants[3] == False:
                screen.blit(turncircle, bot_right_2)

            if rightthree == True and turn == 3:
                screen.blit(turncircle, top_right_3)
            elif rightthree == True and turn == 4:
                screen.blit(turncircle, mid_right_3)
            elif rightthree == True and turn == 5:
                screen.blit(turncircle, bot_right_3)

            if leftsolomid == True and turn == 0:
                screen.blit(turncircle, mid_left_1)
            elif leftsolomid == True and turn == 1:
                screen.blit(turncircle, mid_left_1)
            elif leftsolomid == True and turn == 2:
                screen.blit(turncircle, mid_left_1)

            if lefttwo == True and turn == 0 and combatants[2] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 1 and combatants[2] == False:
                screen.blit(turncircle, bot_left_2)

            elif lefttwo == True and turn == 2 and combatants[1] == False:
                screen.blit(turncircle, bot_left_2)

            elif lefttwo == True and turn == 0 and combatants[1] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 1 and combatants[0] == False:
                screen.blit(turncircle, top_left_2)

            elif lefttwo == True and turn == 2 and combatants[0] == False:
                screen.blit(turncircle, bot_left_2)

            if leftthree == True and turn == 0:
                screen.blit(turncircle, top_left_3)
            elif leftthree == True and turn == 1:
                screen.blit(turncircle, mid_left_3)
            elif leftthree == True and turn == 2:
                screen.blit(turncircle, bot_left_3)

        combat(combatants)
        combatimages(combatants)
        mx, my = pygame.mouse.get_pos()

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        pygame.display.update()
        Clock.tick(120)

demo()
