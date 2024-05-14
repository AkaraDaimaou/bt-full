import random
import sys
import os
print(os.getcwd())
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
flap_sound = pygame.mixer.Sound('wing.wav')
collision_sound = pygame.mixer.Sound('hit.wav')
score_sound = pygame.mixer.Sound('point.wav')
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
game_images['background'] = load_image('background.png')
game_images['flappydragon'] = load_image('bluebird.png')
game_images['pipeimage'] = (load_image('pipe_up.png'), load_image('pipe_bottom.png'))
game_images['sea_level'] = load_image('base.png')
game_images['scoreimages'] = [load_image(f'number_{i}.png') for i in range(10)]

# Placeholder for pipe creation logic
def createPipe():
    y_pos = random.randint(int(window_height * 0.3), int(window_height * 0.6))
    gap = 200  # Pipe gap
    pipe_height = game_images['pipeimage'][0].get_height()
    return [{'x': window_width, 'y': y_pos - pipe_height}, {'x': window_width, 'y': y_pos + gap}]

# Game over function
def game_over(your_score):
    print("Game Over! Your Score:", your_score)
    print("Press Enter to play again or Esc to exit")

# Update score function
def update_score(your_score, up_pipes, dragon_x):
    pipe_width = game_images['pipeimage'][0].get_width()
    for pipe in up_pipes:
        if pipe['x'] + pipe_width < dragon_x:
            your_score += 1
            score_sound.play()  # Play score sound effect
    return your_score

# Input handler
def handle_input():
    dragon_flapped = False
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            dragon_flapped = True
            flap_sound.play()
    return dragon_flapped

# Render game
def render_game(vertical, horizontal, up_pipes, down_pipes, your_score):
    window.blit(game_images['background'], (0, 0))
    for u_pipe, d_pipe in zip(up_pipes, down_pipes):
        window.blit(game_images['pipeimage'][0], (u_pipe['x'], u_pipe['y']))
        window.blit(game_images['pipeimage'][1], (d_pipe['x'], d_pipe['y']))
    window.blit(game_images['sea_level'], (0, window_height - game_images['sea_level'].get_height()))
    window.blit(game_images['flappydragon'], (horizontal, vertical))
    show_score(your_score)
    pygame.display.update()

# Show score
def show_score(your_score):
    score_digits = [int(x) for x in list(str(your_score))]
    total_width = 0  # total width of all numbers to be printed
    for digit in score_digits:
        total_width += game_images['scoreimages'][digit].get_width()
    X_offset = (window_width - total_width) / 2
    for digit in score_digits:
        window.blit(game_images['scoreimages'][digit], (X_offset, window_height * 0.1))
        X_offset += game_images['scoreimages'][digit].get_width()

# Show welcome screen
def show_welcome_screen():
    title_font = pygame.font.SysFont("Arial", 40)
    start_font = pygame.font.SysFont("Arial", 28)
    title_surf = title_font.render('Flappy Dragon Game', True, (255,255,255))
    start_surf = start_font.render('Press SPACE to start', True, (255,255,255))
    while True:
        window.blit(game_images['background'], (0, 0))
        window.blit(title_surf, (window_width / 2 - title_surf.get_width() / 2, window_height / 4))
        window.blit(start_surf, (window_width / 2 - start_surf.get_width() / 2, window_height / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
        framepersecond_clock.tick(framepersecond)

# Main game loop
def main():
    show_welcome_screen()
    # Initial game state...
    your_score = 0
    horizontal = int(window_width / 5)
    vertical = int(window_height / 2)
    ground = window_height - game_images['sea_level'].get_height()
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
    pipeVelX = -4
    dragon_velocity_y = -9
    dragon_Max_Vel_Y = 10
    dragon_Min_Vel_Y = -8
    dragonAccY = 1
    dragon_flap_velocity = -8
    dragon_flapped = False

    while True:
        dragon_flapped = handle_input()

        vertical += dragon_velocity_y
        dragon_velocity_y += dragonAccY if vertical < ground else 0
        vertical = min(vertical, ground)

        for u_pipe, d_pipe in zip(up_pipes, down_pipes):
            u_pipe['x'] += pipeVelX
            d_pipe['x'] += pipeVelX

        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            new_pipe = createPipe()
            up_pipes.append(new_pipe[0])
            down_pipes.append(new_pipe[1])
            up_pipes.pop(0)
            down_pipes.pop(0)

        if dragon_flapped:
            if vertical > 0:
                dragon_velocity_y = dragon_flap_velocity
            dragon_flapped = False

        your_score = update_score(your_score, up_pipes, horizontal)

        render_game(vertical, horizontal, up_pipes, down_pipes, your_score)

        # Check for collisions
        for u_pipe, d_pipe in zip(up_pipes, down_pipes):
            pipe_height = game_images['pipeimage'][0].get_height()
            if (vertical < u_pipe['y'] + pipe_height or vertical + game_images['flappydragon'].get_height() > d_pipe['y']) and horizontal + game_images['flappydragon'].get_width() > u_pipe['x'] and horizontal < u_pipe['x'] + game_images['pipeimage'][0].get_width():
                collision_sound.play()
                game_over(your_score)
                show_welcome_screen()

        framepersecond_clock.tick(framepersecond)

if __name__ == '__main__':
    main()
