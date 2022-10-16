# PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.
import torch
# this library is used to import stack 
from collections import deque
# importing the snake_game module
from snake_game import Nokia_Game, Direction, Point

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

    # method to get the state
    # keeps track of the current environment
    def get_state(self, snake_game):
        pass

    # method get_action
    # get action based on the state
    def get_action(self, state):
        pass

    def long_memory_train(self):
        pass

    def short_memory_train(self):
        pass

def train_model():
    pass

if __name__ == "main":
    train_model()
