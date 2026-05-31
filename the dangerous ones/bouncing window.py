import pygame
import pymunk
import pymunk.pygame_util
import math
import pygetwindow
import os

pygame.init()

WIDTH, HEIGHT = 1919, 1079
window = pygame.display.set_mode((WIDTH, HEIGHT))

#set background:

def draw(space, window, draw_options, line):
    window.fill("white")
    if line:
        pygame.draw.line(window, "black", line[0], line[1], 3)
    space.debug_draw(draw_options)
    pygame.display.update()

#calculate the distance between 2 points

def calc_distance(p1, p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

#calculate an angle

def calc_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

#create sim boundaries

def create_boundaries(space, width, height):
    
    #create rectangle measurments

    rects = [
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width - 10, height/2), (20, height)]
    ]

    #define rectangle bodies
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

    #self explanatory
def create_ball(space, radius, mass, pos, type):
    #define ball body
    if type == "Dynamic":
        body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    else:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
    #place ball at passed position
    body.position = pos
    #create circle visual body
    shape = pymunk.Circle(body, radius)
    #hmmmmmm, i wonder what this does
    shape.mass = mass
    #define elasticity, friction, and color respectively
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.color = (255, 100, 100, 100)
    #add ball to simulation
    space.add(body, shape)
    return shape

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    space = pymunk.Space()
    space.gravity = (0, 981)
    large_ball = create_ball(space, 60, 10, (500, 400), "Dynamic")
    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    pressed_pos = None
    ball = None
    while run:
        line = None
        if ball and pressed_pos:
            line = [pressed_pos, pygame.mouse.get_pos()]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_ball(space, 30, 10, pressed_pos, "Static")
                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC
                    angle = calc_angle(*line)
                    force = calc_distance(*line) * 50
                    fx = math.cos(angle) * force
                    fy = math.sin(angle) * force
                    ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                    pressed_pos = None
                else:
                    space.remove(ball, ball.body)
                    ball = None
        try:
            Pywindow: pygetwindow.Win32Window = pygetwindow.getWindowsWithTitle("pygame window")[0]
            SysWindow = pygetwindow.getWindowsWithTitle('Untitled - Notepad')
            SysWindow1 = SysWindow[0]
            SysWindow1.center = ball.body.position
            SysWindow2 = SysWindow[1]
            SysWindow2.center = large_ball.body.position
            if Pywindow.isActive == False:
                Pywindow.activate()
        except:
            pass
        draw(space, window, draw_options, line)
        space.step(dt)
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)