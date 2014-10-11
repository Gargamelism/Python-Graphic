import pygame, os, random

# Global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PATH = os.getcwd()

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
    good_apples = [os.path.join(PATH, 'good_apple_1.png'), \
                   os.path.join(PATH, 'good_apple_2.png'), \
                   os.path.join(PATH, 'good_apple_3.png')]
    bad_apple = os.path.join(PATH, 'bad_apple.png') 
     
    def __init__(self):
      """ Constructor, create the image of the block. """
      pygame.sprite.Sprite.__init__(self)
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(self.SCREEN_WIDTH)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1
 
        if self.rect.y > self.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()