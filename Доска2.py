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
        self.k = 1

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 1:
                    if self.k % 2 != 0:
                        pygame.draw.line(screen, (0, 255, 0),
                                         ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                          (self.cell_size, self.cell_size)), 1)
                        pygame.draw.line(screen, (255, 0, 0),
                                         ((self.left + x * self.cell_size + self.cell_size,
                                           self.top + y * self.cell_size + self.cell_size),
                                          (self.left + x * self.cell_size, self.top + y * self.cell_size)), 1)
                        self.k += 1
                    elif self.k % 2 == 0:

                        pygame.draw.circle(screen, (255, 0, 0),
                                           ((int(self.left + x * self.cell_size + self.cell_size * 0.5),
                                             int(self.top + y * self.cell_size + self.cell_size * 0.5))),
                                           int(self.cell_size * 0.5 - 4), 2)
                        self.k += 1

                pygame.draw.rect(screen, (255, 255, 255),
                                 ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                  (self.cell_size, self.cell_size)), 2)

    def get_clicked(self, pos):
        cell_x = pos[0] // self.cell_size
        cell_y = pos[1] // self.cell_size
        if 0 <= cell_x <= self.width and 0 <= cell_y <= self.height:
            self.board[cell_y][cell_x] = (self.board[cell_y][cell_x] + 1)


board = Board(5, 6)
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
