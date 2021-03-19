import pygame
import moves


def loadtransimg(imgname):
    return pygame.image.load(imgname).convert_alpha()


tickspeed = 16


class Unit:
    def __init__(self, attack, hitpoints, armor, speed, stillframe):
        self.attack = attack
        self.base_attack = attack
        self.hitpoints = hitpoints
        self.full_health = hitpoints
        self.armor = armor
        self.base_armor = armor
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
        self.xpos = 0
        self.x = 0
        self.y = 0
        self.stunned = False
        self.turns = 0

    def hud(self, attackbar, coordinates):
        if attackbar > 100:
            attackbar = 100
        if self.hitpoints < 0:
            self.hitpoints = 0
        healt_bar_image = self.health_bar_images[int((self.hitpoints/self.full_health)*100//5)]
        attack_bar_image = self.attack_bar_images[int(attackbar//5)]
        return [(healt_bar_image, coordinates), (attack_bar_image, (coordinates[0], coordinates[1]+32))]

    def idle(self):
        if self.state == "idle":
            if self.animation_counter == len(self.idle_animation)*tickspeed:
                self.animation_counter = 0
            self.stillframe = self.idle_animation[self.animation_counter//tickspeed]
        self.animation_counter += 1

    def is_inside(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x+self.xpos >= mouse_x >= self.x and self.y+self.ypos >= mouse_y >= self.y:
            return True


class Archer(Unit):
    def __init__(self, attack, hitpoints, armor, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, armor, speed, stillframe)
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
        self.attack_animation = [loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 14.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 15.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 16.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 17.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 18.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 19.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 20.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 21.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 22.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 23.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 24.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 25.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 26.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 27.png'),
                                 loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 28.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Attack/Archer Skeleton 29.png')]
        self.hit_animation = [loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 31.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 32.png'),
                              loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 33.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 34.png'),
                              loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 35.png'), loadtransimg('UnitAnimations/ArcherSkeleton/Hit/Archer Skeleton 36.png')]
        self.moves = [moves.ArcherAttack(1800, 960, loadtransimg('Unit move Cards/Archer-Basicmove.png'))]
        self.attack_move = self.moves[0]

    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]

    def attacked(self, enemy, speed):
        if self.state == "attacking":
            finished = False
            if self.animation_counter < (len(self.attack_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.attack_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.attack_animation)-1)*speed:
                finished = True
                if enemy.state != "hit":
                    enemy.animation_counter = 0
                    enemy.state = "hit"
            return finished

    def hit(self, speed):
        if self.state == "hit":
            finished = False
            if self.animation_counter < (len(self.hit_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.hit_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.hit_animation)-1)*speed:
                finished = True
            return finished


class Spear(Unit):
    def __init__(self, attack, hitpoints, armor, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, armor, speed, stillframe)
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
        self.death_animation = [loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton28.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton29.png'),
                                loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton30.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton31.png'),
                                loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton32.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton33.png'),
                                loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton34.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton35.png'),
                                loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton36.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton37.png'),
                                loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton38.png'), loadtransimg('UnitAnimations/SpearSkeleton/Death/spear skeleton39.png')]
        self.hit_animation = [loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton21.png'), loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton22.png'),
                              loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton23.png'), loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton24.png'),
                              loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton25.png'), loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton26.png'),
                              loadtransimg('UnitAnimations/SpearSkeleton/Hit/spear skeleton27.png')]
        self.attack_animation = [loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton15.png'), loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton16.png'),
                                 loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton17.png'), loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton18.png'),
                                 loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton19.png'), loadtransimg('UnitAnimations/SpearSkeleton/Attack/spear skeleton20.png')]
        self.move_animation = [loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton40.png'), loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton41.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton42.png'), loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton43.png'),
                               loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton44.png'), loadtransimg('UnitAnimations/SpearSkeleton/Move/spear skeleton45.png')]
        self.moves = [moves.SpearAttack(1800, 960, loadtransimg('Unit move Cards/Spear-Basicmove.png')), moves.SpearBuff(1680, 960, loadtransimg('Unit move Cards/Spear-Secondmove.png'))]
        self.attack_move = self.moves[0]

    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]

    def attacked(self, enemy, speed):
        if self.state == "attacking":
            finished = False
            if self.move(enemy, speed):
                if self.animation_counter < (len(self.attack_animation)-1)*speed:
                    self.animation_counter += 1
                elif self.animation_counter > (len(self.attack_animation)-1)*speed:
                    self.animation_counter = 0
                self.stillframe = self.attack_animation[self.animation_counter//speed]
                if self.animation_counter == (len(self.attack_animation)-1)*speed:
                    finished = True
                    if enemy.state != "hit":
                        enemy.animation_counter = 0
                        enemy.state = "hit"
                return finished

    def move(self, enemy, speed):
        finished = False
        if (self.x, self.y) != (enemy.x, enemy.y):
            if self.animation_counter == (len(self.move_animation) - 1) * speed:
                self.animation_counter = 0
            self.stillframe = self.move_animation[self.animation_counter // speed]
            self.animation_counter += 1
            if self.x < enemy.x:
                if speed > 10:
                    self.x += 1
                else:
                    self.x += 5
            elif self.x > enemy.x:
                if speed > 10:
                    self.x -= 1
                else:
                    self.x -= 5
            else:
                if self.y < enemy.y:
                    self.y += 1
                elif self.y > enemy.y:
                    self.y -= 1
        else:
            finished = True
        return finished

    def hit(self, speed):
        if self.state == "hit":
            finished = False
            if self.animation_counter < (len(self.hit_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.hit_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.hit_animation)-1)*speed:
                finished = True
            return finished


class Mage(Unit):
    def __init__(self, attack, hitpoints, armor, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, armor, speed, stillframe)
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
        self.attack_animation = [loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export14.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export15.png'),
                                 loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export16.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export17.png'),
                                 loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export18.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export19.png'),
                                 loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export20.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export21.png'),
                                 loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export22.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export23.png'),
                                 loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export24.png'), loadtransimg('UnitAnimations/MageSkeleton/Attack/Mage Skeleton-export25.png')]
        self.hit_animation = [loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export26.png'), loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export27.png'),
                              loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export28.png'), loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export29.png'),
                              loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export30.png'), loadtransimg('UnitAnimations/MageSkeleton/Hit/Mage Skeleton-export31.png')]
        self.moves = [moves.MageAttack(1800, 960, loadtransimg('Unit move Cards/Mage-Basicmove.png')), moves.MageBuff(1680, 960, loadtransimg('Unit move Cards/Mage-Healmove.png'))]
        self.attack_move = self.moves[0]
        
    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]

    def attacked(self, enemy, speed):
        if self.state == "attacking":
            finished = False
            if self.animation_counter < (len(self.attack_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.attack_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.attack_animation)-1)*speed:
                finished = True
                if enemy.state != "hit":
                    enemy.animation_counter = 0
                    enemy.state = "hit"
            return finished

    def hit(self, speed):
        if self.state == "hit":
            finished = False
            if self.animation_counter < (len(self.hit_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.hit_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.hit_animation)-1)*speed:
                finished = True
            return finished


class Boss(Unit):
    def __init__(self, attack, hitpoints, armor, speed, stillframe):
        Unit.__init__(self, attack, hitpoints, armor, speed, stillframe)
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
        self.attack_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss21.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss22.png'),
                                 loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss23.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss24.png'),
                                 loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss25.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss26.png'),
                                 loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss27.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Attack/Skeleton Boss28.png')]
        self.hit_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss29.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss30.png'),
                              loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss31.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss32.png'),
                              loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss33.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Hit/Skeleton Boss34.png')]
        self.move_animation = [loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss15.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss16.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss17.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss18.png'),
                               loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss19.png'), loadtransimg('UnitAnimations/EnchantedSkeleton/Move/Skeleton Boss20.png')]
        self.moves = [moves.BossAttack(1800, 960, loadtransimg('Unit move Cards/EnchSkel-BasicMove.png')), moves.BossBuff(1680, 960,loadtransimg('Unit move Cards/EnchSkel-Defmove.png'))]
        self.attack_move = self.moves[0]

    def dead(self):
        if self.state == "dead":
            if self.animation_counter < (len(self.death_animation)-1)*25:
                self.animation_counter += 1
            self.stillframe = self.death_animation[self.animation_counter//25]

    def attacked(self, enemy, speed):
        if self.state == "attacking":
            if self.move(enemy, speed):
                finished = False
                if self.animation_counter < (len(self.attack_animation)-1)*speed:
                    self.animation_counter += 1
                elif self.animation_counter > (len(self.attack_animation)-1)*speed:
                    self.animation_counter = 0
                self.stillframe = self.attack_animation[self.animation_counter//speed]
                if self.animation_counter == (len(self.attack_animation)-1)*speed:
                    finished = True
                    if enemy.state != "hit":
                        enemy.animation_counter = 0
                        enemy.state = "hit"
                return finished

    def move(self, enemy, speed):
        finished = False
        if (self.x, self.y) != (enemy.x, enemy.y):
            if self.animation_counter == (len(self.move_animation)-1)*speed:
                self.animation_counter = 0
            self.stillframe = self.move_animation[self.animation_counter//speed]
            self.animation_counter += 1
            if self.x < enemy.x:
                if speed > 10:
                    self.x += 1
                else:
                    self.x += 5
            elif self.x > enemy.x:
                if speed > 10:
                    self.x -= 1
                else:
                    self.x -= 5
            else:
                if self.y < enemy.y:
                    self.y += 5
                elif self.y > enemy.y:
                    self.y -= 5
        else:
            finished = True
        return finished

    def hit(self, speed):
        if self.state == "hit":
            finished = False
            if self.animation_counter < (len(self.hit_animation)-1)*speed:
                self.animation_counter += 1
            self.stillframe = self.hit_animation[self.animation_counter//speed]
            if self.animation_counter == (len(self.hit_animation)-1)*speed:
                finished = True
            return finished
