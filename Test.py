import pygame.display
import pygame.image
display = pygame.display.set_mode((800, 600))
img = pygame.image.load('images/button1.png')
r = img.get_rect()
# the interesting line
r.center = display.get_rect().center
display.blit(img, r)
pygame.display.flip()
input()