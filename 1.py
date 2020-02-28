import pygame

pygame.init()
x, y = 36, 36
rast = 20
screen = pygame.display.set_mode([(x + 2) * rast, (y + 2) * rast])
pole = [False for i in range(x * y)]
clock = pygame.time.Clock()
fps = 10
moving = False
done = False
while not (done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if moving:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 5 and fps > 1: fps -= 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 4: fps += 1
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            X, Y = event.pos[0] - rast, event.pos[1] - rast
            if X in range(x * rast) and Y in range(y * rast):
                pole[X // rast + (Y // rast) * x] = not (
                    pole[X // rast + (Y // rast) * x])
        if (event.type == pygame.KEYUP and event.key == 32) or (
                event.type == pygame.MOUSEBUTTONUP and event.button == 3): moving = not moving

    if moving:
        pole1 = list(pole)
        for i in range(x * y):
            X, Y, data = i % x, i // x, []
            for xx in [-1, 0, 1]:
                for yy in [-1, 0, 1]:
                    if (0 ** abs(xx) + 0 ** abs(yy) != 2 and X + xx in range(
                            x) and Y + yy in range(y)):
                        data.append(pole[X + xx + (Y + yy) * x])
            if pole[i] and data.count(True) not in [2, 3]:
                pole1[i] = False
            elif data.count(True) == 3:
                pole1[i] = True
        pole = list(pole1)

    for i in range(x * y):
        pygame.draw.rect(screen, (0, 255, 0) if (pole[i]) else (0, 0, 0),
                         [(i % x + 1) * rast, (i // x + 1) * rast, rast, rast])
        pygame.draw.rect(screen, (255, 255, 0),
                         [(i % x + 1) * rast, (i // x + 1) * rast, rast, rast],
                         1)
    if moving:
        clock.tick(fps)
    else:
        clock.tick(60)
    pygame.display.flip()
pygame.quit()
