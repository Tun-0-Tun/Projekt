import pygame
from random import randint
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.sp = []
        self.sp = [[randint(1, 2)] * width for _ in range(height)]
        for i in range(len(self.sp)):
            for j in range(len(self.sp[0])):
                self.sp[i][j] = randint(1, 2)
        random.shuffle(self.sp)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] % 2 != 0:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)), 0)

                pygame.draw.rect(screen, (255, 255, 255),
                                 ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                  (self.cell_size, self.cell_size)), 2)

                if self.sp[y][x] % 2 == 0:
                    pygame.draw.rect(screen, (255, 0, 255),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)))

    def prov(self, pos):
        self.t = 0
        print(pos)
        if pos[0] == 0:
            if pos[1] == 0:
                print(self.sp[pos[0]][pos[1] + 1])
                if self.sp[pos[0]][pos[1] + 1] % 2 == 0:
                    self.t += 1
                if self.sp[pos[0] - 1][pos[1] - 1] % 2 == 0:
                    self.t += 1
                if self.sp[pos[0] - 1][pos[1]] % 2 == 0:
                    self.t += 1
            elif pos[1] == self.height:
                print(self.sp[pos[0]][pos[1] + 1])
                if self.sp[pos[0]][pos[1] + 1] % 2 == 0:
                    self.t += 1
                if self.sp[pos[0] + 1][pos[1] + 1] % 2 == 0:
                    self.t += 1
                if self.sp[pos[0] + 1][pos[1]] % 2 == 0:
                    self.t += 1
        elif pos[0] != 0 and pos[1] != 0:
            if self.sp[pos[0]][pos[1] + 1] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] + 1][pos[1] + 1] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] + 1][pos[1]] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] - 1][pos[1]] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] - 1][pos[1] + 1] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] - 1][pos[1] - 1] % 2 == 0:
                self.t += 1
            if self.sp[pos[0] + 1][pos[1] - 1] % 2 == 0:
                self.t += 1
            if self.sp[pos[0]][pos[1] - 1] % 2 == 0:
                self.t += 1
        return self.t

    def get_clicked(self, pos):
        cell_x = pos[0] // self.cell_size
        cell_y = pos[1] // self.cell_size
        print(self.sp)
        if 0 <= cell_x <= self.width and 0 <= cell_y <= self.height:
            if self.sp[cell_y][cell_x] % 2 != 0:
                m = self.prov((cell_y, cell_x))
                print(m)


board = Board(8, 8)
board.set_view(0, 0, 50)
running = True
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_clicked(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
