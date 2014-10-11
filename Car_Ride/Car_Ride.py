#Game template for Python
#import and intialyze the graphics library
import pygame, math, random, time, os

pygame.init()

#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (48, 118, 58)
red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue = (7, 17, 139)
yellow = (255,255,0)
purple = (146,32,162)
light_gray = (200, 200, 200)
dark_gray = (100, 100, 100)

def print_log(string):
  log = open('log.txt', 'a')
  log.write(str(string) + '\n')
  log.close

# Drawing functions
def draw_hill(location, size):
  pygame.draw.arc(screen, dark_green, [location[0], location[1], size[0], 450], 0, math.pi, 200)
  pygame.draw.arc(screen, black, [location[0], location[1] - 3, size[0], 450], 0, math.pi, 10)
  #pygame.draw.arc(screen, black, [location[0], location[1] - 3, size[0], 450], 0, math.pi, 10)
  hill = calc_hill(location, size)
  return hill

def calc_hill(location, size):
  hill = [None] * size[0]
  #We actually want the angles between 180-360
  diff = 180
  for i in range(len(hill)):
    x = int(size[0]/2 + ((size[0] / 2) * math.cos(math.radians(i + diff)))) + (location[0] - 10)
    y = int(screen_height + ((size[1] / 2) * math.sin(math.radians(i + diff))))
    if y < 540:
      y = y + 1
    #pygame.draw.rect(screen, black, [200 + x, screen_height + y, 10, 10], 0)
    hill[i] = [x, y]
    #print(hill[i])
    if i > 4:
      back = i - 5
      car_angle = calc_car_angle(hill[back], hill[i])
      if car_angle == 0:
        hill[back][1] = hill[back][1] + 2
      hill[back] = [hill[back][0], hill[back][1], calc_car_angle(hill[back], hill[i])]
      #print(hill[i-15])
  return hill 

def draw_car(car, coord, hill, prev_angle):
  #horizontal_rect = [0, 0, 30, 15]
  location = get_car_location(coord, hill)
  #print_log(location)

  new_car = pygame.transform.rotate(car, -location[2])
  return [new_car, location] 
  
def car_jump(i, y_coord, up):
  if up:
    return y_coord - (i * 3)
  else:
    return y_coord + (i * 3) - 20

def car_advance(x_speed, forward):
  if forward == 1:
  #controlled acceleration
    if x_speed > 5:
      return x_speed + 0.2
    else:
      return x_speed + 1
  else:
    if x_speed > 6:
      return x_speed - 0.2
    elif x_speed < -5:
      return -6
    else:
      return x_speed - 1

def calc_car_angle(point_1, point_2):
  delta_x = point_2[0] - point_1[0]
  delta_y = point_2[1] - point_1[1]
  if(delta_x == 0):
    delta_x = 1
  return math.atan(delta_y / delta_x) * 180 / math.pi

def get_car_location(point, point_list):
  #special binary search implementation that finds the number or the latest
  min = 0
  max = 179 #len(point_list) - 1
  while max >= min:
    mid = max - int((max - min)/2)
    if max == min:
      mid = min + 1
    if point_list[mid][0] == point[0] or max == mid:
      return point_list[mid]
    elif point[0] > point_list[mid][0]:
      min = mid
    elif point[0] < point_list[mid][0]:
      max = mid
    #print(mid)
  return -1

#Set the width and height of the screen
screen_width = 1500
screen_height = 600 #500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

#Starting variables that might change during program run
# Loading graphics files
#file names
fuzzcar = "fuzzcar.png"
main_theme = "Car_Ride_main.ogg"

path = os.getcwd()
orig_car = pygame.image.load(os.path.join(path, fuzzcar)).convert()

car_angle = 0
# Loading sound files
main_theme = pygame.mixer.Sound(os.path.join(path, main_theme))
solo_seg = []
solo_seg.append(pygame.mixer.Sound(os.path.join(path, "solo_seg-001.ogg")))
solo_seg.append(pygame.mixer.Sound(os.path.join(path, "solo_seg-002.ogg")))
solo_seg.append(pygame.mixer.Sound(os.path.join(path, "solo_seg-003.ogg")))
solo_seg.append(pygame.mixer.Sound(os.path.join(path, "solo_seg-004.ogg")))
main_theme.play(-1)

#Set window title
pygame.display.set_caption("On the Road Again (Turn the Page)")

#Boolean to know if to stop or not
done = False

#Timing, this way we can schedule FPS
clock = pygame.time.Clock()

#Keyboard starting speed and location
x_speed = 0
y_speed = screen_height - 30
y_coord = screen_height - 30
x_coord = 0

jump = 0

# ----Main Program Loop----
while done == False:
  #All processing should go BELOW this comment

  for event in pygame.event.get(): #User did something
    if event.type == pygame.QUIT: #User clicked on the "close"
      done = True #and close the game
      print("Good-bye")
      pygame.quit() #proper closing of windows
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        x_speed = car_advance(x_speed, 1)
      if event.key == pygame.K_LEFT:
        x_speed = car_advance(x_speed, -1)
      if event.key == pygame.K_SPACE:
        random.choice(solo_seg).play()
        jump = 1
    if event.type == pygame.KEYUP:
      print("key released")
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("mouse clicked")
    if event.type == pygame.MOUSEBUTTONUP:
      print("mouse release")

  #All processing should go ABOVE this comment

  #All game logic should go BELOW this comment
  #car moving
  x_coord += x_speed
  
  #All game logic should go ABOVE this comment

  #All drawing code should go BELOW this comment
  # set background color with:
  screen.fill(dark_blue)
  #moon
  pygame.draw.circle(screen, light_gray, [int(screen_width/2), 0], 100, 0)
  #hill
  hill_1 = draw_hill([-10, 400], [1550, 400])

 
  if x_coord < 0 - 20:
    x_coord = screen_width
  elif x_coord > screen_width:
    x_coord = 0
  
  #pygame.draw.rect(screen, black, [100, 100, 31, 31], 1)
  car_list = draw_car(orig_car, [x_coord, y_coord], hill_1, car_angle)
  #car_angle = car_list[1][2]
  if not jump:
    car = car_list[0]
    height_diff = 10
    y_coord = car_list[1][1] - height_diff
    i = 0
    j = 0
  else:
    car = orig_car
    if i < 11:
      y_coord = car_jump(i, car_list[1][1] - height_diff, 1)
      i = i + 1
    elif i > 10:
      y_coord = car_jump(j, car_list[1][1] - height_diff, 0)
      j = j + 1
      if j == 10:
        i = j = 0
        jump = 0

  screen.blit(car, [x_coord, y_coord])
  orig_car.set_colorkey(black)
   
  pygame.display.flip() #After you finish drawing you must FLIP
  #All drawing code should go ABOVE this comment

  #set FPS to 20
  clock.tick(20)
  
