import random
import sys
import os
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
window_width = 600
window_height = 499
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Dragon Game')

# Game constants
elevation = window_height * 0.8
framepersecond = 32
framepersecond_clock = pygame.time.Clock()

# Image loading helper function
def load_image(image_path):
    if not os.path.isfile(image_path):
        print(f'Image file {image_path} does not exist')
        sys.exit(1)
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f'Unable to load image {image_path}: {e}')
        sys.exit(1)
    return image


# Load game images
game_images = {}
game_images['background'] = load_image("C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/Background.jpg")
game_images['flappydragon'] = load_image('C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/Bird1-1.png')
game_images['pipeimage'] = (load_image('C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/castle_top.png'), load_image('C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/castle_bottom.png'))
game_images['sea_level'] = load_image('C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/ground.png')
game_images['scoreimages'] = [load_image(f'C:/Users/Veerb/Documents/GitHub/bt-full/week4/day5/first hackthon/images/place1.png') for i in range(10)]


# Placeholder for pipe creation logic
def createPipe():
    y_pos = random.randint(int(window_height * 0.3), int(window_height * 0.6))
    gap = 200  # Pipe gap
    pipe_height = game_images['pipeimage'][0].get_height()
    return [{'x': window_width, 'y': y_pos - pipe_height}, {'x': window_width, 'y': y_pos + gap}]

# Define functions for different aspects of the game
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

def update_game_state(vertical, dragon_velocity_y, dragonAccY, dragon_flapped, horizontal, pipeVelX, up_pipes, down_pipes, your_score):
    # Dragon movement
    if dragon_velocity_y < dragon_Max_Vel_Y and not dragon_flapped:
        dragon_velocity_y += dragonAccY

    if dragon_flapped:
        dragon_flapped = False

    vertical += dragon_velocity_y
    vertical = max(0, min(vertical, elevation - game_images['flappydragon'].get_height()))

    # Move pipes
    for pipes in (up_pipes, down_pipes):
        for pipe in pipes:
            pipe['x'] += pipeVelX

    # Add new pipes
    if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
        new_pipe = createPipe()
        up_pipes.append(new_pipe[0])
        down_pipes.append(new_pipe[1])
        up_pipes.pop(0)
        down_pipes.pop(0)

    # Update score
    your_score = update_score(your_score, up_pipes, horizontal)

    return vertical, dragon_velocity_y, your_score

def render_game(vertical, horizontal, up_pipes, down_pipes, your_score):
    # Render everything
    window.blit(game_images['background'], (0, 0))
    for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
        window.blit(game_images['pipeimage'][0], (upperPipe['x'], upperPipe['y']))
        window.blit(game_images['pipeimage'][1], (lowerPipe['x'], lowerPipe['y']))

    window.blit(game_images['sea_level'], (0, elevation))
    window.blit(game_images['flappydragon'], (horizontal, vertical))

    # Score display
    score_digits = [int(x) for x in list(str(your_score))]
    total_width = sum(game_images['scoreimages'][digit].get_width() for digit in score_digits)
    Xoffset = (window_width - total_width) / 2

    for digit in score_digits:
        window.blit(game_images['scoreimages'][digit], (Xoffset, window_height * 0.1))
        Xoffset += game_images['scoreimages'][digit].get_width()

    pygame.display.update()  # Update the display

def handle_collisions(horizontal, vertical, up_pipes, down_pipes, ground):
    dragon_width = game_images['flappydragon'].get_width()
    dragon_height = game_images['flappydragon'].get_height()

    # Check collision with ground
    if vertical + dragon_height >= ground:
        return True

    # Check collision with pipes
    for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
        pipe_width = game_images['pipeimage'][0].get_width()
        pipe_height = game_images['pipeimage'][0].get_height()

        if horizontal + dragon_width >= upperPipe['x'] and horizontal <= upperPipe['x'] + pipe_width:
            if vertical <= upperPipe['y'] + pipe_height or vertical + dragon_height >= lowerPipe['y']:
                return True

    return False

def play_sound_effects():
    # Add code to play sound effects and background music here
    pass

def increase_difficulty(pipeVelX):
    # Add code to increase difficulty here
    pass

def track_high_score():
    # Add code to track and update high score here
    pass

def game_over(your_score):
    # Add code for game over screen here
    print("Game Over! Your Score:", your_score)
    pygame.quit()
    sys.exit()

def update_score(your_score, up_pipes, dragon_x):
    pipe_width = game_images['pipeimage'][0].get_width()
    for pipe in up_pipes:
        if pipe['x'] + pipe_width < dragon_x:
            your_score += 1
    return your_score

def main():
    # Initial game state
    your_score = 0
    horizontal = int(window_width / 5)
    vertical = int(window_height / 2)
    ground = window_height - game_images['sea_level'].get_height()

    # Pipe positions
    first_pipe = createPipe()
    second_pipe = createPipe()

    down_pipes = [
        {'x': window_width + 200, 'y': first_pipe[1]['y']},
        {'x': window_width + 200 + (window_width / 2), 'y': second_pipe[1]['y']},
    ]

    up_pipes = [
        {'x': window_width + 200, 'y': first_pipe[0]['y']},
        {'x': window_width + 200 + (window_width / 2), 'y': second_pipe[0]['y']},
    ]

    # Dragon physics
    global dragon_Max_Vel_Y, dragonAccY, dragon_flap_velocity
    pipeVelX = -4
    dragon_velocity_y = -9
    dragon_Max_Vel_Y = 10
    dragon_Min_Vel_Y = -8
    dragonAccY = 1
    dragon_flap_velocity = -8
    dragon_flapped = False

    while True:
        handle_input()
        
        if handle_collisions(horizontal, vertical, up_pipes, down_pipes, ground):
            game_over(your_score)

        vertical, dragon_velocity_y, your_score = update_game_state(vertical, dragon_velocity_y, dragonAccY, dragon_flapped, horizontal, pipeVelX, up_pipes, down_pipes, your_score)

        render_game(vertical, horizontal, up_pipes, down_pipes, your_score)

        framepersecond_clock.tick(framepersecond)

if __name__ == '__main__':
    main()
