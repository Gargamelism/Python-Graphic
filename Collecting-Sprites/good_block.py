import pygame, block, random, os
from sprite_collector import SCREEN_HEIGHT, SCREEN_WIDTH

# Global constants
BLACK = (0, 0, 0)

PATH = os.getcwd()

class GoodBlock(block.Block):
    """ This class represents the good blocks the player collects. """
    good_apples = [os.path.join(PATH, 'good_apple_1.png'), \
                   os.path.join(PATH, 'good_apple_2.png'), \
                   os.path.join(PATH, 'good_apple_3.png')]
    
    def __init__(self, screen_width, screen_height):
      self.SCREEN_HEIGHT = screen_height
      self.SCREEN_WIDTH = screen_width
      
      """ Constructor, create the image of the block. """
      block.Block.__init__(self)
      self.image = pygame.image.load(random.choice(self.good_apples)).convert()
      self.image.set_colorkey(BLACK)
      self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randint(0, self.SCREEN_HEIGHT)
        self.rect.x = random.randint(0, self.SCREEN_WIDTH)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += random.randint(-3, 3)
        self.rect.x += random.randint(-3, 3)
 
        if self.is_out_of_site(self.rect.x, self.rect.y):
            self.reset_pos()
    
    def is_out_of_site(self, x, y):
      if y < 0 or x < 0 or y > self.SCREEN_HEIGHT or x > self.SCREEN_WIDTH:
        return 1
      return 0