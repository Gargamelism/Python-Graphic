import pygame, block, random, os

# Global constants
BLACK = (0, 0, 0)

PATH = os.getcwd()

class BadBlock(block.Block):
    """ This class represents the bad blocks the player collects. """
    bad_apple = os.path.join(PATH, 'bad_apple.png') 
    direction = 1
    
    def __init__(self, screen_width, screen_height):
      self.SCREEN_HEIGHT = screen_height
      self.SCREEN_WIDTH = screen_width
      
      """ Constructor, create the image of the block. """
      block.Block.__init__(self)
      self.image = self.image = pygame.image.load(self.bad_apple).convert()
      self.image.set_colorkey(BLACK)
      self.rect = self.image.get_rect()
     
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(self.SCREEN_WIDTH)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1 * self.direction 
 
        if self.rect.y > self.SCREEN_HEIGHT - self.rect.height or self.rect.y < 0:
            self.direction *= -1
            