import random
import pygame
import numpy as np
import logging
from blob import Blob


logging.basicConfig(filename = "logfile.log",level=logging.INFO)

"""DEBUG    Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR   Due to a more serious problem, the software has not been able to perform some function.
CRITICAL    A serious error, indicating that the program itself may be unable to continue running."""

WIDTH = 800
HEIGTH = 600
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
STARTING_BLUE_BLOBS = 10 
STARTING_RED_BLOBS = 10
STARTING_GREEN_BLOBS = 20

game_display = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class blue_blob(Blob):
    
    def __init__(self,x_boundary,y_boundary):
        super().__init__((0,0,255),x_boundary,y_boundary)

    def __add__(self,other_blob):
        logging.info(f"blob add op:{self}  + {other_blob} ")
        if other_blob.color == (255,0,0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0,255,0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0,0,255):
            pass
        else:
            raise Exception("Unsupported color!!")

def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y]) - np.array([b2.x,b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):
    blues , reds, greens = blob_list

    for blue_blob_id , blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(str(blue_blob), str(other_blob)))
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        elif blue_blob.size <= 0:
                            del blues[blue_blob_id]

    return blues,reds , greens

class red_blob(Blob):
    
    def __init__(self,x_boundary,y_boundary):
        super().__init__((255,0,0),x_boundary,y_boundary)


class green_blob(Blob):
    
    def __init__(self,x_boundary,y_boundary):
        super().__init__((0,255,0),x_boundary,y_boundary)
      


def draw_environment(blob_list):
    game_display.fill(WHITE)
    blues,reds , greens = handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues,reds , greens
    

def main():
    blue_blobs = dict(enumerate([blue_blob(WIDTH,HEIGTH) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([red_blob(WIDTH,HEIGTH) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([green_blob(WIDTH,HEIGTH) for i in range(STARTING_GREEN_BLOBS)]))

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            blue_blobs,red_blobs,green_blobs = draw_environment([blue_blobs,red_blobs,green_blobs])
            clock.tick(60)
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break


if __name__ == "__main__":
    
    main()


