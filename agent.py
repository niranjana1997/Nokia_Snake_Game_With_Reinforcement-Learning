# optimized tensor library for deep learning using gpus and cpus
import torch as tc
import random as rand
import numpy as np
from game import Nokia_Game, Direction, Point
# Queue data structure is imported
from collections import deque

# Image and video datasets and models for torch deep learning

MAX_MEM = 100_000
SIZE_BATCH = 1000
LEARNING_RATE = 0.001

# class Agent
class Agent:
    # initializer
    def __init__(self):
        pass

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, new_state, game_over):
        pass

    def long_mem_train(self):
        pass

    def short_mem_train(self):
        pass

    def get_action(self, state):
        pass

def training():
    pass

if __name__ == "main":
    training()

