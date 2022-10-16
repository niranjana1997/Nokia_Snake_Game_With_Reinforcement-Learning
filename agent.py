# PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.
import torch
# this library is used to import stack 
from collections import deque
# importing the snake_game module
from snake_game import Nokia_Game, Direction, Point
import matplotlib.pyplot as plt
import numpy as np

MAX_MEM = 100_000
SIZE_BATCH = 1000
LEARNING_RATE = 0.001

MAX_MEM = 100_000
SIZE_BATCH = 1000
LEARNING_RATE = 0.001

# class Agent
class Agent:
     # initializer
    def __init__(self):
        # number of games parameter
        self.num_games = 0
        # randomness parameter
        self.randomness = 0 
        # discount rate
        self.discount_rate = 0.9 
        # if stack exceeds memory, it removes elements from the left
        self.memory = deque(maxlen = MAX_MEM)

    # method remember 
    # inputs: reward, state, action, new_state, game_over
    def remember(self, state, reward, action, new_state, game_over):
        pass

    # method remember 
    # inputs: state, new_state, action , reward, game_over
    def remember(self, state, new_state, action, reward, game_over):
        self.memory.append((state, action, reward, new_state, game_over))

    # method to get the state
    # keeps track of the current environment
    def get_state(self, nokia_game):
        # head is retrieved from the snake variable in nokia_game class
        snake_head = nokia_game.snake[0]
        # point tuples are created in all directions to check if there is any imminent collision 
        left_point = Point(snake_head.x - 20, snake_head.y)
        right_point = Point(snake_head.x + 20, snake_head.y)
        up_point = Point(snake_head.x, snake_head.y - 20)
        down_point = Point(snake_head.x, snake_head.y + 20)
        
        # current direction is a boolean value
        # it checks the current game direction
        # only one of the four values will be True
        current_direction_left = nokia_game.direction == Direction.LEFT
        current_direction_right = nokia_game.direction == Direction.RIGHT
        current_direction_up = nokia_game.direction == Direction.UP
        current_direction_down = nokia_game.direction == Direction.DOWN

        # state has 11 values
        # [danger straight, danger right, danger left, 
        # direction_left, direction_right, direction_up, direction_down
        # worm_left, worm_right, worm_up, worm_down]
        state = [
            # checks if the danger is straight or ahead using the above initialized values
            # this is dependent on current direction
            (current_direction_right and nokia_game.collision(right_point)) or 
            (current_direction_left and nokia_game.collision(left_point)) or 
            (current_direction_up and nokia_game.collision(up_point)) or 
            (current_direction_down and nokia_game.collision(down_point)),

            # checks if the danger is to the right of the current direction
            # This is done using the above initialized values
            # This is dependent on current direction
            (current_direction_up and nokia_game.collision(right_point)) or 
            (current_direction_down and nokia_game.collision(left_point)) or 
            (current_direction_left and nokia_game.collision(up_point)) or 
            (current_direction_right and nokia_game.collision(down_point)),

            # checks if the danger is to the left of the current direction
            # This is done using the above initialized values
            # This is dependent on current direction
            (current_direction_down and nokia_game.collision(right_point)) or 
            (current_direction_up and nokia_game.collision(left_point)) or 
            (current_direction_right and nokia_game.collision(up_point)) or 
            (current_direction_left and nokia_game.collision(down_point)),
            
            # current move direction (only on of the four values are true)
            current_direction_left,
            current_direction_right,
            current_direction_up,
            current_direction_down,
            
            # worm location 
            # worm is to the left of the snake
            nokia_game.worm.x < nokia_game.snake_head.x, 
            # worm is to the right of the snake
            nokia_game.worm.x > nokia_game.snake_head.x,  
            # worm is to the up of the snake
            nokia_game.worm.y < nokia_game.snake_head.y, 
            # worm is to the down of the snake
            nokia_game.worm.y > nokia_game.snake_head.y 
            ]
        # this array is converted to numpy array of type int and returned
        return np.array(state, dtype=int)


    # method get_action
    # get action based on the state
    def get_action(self, state):
        pass

    def long_memory_train(self):
        pass

    def short_memory_train(self):
        pass

def train_model():
    # keeps track of scores to plot
    score_graph = []
    # mean of the score to plot 
    mean_score_graph = []
    # keeps track of the total score
    score_sum = 0
    # keeps track of the best score
    best_score = 0
    #  creating a agent object
    agent = Agent()
    # creating a Nokia_Game object
    nokia_game = Nokia_Game()
    # training loop
    while True:
        # getting current state by calling the get_state method
        current_state = agent.get_state(nokia_game)
        # getting move based on current state
        move = agent.get_action(current_state)
        # this move is used to play the game
        # the values obtained from the move is used to get a new state
        reward, game_over, score = nokia_game.play_game(move)
        new_state = agent.get_state(nokia_game)
        # to train short memory - 
        agent.short_memory_train(current_state, move, reward, new_state, game_over)
        # to remember the current situation
        agent.remember(current_state, new_state, move, reward, game_over)

        # if the game is over
        if game_over:
            # initializes game and resets everything 
            nokia_game.reset_game()
            # increments the num_games by 1 at the start of new game
            agent.num_games += 1
            # to train long memory - replay memory or experienced replay
            # it trains on all previous moves and games. Temendously improves the model
            agent.long_memory_train()

            # updates best_score if there is a new high score
            if score > best_score:
                best_score = score

            # printing all the paramters
            print('Game', agent.num_games, 'Score', score, 'Best Score:', best_score)

            # the current score is added to the list of scores to plot in the graph
            score_graph.append(score)
            # current score is added to total score_sum 
            score_sum += score
            # mean score is calculated
            mean_score = score_sum / agent.num_games
            # mean score is appended to the list
            mean_score_graph.append(mean_score)

    # method remember 
    # inputs: state, new_state, action , reward, game_over
    def remember(self, state, new_state, action, reward, game_over):
        # these variables are passed to the memory stack
        # if the stack if full, it will pop the element to the left
        self.memory.append((state, action, reward, new_state, game_over))


if __name__ == '__main__':
    train_model()
