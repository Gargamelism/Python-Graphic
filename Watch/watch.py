# a graphical watch according to Gozanis specs

import sys, getopt, pygame, time, math, datetime
from time import localtime
from os.path import basename

pygame.init()

# global variables
# struct_time constants
TM_HOUR = 3
TM_MIN = 4
TM_SEC = 5

# define colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
light_blue = (0,128,255)
yellow = (255,255,0)

# set screen size and FPS
width = 700
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)
screen_clock = pygame.time.Clock()

def print_help():
    print('Usage example:', file_name, '-h 13 -m 3 -s 64')
    print('\t', file_name, '--hours 13 --minutes 3 --seconds 64')
    sys.exit(2)

# breaks down the input arguments
def get_time(argv, file_name):
  hours = 0
  minutes = 0
  seconds = 0

  # check if the arguments exist
  try:
    opts, args = getopt.getopt(argv, "h:m:s:", ["hours=", "minutes=", "seconds="])
  except getopt.GetoptError:
    print_help()
  # assign the arguments
  for opt, arg in opts:
    if opt in ("-h", "--hours"):
      hours = int(arg) % 24
    elif opt in ("-m", "--minutes"):
      minutes = int(arg) % 60
    elif opt in ("-s", "--seconds"):
      seconds = int(arg) % 60

  return[hours, minutes, seconds]

def get_current_time(hours_dif, minutes_dif, seconds_dif):
  system_time = time.localtime()
  hours = (system_time[TM_HOUR] + hours_dif) % 12
  minutes = (system_time[TM_MIN] + minutes_dif) % 60
  seconds = (system_time[TM_SEC] + seconds_dif) % 60
  return [hours, minutes, seconds]
        

def create_time_marks(time_unit, mark_count, mark_radius):
    mark_dict_base = {'time_frame': [0, 0], 'position': [0, 0], 'color': 0}
    # create an array that can hold all of the dictionary's information
    mark_array = [mark_dict_base] * mark_count

    # information to calculate the marks' position
    circle_center = [width // 2, height // 2]

    # identify if a certain mark is responsible for multiple time frames
    step = 1
    if(mark_count != time_unit):
        # if it doesn't divide it requires a specific solution
        if((time_unit % mark_count) != 0):
            return 0
        step = math.ceil(time_unit / mark_count)

    # fill the array
    i = int(mark_count * 0.75) # fix offset from circle start to clock start
    for marks in range(len(mark_array)):
        time_frame = [i * step, (i * step) + step - 1]
        # angle of mark in radians
        theta = marks * (2 * math.pi / mark_count)
        position = [circle_center[0] + int(-1 * (mark_radius * math.cos(theta))), \
                    circle_center[1] + int(-1 * (mark_radius * math.sin(theta)))]
        color = 0
        if(step > 1 and (marks % 2) != 0):
            color = 1
        mark_array[i] = {'time_frame': time_frame, 'position': position, 'color': color}
        i += 1
        i %= mark_count
    return mark_array
    
    #print(mark_array)

def draw_time_marks(current_time, time_array, main_color, secondary_color):
  small_radius = 5

  if(not time_array):
      return 0
  for marks in range(len(time_array)):
    color = main_color
    # check if current time is within range
    if(time_array[marks]['time_frame'][0] <= current_time and \
       time_array[marks]['time_frame'][1] >= current_time):
      color = black
      if(1 == time_array[marks]['color']):
          color = secondary_color
    pygame.draw.circle(screen, color, time_array[marks]['position'], small_radius, 0)
    #print(seconds)

def main(argv, file_name):
  user_time = get_time(argv, file_name)

  hours = user_time[0]
  minutes = user_time[1]
  seconds = user_time[2]

  cur_time = datetime.time(hours, minutes, seconds)
  print(time)

  hours_array = create_time_marks(12, 12, (width - 20) // 8)
  minutes_array = create_time_marks(60, 20, (width - 20) //4)
  seconds_array = create_time_marks(60, 60, (width - 20) // 2)
  # get current system time, and create an offset to the current time
  system_time = time.localtime()
  hours_dif = abs(system_time[TM_HOUR] - hours)
  minutes_dif = abs(system_time[TM_MIN] - minutes)
  seconds_dif = abs(system_time[TM_SEC] - seconds)


  is_running = True
# ---- Main Loop ----
  while(is_running == True):
    current_time = get_current_time(hours_dif, minutes_dif, seconds_dif)
    hours = current_time[0]
    minutes = current_time[1]
    seconds = current_time[2]

    print(cur_time)

    draw_time_marks(hours, hours_array, red, 0)
    draw_time_marks(minutes, minutes_array, light_blue, blue)    
    draw_time_marks(seconds, seconds_array, yellow, 0)
    
    pygame.display.flip()

    screen_clock.tick(60)

if __name__ == "__main__":
  main(sys.argv[1:], basename(sys.argv[0]))

