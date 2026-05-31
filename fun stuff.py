import pygame
import pygetwindow
import random
pygame.init()
window = pygetwindow.getActiveWindow()
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
run = True
prop = pygame.Rect((300, 250, 50, 50))
font = pygame.font.Font(None, 48)
text_surface = font.render("hit me!", True, (255, 255, 255))
rumble = font.render("*rumble*", True, (255,100,100))
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            prop.centerx, prop.centery = pygame.mouse.get_pos()
        elif event.type == pygame.WINDOWENTER:
            window = pygetwindow.getActiveWindow()
            for i in range(3):
                screen.blit(rumble, (random.randint(0,800), random.randint(0,600)))
            screen.blit(text_surface, (300, 300))
            pygame.display.update()
            for i in range(1000):
                window.moveRel(random.randint(-1, 1), random.randint(-1, 1))
    screen.blit(text_surface, (300, 300))
    pygame.display.update()