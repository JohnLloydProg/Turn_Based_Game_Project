import pygame


class Move:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.type = "None"
        self.starting_turn = 0
        self.cd = 0
        self.in_cooldown = False

    def is_inside(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x+100 >= mouse_x >= self.x and self.y+100 >= mouse_y >= self.y:
            return True

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class ArcherAttack(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.damage_multiplier = 1.5
        self.type = "attack"
        self.effect = "None"


class SpearAttack(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.damage_multiplier = 1
        self.type = "attack"
        self.effect = "stun"


class MageAttack(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.damage_multiplier = 1.75
        self.type = "attack"
        self.effect = "None"


class BossAttack(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.damage_multiplier = 2
        self.type = "attack"
        self.effect = "None"


class MageBuff(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.type = "buff"
        self.stat_target = "health"
        self.stat_increase = 0.2


class BossBuff(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.type = "buff"
        self.stat_target = "armor"
        self.duration = 3
        self.stat_increase = 0.75


class SpearBuff(Move):
    def __init__(self, x, y, image):
        Move.__init__(self, x, y, image)
        self.type = "attack"
        self.effect = "buff"
        self.stat_target = "attack"
        self.damage_multiplier = 1
        self.duration = 3
        self.stat_increase = 0.5
