# Setup Functions ------------------------------------- #
import json
import os
import random
import sys
import time
from units import Archer, Mage, Spear, Boss

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

AttackBar0_0 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_0.png')
AttackBar0_5 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_1.png')
AttackBar5_10 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_2.png')
AttackBar10_15 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_3.png')
AttackBar15_20= loadtransimg('images/Unit Gui/AttackBars/AttackBar_4.png')
AttackBar20_25 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_5.png')
AttackBar25_30 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_6.png')
AttackBar30_35 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_7.png')
AttackBar35_40 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_8.png')
AttackBar40_45 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_9.png')
AttackBar45_50 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_10.png')
AttackBar50_55 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_11.png')
AttackBar55_60 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_12.png')
AttackBar60_65 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_13.png')
AttackBar65_70 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_14.png')
AttackBar70_75 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_15.png')
AttackBar75_80 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_16.png')
AttackBar80_85 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_17.png')
AttackBar85_90 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_18.png')
AttackBar90_95 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_19.png')
AttackBar95_100 = loadtransimg('images/Unit Gui/AttackBars/AttackBar_20.png')

HealthBar0_0 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_0.png')
HealthBar0_5 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_1.png')
HealthBar5_10 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_2.png')
HealthBar10_15 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_3.png')
HealthBar15_20= loadtransimg('images/Unit Gui/HealthBars/HealthBar_4.png')
HealthBar20_25 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_5.png')
HealthBar25_30 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_6.png')
HealthBar30_35 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_7.png')
HealthBar35_40 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_8.png')
HealthBar40_45 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_9.png')
HealthBar45_50 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_10.png')
HealthBar50_55 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_11.png')
HealthBar55_60 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_12.png')
HealthBar60_65 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_13.png')
HealthBar65_70 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_14.png')
HealthBar70_75 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_15.png')
HealthBar75_80 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_16.png')
HealthBar80_85 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_17.png')
HealthBar85_90 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_18.png')
HealthBar90_95 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_19.png')
HealthBar95_100 = loadtransimg('images/Unit Gui/HealthBars/HealthBar_20.png')

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



unit1 = Mage(808, 8595, 476, 111, MageFrame)
unit2 = Boss(1450, 11700, 637, 95, BossFrame)
unit3 = Archer(1602, 6540, 436, 101, ArcherFrame)
unit4 = Spear(1082, 8155, 371, 106, SpearFrame)
unit5 = Mage(808, 8595, 476, 111, MageFrame)
unit6 = Archer(1602, 6540, 436, 101, ArcherFrame)




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

coordx = screenx / 2
coordy = screeny / 2



def demo():
    global unit1attackbar, unit2attackbar, unit3attackbar, unit4attackbar, unit5attackbar, unit6attackbar, turninit
    global turn
    running = True
    combatants = [False, unit2, False, unit4, unit5, unit6]
    ally_turns = 0
    enemy_turns = 0
    current_turn = None
    location = None
    buff_available = True
    buffs = []
    guis = []

    allyteam = combatants[0:3]
    enemyteam = combatants[3:6]

    for combatant in combatants:
        if combatant:
            if combatant.stillframe == BossFrame and combatant in allyteam:
                combatant.xpos = combatant.stillframe.get_width() / 2 - 60

            if combatant.stillframe == BossFrame and combatant in enemyteam:
                combatant.xpos = combatant.stillframe.get_width() / 2 + 60




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

        global coordx, coordy
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # if event.key == K_a:
                #     coordx -= 5
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_d:
                #     coordx += 5
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_w:
                #     coordy -= 5
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_s:
                #     coordy += 5
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                #
                # if event.key == K_KP4:
                #     coordx -= 50
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_KP6:
                #     coordx += 50
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_KP8:
                #     coordy -= 50
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))
                # if event.key == K_KP2:
                #     coordy += 50
                #     print('\n\n\n\n\n\nX = ' + str(coordx) + '\nY = ' + str(coordy))

            if event.type == pygame.USEREVENT + 1:
                if not turninit:
                    if combatants[0] and combatants[0].state != "dead":
                        unit1attackbar += speedpercentage(combatants[0].speed)
                    if combatants[1] and combatants[1].state != "dead":
                        unit2attackbar += speedpercentage(combatants[1].speed)
                    if combatants[2] and combatants[2].state != "dead":
                        unit3attackbar += speedpercentage(combatants[2].speed)
                    if combatants[3] and combatants[3].state != "dead":
                        unit4attackbar += speedpercentage(combatants[3].speed)
                    if combatants[4] and combatants[4].state != "dead":
                        unit5attackbar += speedpercentage(combatants[4].speed)
                    if combatants[5] and combatants[5].state != "dead":
                        unit6attackbar += speedpercentage(combatants[5].speed)
            if unit1attackbar >= 100:
                turninit = True
                recieveinput = False
                guis = combatants[0].moves
                if not recieveinput:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for gui in guis:
                            if gui.is_inside():
                                if combatants[0].turns - gui.starting_turn >= gui.cd:
                                    if gui.type == "attack":
                                        current_turn = combatants[0]
                                    elif gui.type == "buff":
                                        for buff in buffs:
                                            if buff[0] == "allies" and buff[1] == gui.stat_target:
                                                buffs.remove(buff)
                                                buff_available = False
                                                break
                                        for ally in allyteam:
                                            if ally:
                                                if gui.stat_target == "attack":
                                                    if buff_available:
                                                        ally.attack += ally.attack*gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "armor":
                                                    if buff_available:
                                                        ally.armor += ally.armor*gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "health":
                                                    if ally.hitpoints < ally.full_health:
                                                        ally.hitpoints += ally.full_health*gui.stat_increase
                                                        if ally.hitpoints > ally.full_health:
                                                            ally.hitpoints = ally.full_health
                                                    gui.cd = 4
                                        if gui.stat_target != "health":
                                            buffs.append(("allies", gui.stat_target, gui.stat_increase,
                                                          ally_turns, gui.duration))
                                            ally_turns -= 1
                                        gui.starting_turn = combatants[0].turns+1
                                        unit1attackbar = 0
                                        recieveinput = True
                                        turninit = False
                                        guis = []
                                        combatants[0].turns += 1
                                        ally_turns += 1
                                        current_turn = None
                                        buff_available = True
            elif unit2attackbar >= 100:
                turninit = True
                recieveinput = False
                guis = combatants[1].moves
                if not recieveinput:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for gui in guis:
                            if gui.is_inside():
                                if combatants[1].turns - gui.starting_turn >= gui.cd:
                                    if gui.type == "attack":
                                        current_turn = combatants[1]
                                    elif gui.type == "buff":
                                        for buff in buffs:
                                            if buff[0] == "allies" and buff[1] == gui.stat_target:
                                                buffs.remove(buff)
                                                buff_available = False
                                                break
                                        for ally in allyteam:
                                            if ally:
                                                if gui.stat_target == "attack":
                                                    if buff_available:
                                                        ally.attack += ally.attack * gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "armor":
                                                    if buff_available:
                                                        ally.armor += ally.armor * gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "health":
                                                    if ally.hitpoints < ally.full_health:
                                                        ally.hitpoints += ally.full_health * gui.stat_increase
                                                        if ally.hitpoints > ally.full_health:
                                                            ally.hitpoints = ally.full_health
                                                    gui.cd = 4
                                        if gui.stat_target != "health":
                                            buffs.append(("allies", gui.stat_target, gui.stat_increase, ally_turns,
                                                          gui.duration))
                                            ally_turns -= 1
                                        gui.starting_turn = combatants[1].turns + 1
                                        unit2attackbar = 0
                                        recieveinput = True
                                        turninit = False
                                        guis = []
                                        combatants[1].turns += 1
                                        ally_turns += 1
                                        current_turn = None
                                        buff_available = True
            elif unit3attackbar >= 100:
                turninit = True
                recieveinput = False
                guis = combatants[2].moves
                if not recieveinput:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for gui in guis:
                            if gui.is_inside():
                                if combatants[2].turns - gui.starting_turn >= gui.cd:
                                    if gui.type == "attack":
                                        current_turn = combatants[2]
                                    elif gui.type == "buff":
                                        for buff in buffs:
                                            if buff[0] == "allies" and buff[1] == gui.stat_target:
                                                buffs.remove(buff)
                                                buff_available = False
                                                break
                                        for ally in allyteam:
                                            if ally:
                                                if gui.stat_target == "attack":
                                                    if buff_available:
                                                        ally.attack += ally.attack * gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "armor":
                                                    if buff_available:
                                                        ally.armor += ally.armor * gui.stat_increase
                                                    gui.cd = 4
                                                elif gui.stat_target == "health":
                                                    if ally.hitpoints < ally.full_health:
                                                        ally.hitpoints += ally.full_health * gui.stat_increase
                                                        if ally.hitpoints > ally.full_health:
                                                            ally.hitpoints = ally.full_health
                                                    gui.cd = 4
                                        if gui.stat_target != "health":
                                            buffs.append(("allies", gui.stat_target, gui.stat_increase, ally_turns,
                                                          gui.duration))
                                            ally_turns -= 1
                                        gui.starting_turn = combatants[2].turns + 1
                                        unit3attackbar = 0
                                        recieveinput = True
                                        turninit = False
                                        guis = []
                                        combatants[2].turns += 1
                                        ally_turns += 1
                                        current_turn = None
                                        buff_available = True
            elif unit4attackbar >= 100:
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit4attackbar = 0
                            recieveinput = True
                            turninit = False
                            enemy_turns += 1
            elif unit5attackbar >= 100:
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit5attackbar = 0
                            recieveinput = True
                            turninit = False
                            enemy_turns += 1
            elif unit6attackbar >= 100:
                turninit = True
                recieveinput = False
                if not recieveinput:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            unit6attackbar = 0
                            recieveinput = True
                            turninit = False
                            enemy_turns += 1
            else:
                turninit = False
                recieveinput = True

            if current_turn == combatants[0]:
                for enemy in enemyteam:
                    if enemy.is_inside() and enemy.state != "dead":
                        location = (enemy.pos[0] + 120, enemy.pos[1] - 80)
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if random.choice([False, False, True, False]):
                                critical_multiplier = 2
                            else:
                                critical_multiplier = 1
                            enemy.hitpoints -= ((combatants[0].attack*combatants[0].attack_move.damage_multiplier) - enemy.armor) * critical_multiplier
                            unit1attackbar = 0
                            recieveinput = True
                            turninit = False
                            guis = []
                            combatants[0].turns += 1
                            ally_turns += 1
                            current_turn = None
                            location = None
            elif current_turn == combatants[1]:
                for enemy in enemyteam:
                    if enemy.is_inside() and enemy.state != "dead":
                        location = (enemy.pos[0] + 120, enemy.pos[1] - 80)
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if random.choice([False, False, True, False]):
                                critical_multiplier = 2
                            else:
                                critical_multiplier = 1
                            enemy.hitpoints -= ((combatants[1].attack*combatants[1].attack_move.damage_multiplier) - enemy.armor) * critical_multiplier
                            unit2attackbar = 0
                            recieveinput = True
                            turninit = False
                            guis = []
                            combatants[1].turns += 1
                            ally_turns += 1
                            current_turn = None
                            location = None
            elif current_turn == combatants[2]:
                for enemy in enemyteam:
                    if enemy.is_inside() and enemy.state != "dead":
                        location = (enemy.pos[0] + 120, enemy.pos[1] - 80)
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if random.choice([False, False, True, False]):
                                critical_multiplier = 2
                            else:
                                critical_multiplier = 1
                            enemy.hitpoints -= ((combatants[2].attack*combatants[2].attack_move.damage_multiplier) - enemy.armor) * critical_multiplier
                            unit3attackbar = 0
                            recieveinput = True
                            turninit = False
                            guis = []
                            combatants[2].turns += 1
                            ally_turns += 1
                            current_turn = None
                            location = None

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
                list[0].pos = (screenx / 2 - list[0].xpos - 500, screeny / 2 - 50)
                list[1].pos = (screenx / 2 - list[1].xpos - 700, screeny / 2 + 50)
                leftactortopplacement = True
                leftactormiddleplacement = True
            if leftactortop != False and leftactorbottom != False and leftactormiddle == False:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 500, screeny / 2 - 50))
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50))
                list[0].pos = (screenx / 2 - list[0].xpos - 500, screeny / 2 - 50)
                list[2].pos = (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50)
                leftactortopplacement = True
                leftactorbottomplacement = True
            if leftactormiddle != False and leftactorbottom != False and leftactortop == False:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 500, screeny / 2 - 50))
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50))
                list[1].pos = (screenx / 2 - list[1].xpos - 500, screeny / 2 - 50)
                list[2].pos = (screenx / 2 - list[2].xpos - 700, screeny / 2 + 50)
                leftactormiddleplacement = True
                leftactorbottomplacement = True

            elif leftactortop != False and leftactormiddle == False and leftactorbottom == False:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 600, screeny / 2))
                list[0].pos = (screenx / 2 - list[0].xpos - 600, screeny / 2)
                leftactortopplacement = True
            elif leftactormiddle != False and leftactortop == False and leftactorbottom == False:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 600, screeny / 2))
                list[1].pos = (screenx / 2 - list[1].xpos - 600, screeny / 2)
                leftactormiddleplacement = True
            elif leftactorbottom != False and leftactortop == False and leftactormiddle == False:
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 600, screeny / 2))
                list[2].pos = (screenx / 2 - list[2].xpos - 600, screeny / 2)
                leftactorbottomplacement = True

            if leftactortop != False and leftactortopplacement != True:
                screen.blit(leftactortop, (screenx / 2 - list[0].xpos - 450, screeny / 2 - 100))
                list[0].pos = (screenx / 2 - list[0].xpos - 450, screeny / 2 - 100)
            if leftactormiddle != False and leftactormiddleplacement != True:
                screen.blit(leftactormiddle, (screenx / 2 - list[1].xpos - 600, screeny / 2))
                list[1].pos = (screenx / 2 - list[1].xpos - 600, screeny / 2)
            if leftactorbottom != False and leftactorbottomplacement != True:
                screen.blit(leftactorbottom, (screenx / 2 - list[2].xpos - 750, screeny / 2 + 100))
                list[2].pos = (screenx / 2 - list[2].xpos - 750, screeny / 2 + 100)

            rightactortop = rightactortoppreflip
            rightactormid = rightactormiddlepreflip
            rightactorbot = rightactorbottompreflip

            if rightactortoppreflip != False and rightactormiddlepreflip != False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 700, screeny / 2 + 50))
                list[3].pos = (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50)
                list[4].pos = (screenx / 2 - list[4].xpos + 700, screeny / 2 + 50)
                rightactortopplacement = True
                rightactormiddleplacement = True
            if rightactortoppreflip != False and rightactorbottompreflip != False and rightactormiddlepreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50))
                list[3].pos = (screenx / 2 - list[3].xpos + 500, screeny / 2 - 50)
                list[5].pos = (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50)
                rightactortopplacement = True
                rightactorbottomplacement = True
            if rightactormiddlepreflip != False and rightactorbottompreflip != False and rightactortoppreflip == False:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 500, screeny / 2 - 50))
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50))
                list[4].pos = (screenx / 2 - list[4].xpos + 500, screeny / 2 - 50)
                list[5].pos = (screenx / 2 - list[5].xpos + 700, screeny / 2 + 50)
                rightactormiddleplacement = True
                rightactorbottomplacement = True

            elif rightactortoppreflip != False and rightactormiddlepreflip == False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 600, screeny / 2))
                list[3].pos = (screenx / 2 - list[3].xpos + 600, screeny / 2)
                rightactortopplacement = True
            elif rightactormiddlepreflip != False and rightactortoppreflip == False and rightactorbottompreflip == False:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 600, screeny / 2))
                list[4].pos = (screenx / 2 - list[4].xpos + 600, screeny / 2)
                rightactormiddleplacement = True
            elif rightactorbottompreflip != False and rightactortoppreflip == False and rightactormiddlepreflip == False:
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 600, screeny / 2))
                list[5].pos = (screenx / 2 - list[5].xpos + 600, screeny / 2)
                rightactorbottomplacement = True

            if rightactortoppreflip != False and rightactortopplacement != True:
                screen.blit(pygame.transform.flip(rightactortop, True, False),
                            (screenx / 2 - list[3].xpos + 450, screeny / 2 - 100))
                list[3].pos = (screenx / 2 - list[3].xpos + 450, screeny / 2 - 100)
            if rightactormiddlepreflip != False and rightactormiddleplacement != True:
                screen.blit(pygame.transform.flip(rightactormid, True, False),
                            (screenx / 2 - list[4].xpos + 600, screeny / 2))
                list[4].pos = (screenx / 2 - list[4].xpos + 600, screeny / 2)
            if rightactorbottompreflip != False and rightactorbottomplacement != True:
                screen.blit(pygame.transform.flip(rightactorbot, True, False),
                            (screenx / 2 - list[5].xpos + 750, screeny / 2 + 100))
                list[5].pos = (screenx / 2 - list[5].xpos + 750, screeny / 2 + 100)

            # Displaying Unit Bars

            if rightsolomid == True:
                if combatants[3] and combatants[3].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[3].hud(unit4attackbar,
                                                                                                       HUD_mid_right_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                elif combatants[4] and combatants[4].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[4].hud(unit5attackbar,
                                                                                                       HUD_mid_right_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                elif combatants[5] and combatants[5].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[5].hud(unit6attackbar,
                                                                                                       HUD_mid_right_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[3] != False and combatants[5] == False:
                if combatants[3].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[3].hud(unit4attackbar,
                                                                                                       HUD_top_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[4] != False and combatants[5] == False:
                if combatants[4].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[4].hud(unit5attackbar,
                                                                                                       HUD_bot_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[5] != False and combatants[4] == False:
                if combatants[5].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[5].hud(unit6attackbar,
                                                                                                       HUD_bot_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[3] != False and combatants[4] == False:
                if combatants[3].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[3].hud(unit4attackbar,
                                                                                                       HUD_top_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[4] != False and combatants[3] == False:
                if combatants[4].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[4].hud(unit5attackbar,
                                                                                                       HUD_top_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if righttwo == True and combatants[5] != False and combatants[3] == False:
                if combatants[5].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[5].hud(unit6attackbar,
                                                                                                       HUD_bot_right_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if rightthree == True:
                if combatants[3].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[3].hud(unit4attackbar,
                                                                                                       HUD_top_right_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                if combatants[4].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[4].hud(unit5attackbar,
                                                                                                       HUD_mid_right_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                if combatants[5].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[5].hud(unit6attackbar,
                                                                                                       HUD_bot_right_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if leftsolomid == True:
                if combatants[0] and combatants[0].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[0].hud(unit1attackbar,
                                                                                                       HUD_mid_left_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                elif combatants[1] and combatants[1].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[1].hud(unit2attackbar,
                                                                                                       HUD_mid_left_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                elif combatants[2] and combatants[2].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[2].hud(unit3attackbar,
                                                                                                       HUD_mid_left_1)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if lefttwo == True and combatants[0] != False and combatants[2] == False:
                if combatants[0].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[0].hud(unit1attackbar,
                                                                                                       HUD_top_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                    screen.blit(UnitHud, HUD_top_left_2)

            if lefttwo == True and combatants[1] != False and combatants[2] == False:
                if combatants[1].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[1].hud(unit2attackbar,
                                                                                                       HUD_bot_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                    screen.blit(UnitHud, HUD_bot_left_2)

            if lefttwo == True and combatants[2] != False and combatants[1] == False:
                if combatants[2].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[2].hud(unit3attackbar,
                                                                                                       HUD_bot_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if lefttwo == True and combatants[0] != False and combatants[1] == False:
                if combatants[0].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[0].hud(unit1attackbar,
                                                                                                       HUD_top_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if lefttwo == True and combatants[1] != False and combatants[0] == False:
                if  combatants[1].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[1].hud(unit2attackbar,
                                                                                                       HUD_top_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if lefttwo == True and combatants[2] != False and combatants[0] == False:
                if combatants[2].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[2].hud(unit3attackbar,
                                                                                                       HUD_bot_left_2)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)

            if leftthree == True:
                if combatants[0].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[0].hud(unit1attackbar, HUD_top_left_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                if combatants[1].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[1].hud(unit2attackbar,
                                                                                                       HUD_mid_left_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)
                if combatants[2].state != "dead":
                    [(health_bar, health_bar_coor), (attack_bar, attack_bar_coor)] = combatants[2].hud(unit3attackbar,
                                                                                                       HUD_bot_left_3)
                    screen.blit(health_bar, health_bar_coor)
                    screen.blit(attack_bar, attack_bar_coor)


        def combat(lst):
            global turninit
            global recieveinput
            global circleY
            global circleX
            global unit1attackbar, unit2attackbar, unit3attackbar, unit4attackbar, unit5attackbar, unit6attackbar
            global leftsolomid, lefttwo, leftthree, rightsolomid, righttwo, rightthree
            global HUD_top_left_3, HUD_mid_left_3, HUD_bot_left_3, HUD_top_right_3, HUD_mid_right_3, HUD_bot_right_3
            global HUD_top_left_2, HUD_bot_left_2, HUD_top_right_2, HUD_bot_right_2
            global HUD_mid_left_1, HUD_mid_right_1
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


            # if turn in allyteam:
            #    allyturn = True

            pygame.time.set_timer(pygame.USEREVENT + 1, 1)

            # Turn Circle Positions

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

            # Unit Hud Positions
            # HUD_mid_left_1 = (210, 792) + 30 -242

            HUD_top_left_3 = (388, 448)
            HUD_mid_left_3 = (224, 544)
            HUD_bot_left_3 = (74, 648)

            HUD_top_left_2 = (342, 498)
            HUD_bot_left_2 = (120, 600)

            HUD_mid_left_1 = (240, 550)

            HUD_top_right_3 = (1310, 446)
            HUD_mid_right_3 = (1458, 552)
            HUD_bot_right_3 = (1610, 646)

            HUD_top_right_2 = (1356, 500)
            HUD_bot_right_2 = (1556, 600)

            HUD_mid_right_1 = (1460, 550)


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

            # Defining unit positioning

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

            # Displaying turn circles

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

        for i in range(len(combatants)):
            combatant = combatants[i]
            if combatant:
                if combatant.state == "idle":
                    combatant.idle()
                elif combatant.state == "dead":
                    combatant.dead()
                if combatant.hitpoints == 0 and combatant.state != "dead":
                    if i == 0:
                        unit1attackbar = 0
                    elif i == 1:
                        unit2attackbar = 0
                    elif i == 2:
                        unit3attackbar = 0
                    elif i == 3:
                        unit4attackbar = 0
                    elif i == 4:
                        unit5attackbar = 0
                    elif i == 5:
                        unit6attackbar = 0
                    combatant.animation_counter = 0
                    combatant.state = "dead"

        combat(combatants)
        combatimages(combatants)

        for gui in guis:
            gui.draw(screen)

        if location:
            screen.blit(pygame.image.load("pixelarrow.png"), location)

        # ("allies", gui.stat_target, gui.stat_increase, turns, gui.duration)
        for ally in allyteam:
            if ally:
                for i, buff in enumerate(buffs):
                    if buff[0] == "allies":
                        if ally_turns - buff[3] == buff[4]:
                            if buff[1] == "attack":
                                ally.attack = ally.base_attack
                            elif buff[1] == "armor":
                                ally.armor = ally.base_armor
                            buffs.remove(buff)
                        if buff[1] == "attack":
                            pygame.draw.rect(screen, (255, 0, 0), ((ally.pos[0]+20)+(40*i), ally.pos[1]-30, 30, 30))
                        elif buff[1] == "armor":
                            pygame.draw.rect(screen, (0, 0, 255), ((ally.pos[0]+20)+(40*i), ally.pos[1]-30, 30, 30))

        # Mouse icon change

        pygame.mouse.set_visible(False)
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        pygame.display.update()
        Clock.tick(120)


main_menu()
