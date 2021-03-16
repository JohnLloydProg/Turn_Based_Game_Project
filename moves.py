import pygame


class Move:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.type = "None"
        self.starting_turn = 0
        self.cd = 0

    def is_inside(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x+self.w >= mouse_x >= self.x and self.y+self.h >= mouse_y >= self.y:
            return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))


class ArcherAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 1.5
        self.type = "attack"
        self.effect = "None"


class SpearAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 1
        self.type = "attack"
        self.effect = "None"


class MageAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 1.75
        self.type = "attack"
        self.effect = "None"


class BossAttack(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.damage_multiplier = 2
        self.type = "attack"
        self.effect = "None"


class MageBuff(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.type = "buff"
        self.stat_target = "health"
        self.stat_increase = 0.2


class BossBuff(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.type = "buff"
        self.stat_target = "armor"
        self.duration = 3
        self.stat_increase = 0.75


class SpearBuff(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.type = "buff"
        self.stat_target = "attack"
        self.duration = 3
        self.stat_increase = 0.5


class SpearStun(Move):
    def __init__(self, x, y, w, h, color):
        Move.__init__(self, x, y, w, h, color)
        self.type = "attack"
        self.effect = "stun"
        self.damage_multiplier = 1
