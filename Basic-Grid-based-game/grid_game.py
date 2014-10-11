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
SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255

class Grid_Game(object):
#Class attributes
	game_over = False
	WIDTH = 20
	HEIGHT = 20
	MARGIN = 5
	
#Class methods
#Constructor
	def __init__(self):
	#Set initial variables
		x = 1
	
	#Process keyboard and mouse actions
	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return True
			if event.type == pygame.MOUSEBUTTONDOWN:
				#print('Kalick: ', pygame.mouse.get_pos())
				print('Row:', self.pos_to_grid(pygame.mouse.get_pos())[0], 'Column', self.pos_to_grid(pygame.mouse.get_pos())[1])
				self.grid[self.pos_to_grid(pygame.mouse.get_pos())[0]][self.pos_to_grid(pygame.mouse.get_pos())[1]] += 1
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
		screen.fill(BLACK)

		if self.game_over:
			#draw game over screen
			text = 'GAME OVER!'
			screen.blit(text, [100, 100])

		if not self.game_over:
			#draw objects on screen
			self.fill_grid(screen)

		pygame.display.flip()
	
	def fill_grid(self, screen):
		self.boxes_width = SCREEN_WIDTH // (self.WIDTH + self.MARGIN)
		self.boxes_height = SCREEN_HEIGHT // (self.HEIGHT + self.MARGIN)
	
		for column in range(self.boxes_width):
			for row in range(self.boxes_height):
				if self.grid[row][column] == 3:
					self.grid[row][column] = 0
				elif self.grid[row][column] == 1:
					color = GREEN
				elif self.grid[row][column] == 2:
					color = BLUE
				elif self.grid[row][column] == 0:
					color = WHITE
				pygame.draw.rect(screen, color, [(self.MARGIN * (column + 1)) + (column * self.WIDTH), \
																					 (self.MARGIN * (row + 1)) + (row * self.HEIGHT), self.WIDTH, self.HEIGHT], 0)
				
	def fill_matrice(self):
		self.boxes_width = SCREEN_WIDTH // (self.WIDTH + self.MARGIN)
		self.boxes_height = SCREEN_HEIGHT // (self.HEIGHT + self.MARGIN)
		self.grid = [] 
		for row in range(self.boxes_width):
			self.grid.append([])
			for column in range(self.boxes_height):
				self.grid[row].append(0)
			
	def pos_to_grid(self, position):
		return [int(math.ceil(position[1] / (self.HEIGHT + self.MARGIN))), \
					int(math.ceil(position[0] / (self.WIDTH + self.MARGIN)))]
		

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Grid Marker")
    pygame.mouse.set_visible(True)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Grid_Game()
    game.fill_matrice()
 
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
  
