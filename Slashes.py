import pygame, sys
from random import randint
pygame.init()
warn = pygame.mixer.Sound("warning.wav")
slash = pygame.mixer.Sound("shocker sound.wav")
pygame.mixer.music.load('maniacsrevenge.mp3')
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Slasher")
clock = pygame.time.Clock()

class Dust:
    def __init__(self):
        self.sans = pygame.image.load('dust_ref.png')
        self.rect = self.sans.get_rect(center=(400, 225))
    def update(self):
        self.rect.centerx = 400
        self.rect.x += randint(-5, 5)

sans = Dust()
pygame.mixer.music.play(-1)
while True:
    screen.fill(pygame.Color("black"))
    sans.update()
    screen.blit(sans.sans, sans.rect)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pygame.mixer.Sound.play(warn)
            pygame.time.delay(500)
            screen.fill(pygame.Color('purple'))
            pygame.mixer.Sound.play(slash)
    pygame.display.update()
    clock.tick(10)
