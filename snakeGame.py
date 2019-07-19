import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#set-up the game
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("my Game")
clock = pygame.time.Clock()

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) #this function is defined in the parent class which is inherited...

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       self.speedx = 8
       self.speedy = 0
        
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

       self.rect.x = WIDTH/2
       self.rect.y = HEIGHT/2

    
    def update(self):
        
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.speedy = 0
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.speedy = 0
        if keystate[pygame.K_UP]:
            self.speedx = 0
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedx = 0
            self.speedy = 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
        
#create my own snake
mySnake = Snake(GREEN, 50, 50)

#Create a group to store my sprites
all_sprites = pygame.sprite.Group()
#add mySnake to the group of sprites
all_sprites.add(mySnake)


running = True
while running:
    # Process input (events)

    #remember, pygame.event.get() returns to us a list of events that have piled up while the program was running.
    #That means we have to go through the line and pick out each event to check if they're a quit event.
    #If they are, we have to close the window. If none of the events are a quit event, then keep going in the program.
    for event in pygame.event.get(): 
    # check for closing window
        if event.type == pygame.QUIT:
            running = False
    
    # Update Sprites
    all_sprites.update()
    
    # Render (draw)

    #Clear the previous Sprites drawn
    screen.fill(BLACK)
    #draw the new Sprites
    all_sprites.draw(screen)

    
    #flip the 'white board' so that the computer starts to read what we wrote
    #while we write on the side that the computer has already read(double-buffering).
    pygame.display.flip()


    # Wait until 1/30 seconds has elapsed to give our eyes a chance to see the change
    # before moving on (30FPS = 1Frame every 1/30seconds)
    clock.tick(FPS)

#if We've broken out of the loop, that means that 'Running' is false, which meanse
#we should close the program.

pygame.quit()





