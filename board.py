import pygame


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

    def get_clicked(self, pos):
        cell_x = pos[0] // self.cell_size
        cell_y = pos[1] // self.cell_size
        if 0 <= cell_x <= self.width and 0 <= cell_y <= self.height:
            return (cell_y + 1, cell_x + 1)
        else:
            print('None')
