import pygame
import moves


def loadtransimg(imgname):
    return pygame.image.load(imgname).convert_alpha()


tickspeed = 16


class Unit:
    def __init__(self, attack, hitpoints, speed, stillframe):
        self.attack = attack
        self.hitpoints = hitpoints
        self.full_health = hitpoints
        self.speed = speed
        self.stillframe = stillframe
        self.ypos = stillframe.get_height() / 2
        self.state = "idle"
        self.idle_animation = []
        self.animation_counter = 0
        self.health_bar_images = [loadtransimg('images/Unit Gui/HealthBars/HealthBar_0.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_1.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_2.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_3.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_4.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_5.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_6.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_7.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_8.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_9.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_10.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_11.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_12.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_13.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_14.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_15.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_16.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_17.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_18.png'), loadtransimg('images/Unit Gui/HealthBars/HealthBar_19.png'),
                                  loadtransimg('images/Unit Gui/HealthBars/HealthBar_20.png')]
        self.attack_bar_images = [loadtransimg('images/Unit Gui/AttackBars/AttackBar_0.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_1.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_2.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_3.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_4.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_5.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_6.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_7.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_8.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_9.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_10.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_11.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_12.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_13.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_14.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_15.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_16.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_17.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_18.png'), loadtransimg('images/Unit Gui/AttackBars/AttackBar_19.png'),
                                  loadtransimg('images/Unit Gui/AttackBars/AttackBar_20.png')]

    def hud(self, attackbar, coordinates):
        if attackbar > 100:
            attackbar = 100
        healt_bar_image = self.health_bar_images[int((self.hitpoints/self.full_health)*100//5)]
        attack_bar_image = self.attack_bar_images[int(attackbar//5)]
        return [(healt_bar_image, coordinates), (attack_bar_image, (coordinates[0], coordinates[1]+32))]

    def idle(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*tickspeed:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//tickspeed]
        self.animation_counter += 1


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
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png'),
                               loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Idle/Archer Skeleton 13.png')]
        self.death_animation = [loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 37.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 38.png'),
                                loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 39.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 40.png'),
                                loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 41.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 42.png'),
                                loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 43.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 44.png'),
                                loadtransimg('UnitAnimations/ArcherSkeleton/Death/Archer Skeleton 45.png')]
        self.moves = [moves.ArcherAttack(1800, 960, 100, 100, (255, 255, 0))]

    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]


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
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png'), loadtransimg('UnitAnimations/SpearSkeleton/Idle/spear skeleton13.png')]
        self.moves = [moves.SpearAttack(1800, 960, 100, 100, (0, 255, 255))]


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
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png'),
                               loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png'), loadtransimg('UnitAnimations/MageSkeleton/Idle/Mage Skeleton-export13.png')]
        self.death_animation = [loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export32.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export33.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export34.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export35.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export36.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export37.png'),
                                loadtransimg('UnitAnimations/MageSkeleton/Death/Mage Skeleton-export38.png')]
        self.moves = [moves.MageAttack(1800, 960, 100, 100, (255, 0, 255))]
        
    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]


class Boss(Unit):
    def __init__(self, attack, hitpoints, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, speed, stillframe)
        self.xpos = stillframe.get_width() / 2
        self.idle_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss1.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss2.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss3.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss4.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss5.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss6.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss7.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss8.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss9.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss10.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss11.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss12.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss13.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Idle/Skeleton Boss14.png')]
        self.death_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss35.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss36.png'),
                                loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss37.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss38.png'),
                                loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss39.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss40.png'),
                                loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss41.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Death/Skeleton Boss42.png')]
        self.moves = [moves.BossAttack(1800, 960, 100, 100, (255, 0, 0))]

    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]
