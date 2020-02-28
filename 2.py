from random import randint
import pygame

pygame.init()
x, y = 15, 15
rast = 20
mines = 45
screen = pygame.display.set_mode([(x + 2) * rast, (y + 2) * rast])
pole = [False for i in range(x * y)]
while pole.count(True) < mines:
    pole[randint(0, x * y - 1)] = True
for i in range(x * y):
    pygame.draw.rect(screen, (255, 0, 0) if pole[i] else (0, 0, 0),
                     [(i % x + 1) * rast, (i // x + 1) * rast, rast, rast])
    pygame.draw.rect(screen, (255, 255, 255),
                     [(i % x + 1) * rast, (i // x + 1) * rast, rast, rast], 1)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            X, Y = event.pos[0] // rast - 1, event.pos[1] // rast - 1
            if pole[X + Y * x]:
                done = True
            else:
                res = 0
                for xx in [-1, 0, 1]:
                    for yy in [-1, 0, 1]:
                        if 0 ** abs(xx) + 0 ** abs(
                                yy) != 2 and X + xx > 0 and Y + yy > 0:
                            if X + xx + (Y + yy) * x in range(x * y) and \
                                    pole[X + xx + (Y + yy) * x]:
                                res += 1
                text = pygame.font.Font(None, rast).render(str(res), 0,
                                                           (0, 255, 0))
                xx, yy = (X + 1.5) * rast - text.get_width() // 2, \
                         (Y + 1.5) * rast - text.get_height() // 2
                screen.blit(text, (xx, yy))

    pygame.display.flip()
pygame.quit()
