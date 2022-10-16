# Nokia Snake Game with Reinforcement Learning
Snake – First published by Nokia, for monochrome phones. It was programmed in 1997 by Taneli Armanto of Nokia and introduced on the Nokia 6110.

![image](https://user-images.githubusercontent.com/89472841/196009178-180e840e-9fd8-40ae-bb36-620bbfc0db94.png)

This project is about implementing the reinforcement learning algorithm Deep Q-Learning on the Nokia's Snake Game to predict the actions. It makes use of the Python's Pygame and Pytorch libraries. 

## Installation
### Virtual Environment
A virtual environemnt is created and activated by running the following commands: 
1. conda create -n pygame_env python=3.7
2. conda activate pygame_env
### Other Installations
The following commands are used to install pygame, torch and matplotlib:
1. pip install pygame
2. pip install torch torchvision
3. pip install matplotlib ipython
## Working of the Application:
1. Rule of the Game: Snake should not hit the boundaries and itself.
2. Process:
    1. Initially, snake knows nothing about the game. It is only aware of the environment and tries to make more or less random moves.
    2. With each move and game, it tries to learn more.
    3. In this project, after about 80 game iterations (around 10 minutes), it knows how to play better through improvement.
## Output of the Application

https://user-images.githubusercontent.com/89472841/196058472-82e5d625-cacc-4bdd-9ecd-016948910de1.mov

Output at Iteration 100:

<img width="1244" alt="Screen Shot 2022-10-16 at 5 09 34 PM" src="https://user-images.githubusercontent.com/89472841/196058493-626f0cd8-4734-41f2-b2ac-f1e7f6d1577b.png">

