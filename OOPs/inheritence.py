import random
import pygame
from blob import Blob

WIDTH = 800
HEIGTH = 600
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 9

game_display = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class blue_blob(Blob):
    
    def __init__(self,color,x_boundary,y_boundary):
        super().__init__(color,x_boundary,y_boundary)
        self.color = BLUE

    def move_fast(self):
        self.x += random.randrange(-7,7)
        self.y += random.randrange(-7,7)


class red_blob(Blob):
    
    def __init__(self,color,x_boundary,y_boundary):
        super().__init__(color,x_boundary,y_boundary)
        self.color = RED

    def move_fast(self):
        self.x += random.randrange(-7,7)
        self.y += random.randrange(-7,7)


def draw_environment(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)
            blob.move_fast()
            blob.check_bounds()
    pygame.display.update()
    

def main():
    blue_blobs = dict(enumerate([blue_blob(BLUE,WIDTH,HEIGTH) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([red_blob(RED,WIDTH,HEIGTH) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)


if __name__ == "__main__":
    main()


