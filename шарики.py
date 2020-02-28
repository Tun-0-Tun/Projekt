import pygame

size = [800, 800]
screen = pygame.display.set_mode(size)
v = 20  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()
running = True
fl = False
sp = []


class shar:
    def __init__(self, screen1, col, x, y, r):
        self.x = x
        self.y = y
        self.f = 1

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 20)

    def move(self):
        size = [800, 800]
        if self.y <= 20:
            self.f = 2

        if self.y >= size[1] - 20:
            self.f = 4

        if self.x <= 20:
            self.f = 1

        if self.x >= size[0] - 20 and self.f == 2:
            self.f = 3

        if self.x >= size[0] - 20 and self.f == 1:
            self.f = 4


        v = 100  # пикселей в секунду
        fps = 60
        if self.f == 1:
            self.x += v / fps
            self.y -= v / fps
        elif self.f == 2:
            self.x += v / fps
            self.y += v / fps
        elif self.f == 3:
            self.x -= v / fps
            self.y += v / fps
        elif self.f == 4:
            self.x -= v / fps
            self.y -= v / fps


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            sp.append(shar(screen, (255, 0, 0), int(x), int(y), 20))
            fl = True
    if fl:
        for i in range(len(sp)):
            k = sp[i]
            k.draw()
            k.move()

    clock.tick(fps)
    pygame.display.flip()
