import pygame
import random

WIDTH = 661
HEIGHT = 680
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
        
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
      font = pygame.font.Font(font_name, size)
      text_surface = font.render(text, True, WHITE)
      text_rect = text_surface.get_rect()
      text_rect.midtop = (x, y)
      surf.blit(text_surface, text_rect)
    
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #this function is defined in the parent class which is inherited...
        
        #The block image will always be red
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)

       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        #place it at a random location
        self.rect.x = random.randint(0,59) * 11 + 1;
        self.rect.y = random.randint(0,59) * 11 + 1;
    #use the default update method

    def move(self):
        #move the food to another location
        self.rect.x = random.randint(0,59) * 11 + 1;
        self.rect.y = random.randint(0,59) * 11 + 1;
        
        
class SnakeBlock(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block, it's dimensions,
    #whether or not it's the snake's head and the snake block that is in front of it
    #'head' is meant to be a boolean datatype, meaning it can only be True or False
    #prevSnakeBlock is meant to be a SnakeBlock class object.
    def __init__(self, color, width, height, head, prevSnakeBlock): 
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) #this function is defined in the parent class which is inherited...

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       #keep track of whether or not the block is the head of the snake
       self.head = head 

       #initialize the speed of the snake
       #if we're creating the snake's head, that means the game is just starting, so set the speed to 0
       #if we're creating the snake's body, that means it's speed is determined by the snakeBlock that is in front of it
       #-----------insert your code here ------------------------------




       

       #---------------------------------------------------------------
        
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

        #set the snake's position
       #if it's the head, we'll start in the top left corner
       #if it's the body, we'll start 1 grid-square behind the snakeBlock in front
       #-----------insert your code here ------------------------------




       

       #---------------------------------------------------------------
    def update(self, prevSnakeBlock):
        
        keystate = pygame.key.get_pressed()

        
        #Update the speed of the snake.
        #if the snakeBlock is the snake's head, then it's controlled by the player's
        #key touches (same as last step). If it's the body then it's determined
        #by the speed of the snakeBlock in front of it.
        #-----------insert your code here ------------------------------




       

       #---------------------------------------------------------------
            
        #regardless of whether the snakeblock is the head or not,
        #we want to move it by the amount specified by its speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
        
#create the snake head
snakeHead = SnakeBlock(GREEN, 10, 10, True, None)
#create a peice of food
food = Food() #will automatically be put in a random location
#create a score-keeping device
score = 0
#create an array that will store all of the snake blocks.
#initialize it with only the head
mySnake = [snakeHead]

#Create a group to store my sprites
all_sprites = pygame.sprite.Group()
#add mySnake and the food to the group of sprites
all_sprites.add(snakeHead, food)


running = True
while running:
    
    # Process input (events)
######################################################################################
    #remember, pygame.event.get() returns to us a list of events that have piled up while the program was running.
    #That means we have to go through the line and pick out each event to check if they're a quit event.
    #If they are, we have to close the window. If none of the events are a quit event, then keep going in the program.
    for event in pygame.event.get(): 
    # check for closing window
        if event.type == pygame.QUIT:
            running = False
######################################################################################


    #update the Snake position and speed
#################################################################################################

    #update the position and speed of the snake body.
    #Note that the snake body is indexed in the
    #array from element snake[1] to element snake[len(snake)-1].
    #note that if an array is of size 6, then the last element is actually indexed as array[5].
    #notice that the i variable is decreasing by 1 every time, as shown by the last '-1' parameter
    #notice that the for loop last executes when i=1, which is the block right before the head
    
    for i in range((len(mySnake)-1), 0, -1):
          #-----insert your code here ------------

          #---------------------------------------
        
    #update the speed and position of the snake's head
    mySnake[0].update(None) #we give it none because the head doesen't have a previous block
####################################################################################################


    #check for collision of the head with food to manage scoring system and snake length
    #remember that collisions only happen with the head of the snake.
##############################################
    if mySnake[0].rect.colliderect(food.rect):
        #manage scoring system
        score += 1
        food.move()
        
        #increase the snake length by adding a body block
        #make sure you pass in the right parameters when you call the snake's constructor class
        newBlock = '''insert your code here''' 
        all_sprites.add(newBlock)#make sure you add it to the sprites that we draw to the screen
        mySnake.append(newBlock)#add the new snakeBlock to the mySnake array
################################################
    

    
    # Render (draw)
#################################################
    #Clear the previous Sprites drawn
    screen.fill(BLACK)
    #re-draw the grid
    drawGrid()
    #draw the new Sprites
    all_sprites.draw(screen)
    #draw the score remember, draw_text(surf, text, size, x, y)
    draw_text(screen, "Score: " + str(score), 18, 35, 662)
#####################################################
    
    #flip the 'white board' so that the computer starts to read what we wrote
    #while we write on the side that the computer has already read(double-buffering).
    pygame.display.flip()

    # Wait until 1/30 seconds has elapsed to give our eyes a chance to see the change
    # before moving on (30FPS = 1Frame every 1/30seconds)
    clock.tick(FPS)


#if We've broken out of the loop, that means that 'Running' is false, which meanse
#we should close the program.

pygame.quit()





