import pygame as pg
import sys
import pickle
from settings import *
from classes import *
from camera import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pg.display.set_caption(DISPLAY_TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1, 1)
        self.load_data()
        self.set_current_map(self.testmap_map)
        self.get_map_data()

    def load_data(self):
        # load the map data
        self.testmap2_map = pickle.load(open(os.path.join(LEVELS_FOLDER, "testmap2.p"), "rb"))
        self.yellow_map = pickle.load(open(os.path.join(LEVELS_FOLDER, "yellow.p"), "rb"))
        self.testmap_map = pickle.load(open(os.path.join(LEVELS_FOLDER, "testmap.p"), "rb"))

        # load the image data
        self.banana_img = pg.image.load(os.path.join(SPRITE_FOLDER, "floor.png"))
        self.banana_img = pg.transform.scale(self.banana_img, (TILE_SIZE, TILE_SIZE))
        self.wall_img = pg.image.load(os.path.join(SPRITE_FOLDER, "wall.png"))
        self.wall_img = pg.transform.scale(self.wall_img, (TILE_SIZE, TILE_SIZE))
        self.floor_img = pg.image.load(os.path.join(SPRITE_FOLDER, "floor.png"))
        self.floor_img = pg.transform.scale(self.floor_img, (TILE_SIZE, TILE_SIZE))
        self.barrel_img = pg.image.load(os.path.join(SPRITE_FOLDER, "barrel.png"))
        self.barrel_img = pg.transform.scale(self.barrel_img, (TILE_SIZE, TILE_SIZE))
        self.tile_img = pg.image.load(os.path.join(SPRITE_FOLDER, "tile.png"))
        self.tile_img = pg.transform.scale(self.tile_img, (TILE_SIZE, TILE_SIZE))
        self.tree_img = pg.image.load(os.path.join(SPRITE_FOLDER, "tree.png"))
        self.tree_img = pg.transform.scale(self.tree_img, (TILE_SIZE, TILE_SIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.background_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        self.camera = Camera(self.map_width, self.map_height)
        self.load_tiles(self.current_map)

    def set_current_map(self, map_data):
        # TODO: use this method to change the current map
        self.current_map = map_data
        self.get_map_data()

    def get_map_data(self):
        self.map_width = len(self.current_map[0]) * 32
        self.map_height = len(self.current_map) * 32

    def load_tiles(self, current_map):
        for col, colors in enumerate(self.current_map):
            for row, color in enumerate(colors):
                # each color will load a specific tile
                if color == (230, 230, 19):
                    banana(self, col, row)
                if color == (0, 0, 0):
                    wall(self, col, row)
                if color == (255, 255, 255):
                    floor(self, col, row)
                if color == (0, 0, 255):
                    barrel(self, col, row)
                if color == (255, 0, 0):
                    tile(self, col, row)
                if color == (0, 255, 0):
                    tree(self, col, row)

        self.player = Player(self, 4, 4)


    def unload_tiles(self):
        for sprite in self.background_sprites:
            if sprite is not self.player:
                sprite.kill()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(DISPLAY_FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.background_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for sprite in self.background_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

                if pressed[pg.K_w]:
                    self.player.move(dy=-1)
                if pressed[pg.K_s]:
                    self.player.move(dy=1)
                if pressed[pg.K_a]:
                    self.player.move(dx=-1)
                if pressed[pg.K_d]:
                    self.player.move(dx=+1)


g = Game()
while True:
    g.new()
    g.run()
