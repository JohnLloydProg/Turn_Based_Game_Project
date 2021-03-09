import pygame

from Spritesheet import Spritesheet


class SkeletonBoss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (240, 244)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.velocity = 0
        if self.LEFT_KEY:
            self.velocity = -2
        elif self.RIGHT_KEY:
            self.velocity = 2
        self.rect.x += self.velocity
        self.set_state()
        self.animate()

    def set_state(self):
        self.state = ' idle'
        if self.velocity > 0:
            self.state = 'moving right'
        elif self.velocity < 0:
            self.state = 'moving left'

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == ' idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]



    def load_frames(self):
        idle_frames_right = Spritesheet('Spritesheet/Idle Spritesheet.png')

        self.idle_frames_right = [idle_frames_right.parse_sprite("Skeleton Boss 0.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 1.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 2.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 3.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 4.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 5.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 6.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 7.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 8.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 9.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 10.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 11.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 12.png"),
                                  idle_frames_right.parse_sprite("Skeleton Boss 13.png")]

        moving_frames_right = Spritesheet('Spritesheet/Moving Spritesheet.png')

        self.moving_frames_right = [moving_frames_right.parse_sprite("Skeleton Boss 14.png"),
                                    moving_frames_right.parse_sprite("Skeleton Boss 15.png"),
                                    moving_frames_right.parse_sprite("Skeleton Boss 16.png"),
                                    moving_frames_right.parse_sprite("Skeleton Boss 17.png"),
                                    moving_frames_right.parse_sprite("Skeleton Boss 18.png"),
                                    moving_frames_right.parse_sprite("Skeleton Boss 19.png")]

        self.idle_frames_left = []
        for frames in self.idle_frames_left:
            self.idle_frames_left.append(pygame.transform.flip(frames, True, False))
        self.moving_frames_left = []
        for frames in self.moving_frames_right:
            self.moving_frames_left.append(pygame.transform.flip(frames, True, False))



