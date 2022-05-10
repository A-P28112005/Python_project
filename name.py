import pygame, random, sys
from pygame.locals import * 

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
        return True
    else:
        return False

def die(screen, score):
    f=pygame.font.SysFont('times bold', 30);t=f.render('Your score was: '+str(score), True, (255, 255, 255));screen.blit(t, (10, 270));pygame.display.update();pygame.time.wait(2000);sys.exit(0)
xs = [290, 290, 290, 290, 290];ys = [290, 270, 250, 230, 210];dirs = 0; score = 0;
applepos = (random.randint(0, 590), random.randint(0, 590));
pygame.init();

s=pygame.display.set_mode((600, 600));
pygame.display.set_caption('Snake Game');
appleimage = pygame.Surface((16, 16));
appleimage.fill((127, 255, 0));
img = pygame.Surface((20, 20));
img.fill((255, 0, 0));
f = pygame.font.SysFont('times bold', 30);
clock = pygame.time.Clock()






