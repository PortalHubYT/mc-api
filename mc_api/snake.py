from mcapy_lib import *

import sys
import time
import random

start_time = time.time()


mc_height = 70
WIDTH,  HEIGHT = 50, 50
grid = [[0 for j in range(HEIGHT)] for i in range(WIDTH)]

# def init_snake
snake = [(10, 1), (2, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)]
food = (10, 10)
direction = 0

def new_food():
    global food
    food = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# game_speed 
# game_tick



def remove_tail():
    rem = snake.pop()

    setblock(Coordinates(rem[0], mc_height, rem[1]), Block("white_wool"))
    

def draw_food():    
    setblock(Coordinates(food[0], mc_height, food[1]), Block("black_wool"))
    



def get_direction():
    # vec = (mc.player.getTilePos())
    pos = (vec.x, vec.y, vec.z)
    global direction
    if pos[0] < WIDTH / 4 and direction != 2:
        direction = 3
    elif pos[0] > 3 * (WIDTH/4) and direction != 3:
        direction = 2
    elif pos[2] < HEIGHT / 4 and direction != 0:
        direction = 1
    elif pos[2] > 3 * (HEIGHT/4) and direction != 1:
        direction = 0
    print(direction)
    # mc.postToChat(f"{pos}, {direction}")
    

def move_snake():
    head = snake[0]
    print(direction)
    if direction == 0:
        new = (head[0], head[1] + 1)
    elif direction == 1:
        new = (head[0], head[1] - 1)
    elif direction == 2:
        new = (head[0] + 1, head[1])
    elif direction == 3:
        new = (head[0] - 1, head[1])
    
    
    if new[0] >= WIDTH:
        new = (0, new[1])
    elif new[0] < 0:
        new = (WIDTH - 1, new[1])
    
    if new[1] >= HEIGHT:
        new = (new[0], 0)
    elif new[1] < 0:
        new = (new[0], HEIGHT - 1)
    
    if new == food:
        new_food()
    else:
        remove_tail()
        
    snake.insert(0, new)
    setblock(Coordinates(new[0], mc_height, new[1]), Block("black_wool"))

def draw_snake():
    for x, y in snake:
        print(x, y)
        setblock(Coordinates(x, mc_height, y), Block("black_wool"))

def minecraft_draw_grid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            setblock(Coordinates(x, mc_height, y), Block("white_wool"))
            
    

    
def set_pixel(x, y, n):
    grid[x][y] = n


def render():
    time.sleep(0.03)

    
    
    # get_direction()
    move_snake()
    draw_food()


for y in range(HEIGHT):
    for x in range(WIDTH):
        set_pixel(x, y, 0)
            

minecraft_draw_grid()
draw_snake()
while True:
    render()

        
