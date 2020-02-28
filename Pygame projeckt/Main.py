import pygame
import sys
import os
import os.path
import pygame.font

tile_images = {'wall': pygame.image.load('data/stena.png'),
               'empty': pygame.image.load('data/pol.png'),
               'krai': pygame.image.load('data/krstena.png')}
player_image = pygame.image.load('data/pers.png')

tile_width = tile_height = 50

player = None
pygame.init()
data = {
    'box': pygame.image.load('data/stena.png'),
    'fon': pygame.image.load(os.path.join('data', 'fon.jpg')),
    'grass': pygame.image.load(os.path.join('data', 'pol.png')),
    'mar': pygame.image.load(os.path.join('data', 'pers.png'))
}


def starter(size=(700, 700)):
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(data['fon'].convert(), size)
    screen.blit(fon, (0, 0))
    zv1 = (100, 100, 100)
    zv2 = (120, 120, 120)
    intro_text = (('Лабиринт', (300, 25), 74, (0, 0, 0)),
                  ('Правила игры:', (150, 160), 50, (25, 25, 20)),
                  ('Найти выход', (150, 250), 50, (200, 200, 200)),
                  ('И', (150, 455), 120, zv2),
                  ('Г', (200, 455), 120, zv2),
                  ('Р', (250, 455), 120, zv2),
                  ('А', (300, 455), 120, zv1),
                  ('Т', (350, 455), 120, zv1),
                  ('Ь', (400, 455), 120, zv1))
    for line in intro_text:
        rendered = pygame.font.Font(None, line[2]).render(line[0], 1, line[3])
        rect = rendered.get_rect()
        screen.blit(rendered, (line[1][0] - rendered.get_rect()[2] / 2,
                               line[1][1] - rendered.get_rect()[3] / 2))
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): return (False)
            if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and
                    event.pos[0] in range(114, 451) and event.pos[1] in range(
                        405, 500)): return (True)
        pygame.display.flip()


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину    
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')    
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15,
                                               tile_height * pos_y + 5)
        self.pos_x = pos_x
        self.pos_y = pos_y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            print(len(level))
            if level[y][x] == '@':
                Tile('wall', x, y)
                new_player = Player(x, y)
                print(x)
                print(y)
    return new_player, x, y


def generate(level, coord):
    y, x = coord
    if level[y][x] == '.':
        Tile('empty', x, y)
    elif level[y][x] == '#':
        Tile('wall', x, y)
    elif level[y][x] == '*':
        Tile('krai', x, y)

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - level_x * 50 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - level_y * 50 // 2)


starter()
nMap = 'map.txt'
camera = Camera()
running = False
if os.path.exists(os.path.join('data', nMap)):
    player, level_x, level_y = generate_level(load_level(nMap))
    pygame.init()
    screen = pygame.display.set_mode([level_x * 50, level_y * 50])
    running = True
else:
    print('Файла не существует')

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 50
            if event.key == pygame.K_UP:
                generate(load_level(nMap), (player.pos_y - 1, 
                                            player.pos_x))
                player.rect.y -= 50
            if event.key == pygame.K_DOWN:
                player.rect.y += 50

            elif event.key == pygame.K_RIGHT:
                player.rect.x += 50

    camera.update(player)
    # обновляем положение всех спрайтов
    for sprite in all_sprites:
        camera.apply(sprite)

    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
