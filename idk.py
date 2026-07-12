import pygame
import pygetwindow
# velocity
vel = 1
velx = 0

#define pygame screen/display
screen = pygame.display.set_mode((1000, 800))

#game clock
clck = pygame.time.Clock()

#define rectangle shape and position
rect = (500, 150, 15, 15)

#draw rectangle
idk = pygame.draw.rect(screen, (150, 150, 150), rect)

#main game loop
while(True):
    #gravity and upwards velocity
    velx = velx*0.99
    if velx >= 120:
        velx = 119
    if vel >= 120:
        vel = 119
    if vel >= -0 and idk.bottomleft[1] <= screen.get_height():
        vel = vel+0.8
    elif idk.bottomleft[1] <= screen.get_height():
        vel = vel+0.8
    rect = (rect[0]+velx, rect[1]+vel, rect[2], rect[3])
    print(rect)
    screen.fill((25,0,25))
    idk = pygame.draw.rect(screen, (150, 150, 150), rect)
    if idk.bottomleft[1] >= screen.get_height() and vel*-0.9 <= -0:
        vel = vel*-0.8
        vel = vel+-1
    if idk.topleft[1] <= 0:
        vel = vel*-0.8
        vel = vel+1
    if idk.bottomright[0] >= screen.get_width():
        velx = velx*-0.8
        velx = velx+-1
    if idk.bottomleft[0] <= 0:
        velx = velx*-0.8
        velx = velx+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                velx = velx+10
            if event.key == pygame.K_w:
                vel = vel+-20
            if event.key == pygame.K_a:
                velx = velx+-10
            if event.key == pygame.K_SPACE:
                vel = vel*0.1
                velx = velx*0.1
    pygame.display.update()
    clck.tick(60)