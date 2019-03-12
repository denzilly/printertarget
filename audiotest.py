import pygame
import time

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


hitsound = pygame.mixer.Sound('blast.wav')
winsound = pygame.mixer.Sound('russiaogg.ogg')

time.sleep(0.5)

hitsound.play()