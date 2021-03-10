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
        self.idle_animation = [loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 1.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 2.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 3.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 4.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 5.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 6.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 7.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 8.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 9.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 10.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 11.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 12.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png')]
        self.state = "idle"
        self.animation_counter = 0

    def update(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*5:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//5]
        self.animation_counter += 1


class Spear(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2
        self.idle_animation = [loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton1.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton2.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton3.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton4.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton5.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton6.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton7.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton8.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton9.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton10.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton11.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton12.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png')]
        self.state = "idle"
        self.animation_counter = 0

    def update(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*5:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//5]
        self.animation_counter += 1


class Mage(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2
        self.idle_animation = [loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export1.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export2.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export3.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export4.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export5.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export6.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export7.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export8.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export9.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export10.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export11.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export12.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png')]
        self.state = "idle"
        self.animation_counter = 0

    def update(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*5:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//5]
        self.animation_counter += 1


class Boss(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2 - 60
        self.idle_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss1.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss2.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss3.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss4.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss5.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss6.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss7.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss8.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss9.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss10.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss11.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss12.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss13.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png')]
        self.state = "idle"
        self.animation_counter = 0

    def update(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*5:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//5]
        self.animation_counter += 1
