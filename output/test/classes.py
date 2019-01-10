import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((230, 230, 19))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
            self.collide_with_tiles()
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

    def collide_with_tiles(self, dx=0, dy=0):
        for tile in self.game.tiles:
             if self.rect.colliderect(tile.rect):
                print("Setting current map to testmap2")
                self.game.set_current_map(self.game.testmap2_map)
                self.game.unload_tiles()
                self.game.load_tiles(self.game.current_map)

class banana(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.banana_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class barrel(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.barrel_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class tile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites, game.tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.tile_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class tree(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.tree_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
