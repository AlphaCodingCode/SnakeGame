import pygame
import random

WIDTH = 661
HEIGHT = 661
FPS = 20

#set-up the game
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def drawGrid():
    #how many rows and columns do we want?
    #Well, how long do you want it to take for the snake to get from one side to the other?
    #probably around 3 seconds? If our snake travels 10 pixels every frame and our game is running at 20 frames per second,
    #then how many pixels across should our screen be? Well, if we want it to take three seconds, then 20 frames will elapse 3 times.
    # so, 3*20=60frames. That means we will need 60 columns and 60 rows. If each box of the snake is 10  by 10 pixels
    # that means we will need 10*60=600 pixels. + 61 pixels for each line = 661 pixels
    for i in range(0,61): #61 lines, starts at zero and stops when it hits 61
        pygame.draw.line(screen, WHITE, [(11*i),0], [(11*i), 660], 1)
        pygame.draw.line(screen, WHITE, [0,(11*i)], [660,(11*i)], 1)

    
class Food(pygame.sprite.Sprite):
    def __init__(self):
        #call the parent class's '__init__' function to make this object into a sprite
        #---------------------insert your code here--------------------

        #--------------------------------------------------------------

        #Create a 'surface', using pygame.suface([width,height]) function and save it under an 'image' value in the class
        #once you've done that, use pygame's 'surface.fill(aColor)' function to make the image you created a certain color.
        #---------------------insert your code here--------------------

        #--------------------------------------------------------------

       # Create a value for your class called 'rect' that you make equal to your image's rectangle using the surface.get_rect() function.
       #remember, your image is a surface. Having a property called 'rect' is important because pygame will search for it by default when it's
       #trying to print your sprite to the screen.
        #---------------------insert your code here--------------------

        #--------------------------------------------------------------

        #place in a random grid square. Remember, there are 60 rows and columns and each are spaced 11 pixels apart (to account for the line that seperates them)
        #You can use the function ransom.randint(lowerbound, upperBound) to generate a random number
        #Remember that you can use rect.x and rect.y to set your position
        #---------------------insert your code here--------------------

        #--------------------------------------------------------------
        
    def move(self):
        #place the food in a random grid square
        #-----------------insert your code here-----------------------------


        #-----------------------------------------------------------------
        
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

       #start in the top left corner
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
#Create a food object
#-----------------insert your code here-----------------------------

#-----------------------------------------------------------------

#Create a group to store my sprites
all_sprites = pygame.sprite.Group()
#add mySnake to the group of sprites
all_sprites.add(mySnake, '''add your food object here so that it gets drawn''')


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
    #re-draw the grid
    drawGrid()
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





