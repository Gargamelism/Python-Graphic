#Game template for Python
#import and intialyze the graphics library
import pygame, math, random

pygame.init()

#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
purple = (146,32,162)

#Drawing Classes
class Rectangle:
  #attributes
  x = 0
  y = 0
  height = 0
  width = 0
  surface = ""
  direction_x = 1
  direction_y = 1
  color = (0, 0, 0)
  
  #methods
  #def __init__(self, x, y, height, width, surface):
  
  def draw(self):
    pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.width, self.height], 0)
  
  def move(self, x, y):
    #handle arriving to the edge and being created over the edge
    if self.x > pygame.display.Info().current_w - self.width or self.x < 0:
      self.direction_x *= -1
      if self.x > pygame.display.Info().current_w - self.width:
        self.x = pygame.display.Info().current_w - self.width
    if self.y > pygame.display.Info().current_h - self.height or self.y < 0:
      self.direction_y *= -1
      if self.y > pygame.display.Info().current_h - self.height:
        self.y = pygame.display.Info().current_h - self.height
    self.x += (x * self.direction_x)
    self.y += (y * self.direction_y)
    
  def print(self):
    print(self.x, self.y, self.height, self.width)

class Ellipse(Rectangle):
  #overridden methods
  def draw(self):
    pygame.draw.ellipse(self.surface, self.color, [self.x, self.y, self.width, self.height], 0)

# Drawing functions

#Set the width and height of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Loading graphics files

#Set window title
pygame.display.set_caption("Colored Shaped")

#Boolean to know if to stop or not
done = False

#Timing, this way we can schedule FPS
clock = pygame.time.Clock()

#Variables and objects that need to be stable before the loop
myList = []
for i in range(1000):
  if i % 2 == 0:
    myObject = Rectangle()
  else:
    myObject = Ellipse()
  myObject.surface = screen
  myObject.x = random.randrange(700)
  myObject.y = random.randrange(500)
  myObject.height = random.randint(20, 70)
  myObject.width = random.randint(20, 70)
  myObject.color = (random.randrange(255), random.randrange(255), random.randrange(255))
    
  change_x = random.randint(-3, 3)
  change_y = random.randint(-3, 3)
  
  myList.append([myObject, change_x, change_y])

## Testing grounds
#my_rect = Rectangle()
#my_rect.surface = screen
#my_rect.x = 4 
#my_rect.y = 459 
#my_rect.width = 52 
#my_rect.height = 61

# ----Main Program Loop----
while done == False:
  #All processing should go BELOW this comment

  for event in pygame.event.get(): #User did something
    if event.type == pygame.QUIT: #User clicked on the "close"
      done = True #and close the game
      print("Good-bye")
      pygame.quit() #proper closing of windows
    if event.type == pygame.KEYDOWN:
      print("Key pressed")
    if event.type == pygame.KEYUP:
      print("key released")
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("mouse clicked")
    if event.type == pygame.MOUSEBUTTONUP:
      print("mouse released")

  #All processing should go ABOVE this comment

  #All game logic should go BELOW this comment
  #All game logic should go ABOVE this comment

  #All drawing code should go BELOW this comment
  # set background color with:
  screen.fill(black)
  
  for shape in myList:
    shape[0].move(shape[1], shape[2])
    shape[0].draw()

## Testing grounds
#  my_rect.move(-3, -3)
#  my_rect.draw()

  pygame.display.flip() #After you finish drawing you must FLIP
  #All drawing code should go ABOVE this comment

  #set FPS to 20
  clock.tick(20)
  