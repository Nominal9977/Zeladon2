
# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# screen settings
WIDTH = 800
HEIGHT = 600
TITLE = "My Awesome house"
FPS = 60


# Define colors
'''
Each color is defined as and RGB tuple. A search for'RGB color picker'
should provide you with tools to get the values for other colors.
'''
WHITE =(255,255,255)
RED =(247, 7, 7)
GREEN =(20, 227, 9)
BLUE =(46, 31, 112)
LIGHT_BLUE = (173, 216 , 230)
BLACK = (0,0,0)
BASE=(49, 9, 227)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
YELLOW = (255, 255, 150)
DARK_GREEN = ( 1, 50, 32)








    
# Fonts
FONT_SM = pygame.font.Font(None, 48)
FONT_MD = pygame.font.Font(None, 64)
FONT_LG = pygame.font.Font(None, 96)

#sounds
pygame.mixer.music.load("snd/birds_wind.ogg")
pygame.mixer.music.load("snd/crickets.ogg")





# Make the screen
surface = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()



#functions
def draw_sky(color):
    surface.fill(color)
def draw_sun():
    pygame.draw.ellipse(surface, YELLOW, [-100, -100, 200, 200])
def draw_moon():
    pygame.draw.ellipse(surface, WHITE, [-100, -100, 200, 200])

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
        
    pygame.draw.ellipse(surface, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(surface, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(surface, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(surface, color, [x + 35, y, 50, 50])
    pygame.draw.rect(surface, color, [x + 20, y + 20, 60, 40])

def  draw_bush(loc, color):
    x = loc[0]
    y = loc[1]
        
    pygame.draw.ellipse(surface, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(surface, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(surface, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(surface, color, [x + 35, y, 50, 50])
    pygame.draw.rect(surface, color, [x + 20, y + 20, 60, 40])


def draw_grass():
    pygame.draw.rect(surface, DARK_GREEN, [0, 300, 800, 300])

def draw_house(light_on):
     pygame.draw.rect(surface, BASE, [105,120,290,260], 0)

 
     pygame.draw.polygon(surface, RED, [[75,120], [430,120], [245, 5]], 0)
  

     if light_on:
          
          
          pygame.draw.rect(surface, YELLOW, [155, 155, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [235, 155, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [315, 155, 30, 30], 0)
  
          pygame.draw.rect(surface, YELLOW, [155, 215, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [235, 215, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [315, 215, 30, 30], 0)
  
          pygame.draw.rect(surface, YELLOW, [155, 275, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [235, 275, 30, 30], 0)
          pygame.draw.rect(surface, YELLOW, [315, 275, 30, 30], 0)

     else:
          pygame.draw.rect(surface, BLACK, [155, 155, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [235, 155, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [315, 155, 30, 30], 0)
  
          pygame.draw.rect(surface, BLACK, [155, 215, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [235, 215, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [315, 215, 30, 30], 0)
  
          pygame.draw.rect(surface, BLACK, [155, 275, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [235, 275, 30, 30], 0)
          pygame.draw.rect(surface, BLACK, [315, 275, 30, 30], 0)
          
  

     pygame.draw.rect(surface, WHITE, [190, 315, 30, 65], 0)
     pygame.draw.rect(surface, WHITE, [290, 315, 30, 65], 0)
  
     pygame.draw.rect(surface, BLACK, [200, 340, 20, 10], 0)
     pygame.draw.rect(surface, BLACK, [290, 340, 20, 10], 0)

def draw_sky(color):
     surface.fill(sky_color)

def draw_stars():
    for loc in star_locs:
        x = loc[0]
        y = loc[1]
        pygame.draw.ellipse(surface, WHITE, [x, y, 3, 3])
    

def play_music(file, loops):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops)    

# Initial state
daytime = True
light_on = False

running = True
num_clouds = 10
num_stars = random.randrange(50, 600)
num_bush = 10


#make clouds
cloud_locs = []
while len(cloud_locs) < num_clouds:
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, 150)
    loc = [x, y]
    
    cloud_locs.append(loc)

# Make stars
star_locs = []
while len(star_locs) < num_stars:
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, 300)
    loc = [x, y]
    star_locs.append(loc)
    
# making a bush 
bush_locs = []
x = -100
while len(bush_locs) < num_bush:
    
    x = (x + 100)
    y = random.randrange(400,401 )
    loc = [x, y]
    bush_locs.append(loc)

# Game loop
pygame.mixer.music.play(-1)


    
    

while running:
    # Input handling
    '''
    This is where we React to key presses, mouse clicks, etc. For now,
    we'll just check to see if the X is clicked.
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                daytime = not daytime
            elif event.key == pygame.K_l:
                light_on = not light_on

            
    # Game logic
    '''
    This is where we do things like check for collisions, update coordinates
    of moving objects, etc.) We'll leave this section alone for now.
    ''' 
    if daytime:
        sky_color = LIGHT_BLUE
        cloud_color = WHITE
        bush_color = GREEN 
    else:
        sky_color = BLACK
        cloud_color = GRAY
        bush_color = GRAY
    for loc in cloud_locs:
        loc[0] += 1

        if loc[0] > WIDTH:
            loc[0] = -100
    # Drawing code
    '''
    Understand that nothing is actully drawn on the screen here. Instead,
    the picture is assembled in the computers memory.

   '''
    
    draw_sky(sky_color)
    draw_grass()
    if not daytime:
        draw_stars()
        play.crickets.ogg 
    if daytime:
        draw_sun()
        play.brids_wind.ogg
        
    else:
        draw_moon()

    for loc in cloud_locs:
        draw_cloud(loc, cloud_color )
    
    for loc in bush_locs:
        draw_bush (loc, bush_color )
    draw_house(light_on)

    
    
   
   
    
        
      
        

    
    
    

     # Update screen (Actually draw the picture in the screen.)
    '''
    The update() function takes the picture from the computer's memory buffer
    and actually puts it on the screen.
    '''
    pygame.display.update()

    # Limit refresh rate of game loop
    '''
    The game loop will pause for a bit here so that the screen refreshes at
    the desired rate.
    '''
    clock.tick(FPS)

# Close window and quit
pygame.quit()
