import pygame


def loadtransimg(imgname):
    return pygame.image.load(imgname).convert_alpha()


class Unit:
    def __init__(self, attack, hitpoints, speed, stillframe):
        self.attack = attack
        self.hitpoints = hitpoints
        self.speed = speed
        self.stillframe = stillframe
        self.ypos = stillframe.get_height() / 2


class Archer(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2


class Spear(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2


class Mage(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2


class Boss(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2 - 60
