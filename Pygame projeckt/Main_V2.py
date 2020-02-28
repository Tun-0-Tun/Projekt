import pygame
import sys
import os
import os.path
import pygame.font
import time

tile_images = {'wall': pygame.image.load('data/stena.png'),
               'empty': pygame.image.load('data/pol.png'),
               'krai': pygame.image.load('data/krstena.png'),
               'ded': pygame.image.load('data/ded.png'),
               'Alina': pygame.image.load('data/Alina.png'),
               'pauk': pygame.image.load('data/pauk1.png'),
               'vih': pygame.image.load('data/vih.png'),
               'key': pygame.image.load('data/kluch.png'),
               'Lovushka': pygame.image.load('data/lowushka.png')}
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


def starter(size=(1500, 900)):
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
all_sprites2 = pygame.sprite.Group()
tiles_group2 = pygame.sprite.Group()
player_group2 = pygame.sprite.Group()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, n):
        if n == 1:
            super().__init__(player_group, all_sprites)
            self.image = player_image
        elif n == 2:
            super().__init__(player_group2, all_sprites2)
            self.image = player_image

        self.rect = self.image.get_rect().move(tile_width * pos_x + 15,
                                                   tile_height * pos_y + 5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.HP = 3


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Tile2(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group2, all_sprites2)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


def generate_level(level):
    new_player, new_player2, x, y = None, None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            print(len(level))
            if level[y][x] == '@':
                Tile('wall', x, y)
                new_player = Player(x, y, 1)
            if level[y][x] == '%':
                Tile2('wall', x, y)
                new_player2 = Player(x, y, 2)
    return new_player, new_player2, x, y


def generate(level, coord, nhod):
    y, x = coord
    if nhod % 2 != 0:
        if level[y][x] == '.':
            Tile('empty', x, y)
        elif level[y][x] == '#':
            Tile('wall', x, y)
        elif level[y][x] == '*':
            Tile('krai', x, y)
        elif level[y][x] == 'D':
            Tile('wall', x, y)
            Tile('ded', x, y)
        elif level[y][x] == 'A':
            Tile('wall', x, y)
            Tile('Alina', x, y)
        elif level[y][x] == '?':
            Tile('vih', x, y)
        elif level[y][x] == 'S':
            Tile('wall', x, y)
            Tile('pauk', x, y)
        elif level[y][x] == 'K':
            Tile('wall', x, y)
            Tile('key', x, y)
        elif level[y][x] == 'L':
            Tile('Lovushka', x, y)
        elif level[y][x] == 'J':
            Tile('wall', x, y)
        elif level[y][x] == '1':
            Tile('wall', x, y)
    else:
        if level[y][x] == '.':
            Tile2('empty', x, y)
        elif level[y][x] == '#':
            Tile2('wall', x, y)
        elif level[y][x] == '*':
            Tile2('krai', x, y)
        elif level[y][x] == 'D':
            Tile2('wall', x, y)
            Tile2('ded', x, y)
        elif level[y][x] == 'K':
            Tile2('wall', x, y)
            Tile2('key', x, y)
        elif level[y][x] == '?':
            Tile2('wih', x, y)
        elif level[y][x] == 'A':
            Tile2('vall', x, y)
            Tile2('Alina', x, y)
        elif level[y][x] == 'S':
            Tile2('wall', x, y)
            Tile2('pauk', x, y)
        elif level[y][x] == 'L':
            Tile2('Lovushka', x, y)
        elif level[y][x] == 'J':
            Tile2('wall', x, y)
        elif level[y][x] == '1':
            Tile2('wall', x, y)


'''class Camera:
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
        self.dy = -(target.rect.y + target.rect.h // 2 - level_y * 50 // 2)'''

starter()
Nhod = 1
nMap = 'map.txt'
'''camera = Camera()'''
running = False
if os.path.exists(os.path.join('data', nMap)):
    player, player2, level_x, level_y = generate_level(load_level(nMap))
    pygame.init()
    screen = pygame.display.set_mode([(level_x + 1) * 50 + 250, (level_y +
                                                                 1) * 50])
    screen2 = pygame.display.set_mode([(level_x + 1) * 50 + 250, (level_y +
                                                                  1) * 50])
    running = True
else:
    print('Файла не существует')
map1 = load_level(nMap)
print(map1)
yellow = (255, 255, 0)
blue = (0, 0, 255)
fontObj = pygame.font.Font(None, 20)
text_y = 20
text = (('Вы оказались в мерзком подземелье, ', ((level_x + 1) * 50 + 50,
                                                 text_y), 20, (255, 255, 0)),
        ('время сделать выбор. Умереть или искать выход?', ((level_x + 1) *
                                                            50, text_y + 50),
         20, (255, 255, 0)))
text_y += 100


def DedTrigger():
    text = (('Три сотни лет я сидел здесь, три сотни лет считал свои мысли и ',
             ((level_x + 1) * 50 + 50, 100), 15, (255, 255, 0)),
            ('собирал крупицы чужой памяти. Три сотни лет я ждал человека,',
             ((level_x + 1) * 50 + 50, 120), 15, (255, 255, 0)),
            ('которому суждено увидеть и пережить многое в своих '
             'странствиях.. ', ((level_x + 1) * 50 + 50, 140), 15, (255, 255,
                                                                    0)),
            ('И так и не дождался...', ((level_x + 1) * 50 + 50, 160), 15,
             (255, 255, 0)))
    return text


def AlinTrigger():
    text = (('Да, да, всё хорошо...',
             ((level_x + 1) * 50 + 100, 100), 15, (255, 255, 0)),
            ('Жаль, что мне плевать... Ведь я такая холодная...',
             ((level_x + 1) * 50 + 100, 120), 15, (255, 255, 0)),
            ('И тебе...', ((level_x + 1) * 50 + 100, 140), 15, (255, 255,
                                                                0)),
            ('Ой всё, ты не видел Артьомочку?', ((level_x + 1) * 50 + 100,
                                                 160),
             15,
             (255, 255, 0)))
    return text


def SpiderTrigger():
    text = (('Мурчит...',
             ((level_x + 1) * 50 + 50, 100), 15, (255, 255, 0)),
            ('*Грустно мурчит*',
             ((level_x + 1) * 50 + 50, 120), 15, (255, 255, 0)),
            ('*Мурчит по-паучи*', ((level_x + 1) * 50 + 50, 140), 15, (255,
                                                                       255,
                                                                       0)))
    return text


def LowushkaDeistv():
    print('asdasdasdasdasdas')
    if Nhod % 2 != 0:
        player.HP -= 1
        text = (
            ('Вы попадаете в ловушку', ((level_x + 1) * 50, text_y), 20,
             (255, 255, 0)),
            ('Теперь ваше колличество HP: ' + str(player.HP), ((level_x +
                                                                1) * 50,
                                                               text_y + 50),
             20, (255, 255, 0)))
    else:
        player2.HP -= 1
        text = (
            ('Вы попадаете в ловушку', ((level_x + 1) * 50, text_y), 20,(255, 255, 0)),
            ('Теперь ваше колличество HP: ' + str(player2.HP), ((level_x + 1)
                                                               * 50,text_y + 50),
             20, (255, 255, 0)))
    return text

        
        
    
    


fl = True

while running:
    screen.fill((0, 0, 0))
    if text_y > level_y:
        text_y = 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
        elif event.type == pygame.KEYDOWN:
            if fl:
                if event.key == pygame.K_LEFT:
                    fl = not fl
                    if Nhod % 2 != 0:
                        zone = load_level(nMap)[player.pos_y][player.pos_x - 1]
                        generate(load_level(nMap), (player.pos_y,
                                                    player.pos_x - 1), Nhod)
                        if zone == 'J':
                            player.pos_x -= 1
                            player.rect.x -= 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or \
                                zone == '@' or zone == '%' or zone == 'L':
                            player.pos_x -= 1
                            player.rect.x -= 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                text =  LowushkaDeistv()
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    else:
                        zone = load_level(nMap)[player2.pos_y][player2.pos_x - 1]
                        generate(load_level(nMap), (player2.pos_y,
                                                    player2.pos_x - 1), Nhod)
                        if zone == 'J':
                            player2.pos_x -= 1
                            player2.rect.x -= 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or zone == '@' or zone == '%' or zone == 'L':
                            player2.pos_x -= 1
                            player2.rect.x -= 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца',
                                     ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                text =  LowushkaDeistv()
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    
                if event.key == pygame.K_UP:
                    fl = not fl
                    if Nhod % 2 != 0:
                        zone = load_level(nMap)[player.pos_y - 1][player.pos_x]
                        generate(load_level(nMap), (player.pos_y - 1,
                                                    player.pos_x), Nhod)
                        if zone == 'J':
                            player.pos_y -= 1
                            player.rect.y -= 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or zone == '@' or zone == '%' or zone == 'L':
                            player.pos_y -= 1
                            player.rect.y -= 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                text =  LowushkaDeistv()
                        elif zone == 'D':
                            text = DedTrigger()
        
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    else:
                        zone = load_level(nMap)[player2.pos_y - 1][player2.pos_x]
                        generate(load_level(nMap), (player2.pos_y - 1,
                                                    player2.pos_x), Nhod)
                        if zone == 'J':
                            player2.pos_y -= 1
                            player2.rect.y -= 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or zone == '@' or zone == '%' or zone == 'L':
                            player2.pos_y -= 1
                            player2.rect.y -= 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца',
                                     ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                text =  LowushkaDeistv()
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    
                if event.key == pygame.K_DOWN:
                    fl = not fl
                    if Nhod % 2 != 0:
                        zone = load_level(nMap)[player.pos_y + 1][player.pos_x]
                        generate(load_level(nMap), (player.pos_y + 1,
                                                    player.pos_x), Nhod)
                        if zone == 'J':
                            player.pos_y += 1
                            player.rect.y += 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                            
                        
                        if zone == '#' or \
                                zone == '@' or zone == '%' or zone == 'L':
                            player.pos_y += 1
                            player.rect.y += 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                text = LowushkaDeistv()
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    else:
                        zone = load_level(nMap)[player2.pos_y + 1][player2.pos_x]
                        generate(load_level(nMap), (player2.pos_y + 1,
                                                    player2.pos_x), Nhod)
                        if zone == 'J':
                            player2.pos_y += 1
                            player2.rect.y += 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or zone == '@' or zone == '%' or zone == 'L':
                            player2.pos_y += 1
                            player2.rect.y += 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            if zone == 'L':
                                text = LowushkaDeistv()
                            text_y += 100
    
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
    
    
    
                elif event.key == pygame.K_RIGHT:
                    fl = not fl
                    if Nhod % 2 != 0:
                        zone = load_level(nMap)[player.pos_y][player.pos_x + 1]
                        generate(load_level(nMap), (player.pos_y,
                                                    player.pos_x + 1), Nhod)
                        if zone == 'J':
                            player.pos_x += 1
                            player.rect.x += 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or \
                                zone == '@' or zone == '%' or zone == 'L':
                            player.pos_x += 1
                            player.rect.x += 50
                            if zone == 'L':
                                text = LowushkaDeistv()
                            else:
                                text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                         (255, 255, 0)),
                                        ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                         20, (255, 255, 0)))
                        
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                    else:
                        zone = load_level(nMap)[player2.pos_y][player2.pos_x + 1]
                        generate(load_level(nMap), (player2.pos_y,
                                                    player2.pos_x + 1), Nhod)
                        if zone == 'J':
                            player2.pos_x += 1
                            player2.rect.x += 50
                            text = (
                            ('Лязг металла', ((level_x + 1) * 50, text_y), 20,
                             (255, 255, 0)),
                            ('Трупный запах бьёт вам в лицо', ((level_x + 
                                                                 1) * 50, text_y + 50),
                             20, (255, 255, 0)))
                        if zone == '#' or zone == '@' or zone == '%' or zone == 'L':
                            player2.pos_x += 1
                            player2.rect.x += 50
                            text = (('Тишина', ((level_x + 1) * 50, text_y), 20,
                                     (255, 255, 0)),
                                    ('Стук сердца', ((level_x + 1) * 50, text_y + 50),
                                     20, (255, 255, 0)))
                            text_y += 100
                            if zone == 'L':
                                LowushkaDeistv()
                                
    
                        elif zone == 'D':
                            text = DedTrigger()
    
                        elif zone == 'A':
                            text = AlinTrigger()
                        elif zone == 'S':
                            text = SpiderTrigger()
                
            elif event.key == pygame.K_SPACE:
                Nhod += 1
                fl = True
                
  
            
            
            

    '''camera.update(player)'''
    # обновляем положение всех спрайтов
    '''for sprite in all_sprites:
        camera.apply(sprite)'''
    if Nhod % 2 != 0:
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        for line in text:
            rendered = pygame.font.Font(None, line[2]).render(line[0], 1, line[3])
            rect = rendered.get_rect()
            screen.blit(rendered, (line[1][0] - rendered.get_rect()[2] / 2,
                                   line[1][1] - rendered.get_rect()[3] / 2))
        
    else:
        all_sprites2.draw(screen2)
        tiles_group2.draw(screen2)
        player_group2.draw(screen2)
        for line in text:
            rendered = pygame.font.Font(None, line[2]).render(line[0], 1, line[3])
            rect = rendered.get_rect()
            screen.blit(rendered, (line[1][0] - rendered.get_rect()[2] / 2,
                                   line[1][1] - rendered.get_rect()[3] / 2))

    pygame.display.flip()
