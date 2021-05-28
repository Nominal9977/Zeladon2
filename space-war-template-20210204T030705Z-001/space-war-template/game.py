# Imports
import pygame
import random


# Window settings
WIDTH = 960
HEIGHT = 660
TITLE = "a shippy game"
FPS = 60

# game stages
START = 0
PLAYING = 1
END = 2

# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Load fonts
tittle_font=pygame.font.Font("assets/fonts/recharge bd.ttf", 80)
default_font=pygame.font.Font(None, 40) 

# Load images
ship_img = pygame.image.load("assets/images/playerShip.png").convert_alpha()
enemyRed_img = pygame.image.load("assets/images/enemyRed.png").convert_alpha()
enemyBlack_img = pygame.image.load("assets/images/enemyBlack.png").convert_alpha()
laserRed_img = pygame.image.load("assets/images/laserRed.png").convert_alpha()
laserBlue_img = pygame.image.load("assets/images/LaserBlue.png").convert_alpha()
powerup_img = pygame.image.load("assets/images/powerupYellow_bolt.png").convert_alpha()



# Load sounds
laser_snd =pygame.mixer.Sound('assets/sounds/laser.ogg')
explosion_snd= pygame.mixer.Sound('assets/sounds/explosion.ogg')


#music
start_music = 'assets/music/intro.ogg'

main_theme = 'assets/music/theme.ogg'

# Game classes
class Ship(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5
        self.shield = 3 
    def move_left(self):
        self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
         x = self.rect.centerx
         y = self.rect.top

         lasers.add( Laser(x, y, laserRed_img) )
         

         
         

         laser_snd.play()

    def check_bombs(self):
        hits = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hits:
            self.shield -= 1

            if self.shield <= 0 :
                self.kill()
                explosion_snd.play 
        

    def check_powerups(self):
        hits = pygame.sprite.spritecollide(self, powerups, True)

        for hit in hits:
            hit.apply(self)
            print('Bwooooooop!')
            
    def update (self):
       self.check_bombs()
       self.check_powerups()
       
class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5
    def update(self):
        self.rect.y -= self.speed




class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image, shield, value):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.shield = shield
        self.value = value

    def update (self):
        hits = pygame.sprite.spritecollide(self, lasers, True)

        for laser in hits:
            self.shield -=1
        if self.shield <= 0:
             self.kill()
             explosion_snd.play()
             player.score += self.value 
             print(player.score)

    def drop_bomb(self):
        x = self.rect.centerx
        y = self.rect.bottom

        bomb = Bomb(x, y, laserBlue_img)

        bombs.add(bomb)
            
        
class Fleet(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)

        self.speed = 2
        self.bomb_rate = 3

    def move(self):
        reverse = False
        for sprite in self.sprites():
            sprite.rect.x += self.speed

            if sprite.rect.right > WIDTH or sprite.rect.left < 0:
                reverse = True
        if reverse:
            self.speed *= -1
    def select_bomber(self):
       
        sprites = self.sprites()

        if len(sprites) > 0:
            
            r = random.randrange(0,120)
            if r < self.bomb_rate + player.level:
                bomber = random.choice(sprites)
                bomber.drop_bomb()
            

    def update(self, *args):
        super().update(*args)
        self.move()

        if len(player) >0:
            self.select_bomber()
class Bomb(pygame.sprite.Sprite):

   def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 4
   def drop_bomb(self):
        x = self.rect.centerx
        y = self.rect.bottom

        bomb = Bomb(x, y, laserBlue_img)

        bombs.add(bomb)
   def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class ShieldPowerup(pygame.sprite.Sprite):

   def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5
   def apply(self, ship):
        ship.shield = 3 
   def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

            
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image, shield, value):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.shield = shield
        self.value = value

    def update (self):
        hits = pygame.sprite.spritecollide(self, lasers, True)

        for laser in hits:
            self.shield -=1
        if self.shield <= 0:
             self.kill()
             explosion_snd.play()
             player.score += self.value 
             print(player.score)

    def drop_bomb(self):
        x = self.rect.centerx
        y = self.rect.bottom

        bomb = Bomb(x, y, laserBlue_img)

        bombs.add(bomb)

# Setup
def new_game():
    global ship, player  
    start_x = WIDTH/2
    start_y = HEIGHT - 100
    ship = Ship(start_x, start_y, ship_img)
    player = pygame.sprite.GroupSingle()
    player.add(ship)
    
    player.score = 0
    player.level = 1
    pygame.mixer.music.load(start_music)
    pygame.mixer.music.play(-1)

def start_level():
    global enemies,lasers,bombs,powerups
    if player.level == 1:
        e1= Enemy(150, 200,enemyRed_img, 1, 10 )
        e2= Enemy(250, 200,enemyRed_img, 1, 10 )
        e3= Enemy(350, 200,enemyRed_img, 1, 10 )
        enemies = Fleet(e1,e2,e3,)
    if player.level == 2: 
        e1= Enemy(150, 200,enemyRed_img, 1, 10 )
        e2= Enemy(250, 200,enemyRed_img, 1, 10 )
        e3= Enemy(350, 200,enemyRed_img, 1, 10 )
        e4= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e5= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

    
    if player.level == 3: 
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e5= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

    if player.level == 4:
    
        e1= Enemy(150, 200,enemyRed_img, 1, 10 )
        e2= Enemy(250, 200,enemyRed_img, 1, 10 )
        e3= Enemy(350, 200,enemyRed_img, 1, 10 )
        e4 =Enemy(450, 200,enemyRed_img, 1, 10 )
        e5 =Enemy(550, 200,enemyRed_img, 1, 10 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

    if player.level == 5:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)
    if player.level == 6:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)
    if player.level == 7:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)
    if player.level == 8:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

    if player.level == 9:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

    if player.level == 10:
    
        e1= Enemy(150, 200,enemyBlack_img, 3, 50 )
        e2= Enemy(250, 200,enemyBlack_img, 3, 50 )
        e3= Enemy(350, 200,enemyBlack_img, 3, 50 )
        e4 =Enemy(450, 200,enemyBlack_img, 3, 50 )
        e5 =Enemy(550, 200,enemyBlack_img, 3, 50 )
        e6= Enemy(215, 100,enemyBlack_img, 3, 50 )
        e7= Enemy(315, 100,enemyBlack_img, 3, 50 )
        enemies = Fleet(e1,e2,e3,e4,e5)

        
    lasers= pygame.sprite.Group()
    bombs= pygame.sprite.Group()

    x = random.randint(0, WIDTH)
    y = random.randint( -3000, -1000)
    p1 = ShieldPowerup( x, y, powerup_img)

    powerups = pygame.sprite.Group(p1)


def display_stats():
    score_text = default_font.render("Score: " + str(player.score), True, WHITE)
    rect = score_text.get_rect()
    rect.top = 20
    rect.left = 20
    screen.blit(score_text, rect)

    level_text = default_font.render("Level: " + str(player.level), True, WHITE)
    rect = score_text.get_rect()
    rect.top = 20
    rect.right = WIDTH - 20 
    screen.blit(level_text, rect)

    
    
def start_screen():
    screen.fill(BLACK)
    
    TITLE_text = tittle_font.render(TITLE, True, WHITE)
    rect = TITLE_text.get_rect()
    rect.centerx = WIDTH // 2 
    rect.bottom = HEIGHT // 2 - 15 
    screen.blit(TITLE_text, rect)

    
    sub_text = default_font.render("Press any key to start" , True, WHITE)
    rect = sub_text.get_rect()
    rect.centerx = WIDTH // 2 
    rect.top = HEIGHT // 2 + 15  
    screen.blit(sub_text, rect)

def end_screen():
    end_text = default_font.render("Game Over", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2 
    rect.centery = HEIGHT // 2  
    screen.blit(end_text, rect)
# Game loop
new_game()
start_level()
stage = START
running = True

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                stage = PLAYING
                pygame.mixer.music.load(main_theme)
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_SPACE:
            
                ship.shoot()
            elif stage == END:
                if event.key == pygame.k_r:
                    new_game()
                    start_level()
                    stage = START
                       
                

        
    if stage == PLAYING:
        pressed = pygame.key.get_pressed()


        if pressed [ pygame.K_LEFT]:
                ship.move_left()

        elif pressed[pygame.K_RIGHT]:
                ship.move_right()

    
    # Game logic
    if stage != START:
        lasers.update()
        enemies.update()
        bombs.update()
        player.update()
        powerups.update()

    if len(enemies) == 0:
        player.level += 1
        start_level()

    if len(player) == 0:
        stage = END
        pygame.mixer.music.stop()
    

     

        
    # Drawing code
    screen.fill(BLACK)
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    powerups.draw(screen)
    display_stats()

    if stage == START:

        start_screen()

    if stage == END:
        end_screen()
        
        
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

