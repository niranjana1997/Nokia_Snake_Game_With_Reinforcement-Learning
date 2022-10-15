from collections import namedtuple
import pygame as pg
from enum import Enum
import random as rand

pg.init()

# setting the font_face and size
font_style = pg.font.SysFont("cambria", 25)

# setting the values for each of the direction using Enum
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# colors defined
neon = (204, 255, 102)
dark_green = (0, 51, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# snake and its speed is set
snake_block = 20
speed = 15

Point = namedtuple('Point', 'x, y')

# created a class Nokia_Game
class Nokia_Game:
    # initializer has parameters width (default: 600) and height (default: 400)
    def __init__(self, width = 600, height = 400):
        # class fields
        self.width = width
        self.height = height
        # displays the window using the pygame library with width and height
        self.window = pg.display.set_mode((self.width, self.height))
        # title of the window is set
        pg.display.set_caption('Nokia Snake Game')
        self.clock = pg.time.Clock()
        
        # initial direction is set
        self.direction = Direction.RIGHT
        
        self.snake_head = Point(self.width // 2, self.height // 2)
        self.snake = [self.snake_head, 
                      Point(self.snake_head.x - snake_block, self.snake_head.y),
                      Point(self.snake_head.x - (2 * snake_block), self.snake_head.y)]
        # initial score is set to 0
        self.score = 0
        # initial value for the worm is set to None
        self.worm = None
        # insert worm method is called to set the x and y coordinates 
        self.insert_worm()
        
    def insert_worm(self):
        # worm's x and y coordiantes are set and assigns random values within the frame
        worm_x = rand.randint(0, (self.width - snake_block) // snake_block) * snake_block 
        worm_y = rand.randint(0, (self.height - snake_block) // snake_block) * snake_block
        self.worm = Point(worm_x, worm_y)
        # if the worm is inserted at the snake's position
        if self.worm in self.snake:
            # the insert_worm method is called again to insert the worm ata different position
            self.insert_worm()
        
    def play_game(self):
        # gets user input
        for event in pg.event.get():
            # checks if the event is quit, then pg.quit() and sys.exit() methods are called
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            # checks if any key is pressed down
            if event.type == pg.KEYDOWN:
                # checks if the key pressed is up arrow
                if event.key == pg.K_UP:
                    # value 3 is set to the variable direction
                    self.direction = Direction.UP
                # checks if the key pressed is down arrow
                elif event.key == pg.K_DOWN:
                    # value 4 is set to the variable direction
                    self.direction = Direction.DOWN
                # checks if the key pressed is left arrow
                elif event.key == pg.K_LEFT:
                    # value 1 is set to the variable direction
                    self.direction = Direction.LEFT
                # checks if the key pressed is right arrow
                elif event.key == pg.K_RIGHT:
                    # value 2 is set to the variable direction
                    self.direction = Direction.RIGHT
                
        
        # depending on the change in direction updated above, the direction of the snake is changed
        # by calling by the move_direction method
        # This updates the head
        self.move_direction(self.direction) 
        # the updated head is added to the snake
        self.snake.insert(0, self.snake_head)
        # game_over variable is set to False
        game_over = False
        # check if the game is over by calling the collision method
        if self.collision():
            # sets the game_over variable to True
            game_over = True
            # returns the game_over and score variable to the main method
            return game_over, self.score
            
        # if the head of the snake touches the worm
        if self.snake_head == self.worm:
            # score is incremented by 1
            self.score += 1
            # the worm is inserted elsewhere by calling the insert_worm method
            self.insert_worm()
        else:
            self.snake.pop()
        
        # updating interface by calling the method interface_update
        self.interface_update()
        # updating the clock speed 
        self.clock.tick(speed)
        # returning the values in game_over and score variable
        return game_over, self.score
    
    # checks if any collision has happened
    def collision(self):
        # if the head of the snake hits any of the boundaries, it will return a boolean value 'True'
        if (self.snake_head.x > self.width - snake_block) or (self.snake_head.x < 0) or (self.snake_head.y > self.height - snake_block) or (self.snake_head.y < 0):
            return True
        # if the head of the snake hit any part of itself, it will return a boolean value 'True'
        if self.snake_head in self.snake[1:]:
            return True
        # if it does not satisfy any of the above conditions, it will return a boolean value 'False'
        return False

    # function to display message in the frame
    def display_message(self, message, font_color, coordinates):
        # Text antialiasing (set to False) is a technique used to smooth the edges of text on a screen.
        message = font_style.render(message, False, font_color)
        # message at coordinates (0,0) is displayed
        self.window.blit(message, coordinates)


    def interface_update(self):
        # the background display is filled with neon color
        self.window.fill(neon)

        # snake is drawn in the window
        for eachPoint in self.snake:
            pg.draw.rect(self.window, dark_green, pg.Rect(eachPoint.x, eachPoint.y, snake_block, snake_block))
            pg.draw.rect(self.window, dark_green, pg.Rect(eachPoint.x+4, eachPoint.y+4, 12, 12))
        
        # worm's is drawn in the window with color and coordinates
        pg.draw.rect(self.window, red, pg.Rect(self.worm.x, self.worm.y, snake_block, snake_block))
        # score is updated by calling the method display_message
        self.display_message("Score: " + str(self.score), black, [0, 0])
        pg.display.flip()
        
    # this method is used to move the direction of the snake
    def move_direction(self, direction):
        # the x and y axis values are set
        x_axis = self.snake_head.x
        y_axis = self.snake_head.y
        # depending on the direction of the snake, x and y axis values are changed
        if direction == Direction.DOWN:
            y_axis += snake_block
        elif direction == Direction.UP:
            y_axis -= snake_block
        elif direction == Direction.RIGHT:
            x_axis += snake_block
        elif direction == Direction.LEFT:
            x_axis -= snake_block
        # the head value is updated
        self.snake_head = Point(x_axis, y_axis)
            

if __name__ == '__main__':
    # nokia_game is created with class Nokia_Game
    nokia_game = Nokia_Game()
    # this loop will run till the game_over variable is set to True
    while True:
        # values returned from the play_game method is stored in game_over and score
        game_over, score = nokia_game.play_game()
        # if the game is over
        if game_over:
            break
    # score is printed
    print('Score', score)  
    # the game window is closed
    pg.quit()