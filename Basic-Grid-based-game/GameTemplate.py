#Class based game template for Python
#import different modules and libraries
import pygame, math, random, os

# Gloval variables
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PURPLE = (146,32,162)

# File's path
PATH = os.getcwd()

# Screen size
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Game(object):
	#Class attributes
	game_over = False

	#Class methods
	#Constructor
	def __init__(self):
	#Set initial variables
	
	#Process keyboard and mouse actions
	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return True
			if event.type == pygame.MOUSEBUTTONDOWN:
					if self.game_over:
					#If in "game over" screen restart on mouse click
							self.__init__()
			
			#set moving speed direction on key down
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					x = 1
				if event.key == pygame.K_LEFT:
					x = 1
				if event.key == pygame.K_UP:
					x = 1
				if event.key == pygame.K_DOWN:
					x = 1
			#stop moving on key up
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:         
					x = 1
				if event.key == pygame.K_LEFT:
					x = 1
				if event.key == pygame.K_UP:
					x = 1
				if event.key == pygame.K_DOWN:
					x = 1

		return False
		
	#Game logic, where to draw what, when to play a sound etc.
	def run_logic(self):
		if not self.game_over:
			x = 1
	
	#Actually draw everything on screen
	def display_frame(self, screen):
		screen.fill(WHITE)

		if self.game_over:
			#draw game over screen
			screen.blit(text, [center_x, center_y])

		if not self.game_over:
			#draw objects on screen
			x = 1

		pygame.display.flip()

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Ninja")
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
	
if __name__ == "__main__":
	main()
  
