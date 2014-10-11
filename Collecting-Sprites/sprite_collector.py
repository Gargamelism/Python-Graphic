import pygame, random, os, block, good_block, bad_block

#--- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PATH = os.getcwd()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
 
# --- Classes ---
 
class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    
    #Attributes
    change_x = 0
    change_y = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(PATH, 'yozhik.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.facing_direction = 1 
    
    def change_direction(self, change_direction):
      if self.facing_direction != change_direction:
        self.image = pygame.transform.flip(self.image, True, False)
        self.facing_direction *= -1
      
    def change_speed(self, x, y):
      self.change_x += x
      self.change_y += y
 
    def play_sound(self, sound):
      slide = pygame.mixer.Sound(os.path.join(PATH, 'slide_efect.ogg'))
      if sound == 0:
        slide.play()
 
    def update(self):
        """ Update the player location. """
        #pos = pygame.mouse.get_pos()
        self.rect.x += self.change_x #pos[0]
        if self.rect.x < 0 - self.image.get_width():
          self.play_sound(0)
          self.rect.x = SCREEN_WIDTH
        if self.rect.x > SCREEN_WIDTH:
          self.play_sound(0)
          self.rect.x = 0
          
        self.rect.y += self.change_y #pos[1]
        if self.rect.y < 0 - self.image.get_height():
          self.play_sound(0)
          self.rect.y = SCREEN_HEIGHT
        if self.rect.y > SCREEN_HEIGHT:
          self.play_sound(0)
          self.rect.y = 0
 
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
        
    # --- Class attributes.
    # In this case, all the data we need
    # to run our game.
 
    # Sprite lists
    block_list = None
    all_sprites_list = None
    player = None
 
    # Other data
    game_over = False
    score = 0
    
    # --- Class methods
    # Set up the game
    def __init__(self):
        self.score = 0
        self.game_over = False
 
        # Create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
 
        # Create the block sprites
        for i in range(50):
            temp_good_block = good_block.GoodBlock(SCREEN_WIDTH, SCREEN_HEIGHT)
            temp_bad_block = bad_block.BadBlock(SCREEN_WIDTH, SCREEN_HEIGHT)
 
            temp_good_block.rect.x = random.randrange(SCREEN_WIDTH)
            temp_good_block.rect.y = random.randrange(SCREEN_HEIGHT - temp_good_block.rect.height)
            temp_bad_block.rect.x = random.randrange(SCREEN_WIDTH)
            temp_bad_block.rect.y = random.randrange(SCREEN_HEIGHT - temp_bad_block.rect.height)
 
            self.good_block_list.add(temp_good_block)
            self.bad_block_list.add(temp_bad_block)
            self.all_sprites_list.add(temp_good_block)
            self.all_sprites_list.add(temp_bad_block)
 
        # Create the player and place him at the beginning
        self.player = Player()
        self.player.rect.x = SCREEN_WIDTH / 2
        self.player.rect.y = SCREEN_HEIGHT - self.player.image.get_height()
        self.all_sprites_list.add(self.player)
 
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
            
            #set moving speed direction on key down
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                self.player.change_direction(-1)
                self.player.change_speed(5, 0)                
              if event.key == pygame.K_LEFT:
                self.player.change_direction(1)
                self.player.change_speed(-5, 0)
              if event.key == pygame.K_UP:
                self.player.change_speed(0, -5)
              if event.key == pygame.K_DOWN:
                self.player.change_speed(0, 5)
            #stop moving on key up
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_RIGHT:         
                self.player.change_speed(-5, 0)                
              if event.key == pygame.K_LEFT:
                self.player.change_speed(5, 0)
              if event.key == pygame.K_UP:
                self.player.change_speed(0, 5)
              if event.key == pygame.K_DOWN:
                self.player.change_speed(0, -5)
 
        return False
 
    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
 
            # See if the player block has collided with anything.
            good_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            bad_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)
 
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.score += 1
                self.play_sound(0)
                #print(self.score)
            for block in bad_blocks_hit_list:
                self.score -= 1
                self.play_sound(1)
                #print(self.score)

            
            # You can do something with "block" here.
            
            if len(self.good_block_list) == 0:
                self.game_over = True
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)
 
        if self.game_over:
            #font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, you have collected: " + str(self.score) + " ripe apples click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            self.print_score(screen)
 
        pygame.display.flip()
    
    def print_score(self, surface):
      font = pygame.font.SysFont("Calibri", 25, True, False)
      current_score = font.render("Score: " + str(self.score), True, BLACK)
      score_x = SCREEN_WIDTH - current_score.get_width()
      score_y = SCREEN_HEIGHT - current_score.get_height()
      surface.blit(current_score, [score_x, score_y])
    
    def play_sound(self, sound):
      success = pygame.mixer.Sound(os.path.join(PATH, 'success.ogg'))
      fail = pygame.mixer.Sound(os.path.join(PATH, 'fail_effects.ogg'))
      if sound == 0:
        success.play()
      if sound == 1:
        fail.play()
 
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
