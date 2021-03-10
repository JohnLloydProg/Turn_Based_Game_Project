import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

def loadtransimg(imgname):
    return pygame.image.load(imgname).convert_alpha()

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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))
        self.current_health = 200
        self.target_health = 500
        self.max_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health


    def update(self):
        self.basic_health()

    def basic_health(self):


        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.target_health / self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.health_bar_length, 25), 4)



player = pygame.sprite.GroupSingle(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.sprite.get_health(50)
            if event.key == pygame.K_DOWN:
                player.sprite.get_damage(50)



    screen.fill((30, 30, 30))
    player.draw(screen)
    player.update()
    pygame.display.update()
    clock.tick(60)