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

# Load game sounds
# Add sound effects for dragon flapping, collisions, and scoring
flap_sound = pygame.mixer.Sound("flap_sound.wav")
collision_sound = pygame.mixer.Sound("collision_sound.wav")
score_sound = pygame.mixer.Sound("score_sound.wav")

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
game_images['background'] = load_image("background.jpg")
game_images['flappydragon'] = load_image('flappydragon.png')
game_images['pipeimage'] = (load_image('pipe_top.png'), load_image('pipe_bottom.png'))
game_images['sea_level'] = load_image('ground.png')
game_images['scoreimages'] = [load_image(f'number_{i}.png') for i in range(10)]

# Placeholder for pipe creation logic
def createPipe():
    y_pos = random.randint(int(window_height * 0.3), int(window_height * 0.6))
    gap = 200  # Pipe gap
    pipe_height = game_images['pipeimage'][0].get_height()
    return [{'x': window_width, 'y': y_pos - pipe_height}, {'x': window_width, 'y': y_pos + gap}]

# Define functions for different aspects of the game
# Implement game over screen
def game_over(your_score):
    print("Game Over! Your Score:", your_score)
    # Add code to display game over screen and handle user input for options

# Update score function
def update_score(your_score, up_pipes, dragon_x):
    pipe_width = game_images['pipeimage'][0].get_width()
    for pipe in up_pipes:
        if pipe['x'] + pipe_width < dragon_x:
            your_score += 1
            score_sound.play()  # Play score sound effect
    return your_score

# Main game loop
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
        flap = handle_input()  # Get flap action from user input
        
        if handle_collisions(horizontal, vertical, up_pipes, down_pipes, ground):
            collision_sound.play()  # Play collision sound effect
            game_over(your_score)

        vertical, dragon_velocity_y, your_score = update_game_state(vertical, dragon_velocity_y, dragonAccY, dragon_flapped, horizontal, pipeVelX, up_pipes, down_pipes, your_score, flap)

        render_game(vertical, horizontal, up_pipes, down_pipes, your_score)

        framepersecond_clock.tick(framepersecond)

if __name__ == '__main__':
    main()
