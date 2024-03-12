import pygame
import random
SX = 600
SY = 600

pygame.init()
screen = pygame.display.set_mode((SX, SY))
running = True

NumStar = 100 
speed = 0.09  
stars = []  



def new_star():
    star = [random.randint(0, SX) - SX // 2, random.randint(0, SY) - SY // 2, 256, 0]
    return star


for i in range(0, NumStar):  
    stars.append(new_star())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 
    x = y = 0
    for i in range(0, NumStar):  
        s = stars[i]  
        x = s[0] * 256 / s[2]
        y = s[1] * 256 / s[2]
        s[2] -= speed  #

       
        if s[2] <= 0 or x <= -SX // 2 or x >= SX // 2 or y <= -SY // 2 or y >= SY // 2:
            s = new_star()

        if s[3] < 256: 
            s[3] += 0.15

        if s[3] >= 256:  
            s[3] = 255

        stars[i] = s 

       
        x = round(s[0] * 256 / s[2]) + SX // 2
        y = round(s[1] * 256 / s[2]) + SY // 2
        pygame.draw.circle(screen, (s[3], s[3], s[3]), (x, y), 3)

    pygame.display.flip()

pygame.quit()
