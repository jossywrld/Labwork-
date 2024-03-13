import pygame
import random

SX = SY = 600

pygame.init()

screen = pygame.display.set_mode((SX, SY))
running = True

Num_of_stars = 100
speed = 0.09
stars = []
def new_star():
    x = random.randint(0, SX) - SX //2
    y = random.randint(0, SY) - SY //2
    z = 256
    color = 0 
    star = [x, y, z, color]
    return star
def move_and_check(star: list):
    x = (star[0] * 256) / star[2]
    y =  (star[1] * 256) / star[2]
    
    star[2] -= speed

    if star[2] <=0 or x <= -SX //2 or x >= SX //2 or y <= -SY //2 or y >= SY //2:
        star = new_star()

    if star[3] < 150:
        star[3] += 0.15

    if star[3] >= 150:
        star[3] = 255

    return star

def draw_star(star: list):
    x = (star[0] * 256) / star[2] + SX // 2
    y = (star[1] * 256) / star[2] + SY // 2
    pygame.draw.circle(screen, (150, star[3], star[3]), (x, y), 3)


for i in range(0, Num_of_stars):
    stars.append(new_star())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(0, Num_of_stars):
        s = stars[i]

        s = move_and_check(s)

        stars[i] = s

        draw_star(s)
        

    pygame.display.flip()

pygame.quit()
