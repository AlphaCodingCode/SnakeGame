import pygame
import random

WIDTH = 661
HEIGHT = 661
FPS = 20

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

def drawGrid():
    for i in range(0,61): #61 lines, starts at zero and stops when it hits 61
        pygame.draw.line(screen, WHITE, [(11*i),0], [(11*i), 660], 1) #vertical lines
        pygame.draw.line(screen, WHITE, [0,(11*i)], [660,(11*i)], 1) #horizontal lines
    #Here is how we figured out how many rows and columns we wanted if you were curious:
    #Well, how long do you want it to take for the snake to get from one side to the other?
    #probably around 3 seconds? If our snake travels 10 pixels every frame and our game is running at 20 frames per second,
    #then how many pixels across should our screen be? Well, if we want it to take three seconds, then 20 frames will elapse 3 times.
    # so, 3*20=60frames. That means we will need 60 columns and 60 rows. If each box of the snake is 10  by 10 pixels
    # that means we will need 10*60=600 pixels. + 61 pixels for each line = 661 pixels



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

        #initialize the speed of the snake
       self.speedx = 0
       self.speedy = 0
        
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

       self.rect.x = 1
       self.rect.y = 1

    
    def update(self):
        
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_RIGHT]:
            if(self.speedx >= 0):
                self.speedx = 11
                self.speedy = 0
        if keystate[pygame.K_LEFT]:
            if(self.speedx <= 0):
                self.speedx = -11
                self.speedy = 0
        if keystate[pygame.K_UP]:
            if(self.speedy <= 0):
                self.speedx = 0
                self.speedy = -11
        if keystate[pygame.K_DOWN]:
            if(self.speedy >= 0):
                self.speedx = 0
                self.speedy = 11

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
        
#create my own snake
mySnake = Snake(GREEN, 10, 10)

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
    drawGrid()

    
    #flip the 'white board' so that the computer starts to read what we wrote
    #while we write on the side that the computer has already read(double-buffering).
    pygame.display.flip()


    # Wait until 1/30 seconds has elapsed to give our eyes a chance to see the change
    # before moving on (30FPS = 1Frame every 1/30seconds)
    clock.tick(FPS)

#if We've broken out of the loop, that means that 'Running' is false, which meanse
#we should close the program.

pygame.quit()





