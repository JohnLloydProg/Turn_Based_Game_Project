import pygame


class Move:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.type = None

    def is_inside(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x+self.w >= mouse_x >= self.x and self.y+self.h >= mouse_y >= self.y:
            return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))


class ArcherAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 0.5
        self.type = "attack"


class SpearAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 1
        self.type = "attack"


class MageAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 0.75
        self.type = "attack"


class BossAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 2
        self.type = "attack"


class MageBuff(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.type = "buff"
        self.stat_target = "attack"
        self.duration = 3
        self.stat_increase = 0.5
