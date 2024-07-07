import pygame
import sys
import os
import random

# Constants
width = 600
height = 800
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
dark_gray = (100, 100, 100)
clock = pygame.time.Clock()
g = 1
score = 0
fps = 13
fruits = ['watermelon', 'orange']

# Initialize Pygame
pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fruit Ninja')
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 32)
button_font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 36)

# Load images from 'images' folder
image_path = os.path.join(os.getcwd(), 'images')

background_image = pygame.image.load(os.path.join(image_path, 'wall.jpeg'))
background_image = pygame.transform.scale(background_image, (width, height))
title_image = pygame.image.load(os.path.join(image_path, 'title.png'))

# Function to generate random fruits
def generate_random_fruits(fruit):
    path = os.path.join(image_path, fruit + '.png')
    data[fruit] = {
        'img': pygame.image.load(path),
        'x': random.randint(100, 500),
        'y': 800,
        'speed_x': random.randint(-10, 10),
        'speed_y': random.randint(-80, -60),
        'throw': False,
        't': 0,
        'hit': False,
    }
    if random.random() >= 0.75:
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

# Initial fruit generation
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

# Function to draw the home page
def draw_home_page(mouse_pos):
    gameDisplay.blit(background_image, (0, 0))
    gameDisplay.blit(title_image, (width // 2 - title_image.get_width() // 2, height // 20))  # Move the title image higher

    start_button = pygame.Rect(width // 2 - 100, height // 2 + -10, 200, 50)  # Move the button lower
    if start_button.collidepoint(mouse_pos):
        pygame.draw.rect(gameDisplay, light_gray, start_button)
    else:
        pygame.draw.rect(gameDisplay, gray, start_button)
    pygame.draw.rect(gameDisplay, black, start_button, 2)

    start_text = button_font.render('Start Game', True, black)
    gameDisplay.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, start_button.y + (start_button.height - start_text.get_height()) // 2))
    
    return start_button

# Main loop
in_home_page = True

while True:
    mouse_pos = pygame.mouse.get_pos()
    if in_home_page:
        start_button = draw_home_page(mouse_pos)
    else:
        gameDisplay.blit(background_image, (0, 0))

        # Draw header
        pygame.draw.rect(gameDisplay, gray, (0, 0, width, 100))
        score_text = font.render(f'Score: {score}', True, black)
        gameDisplay.blit(score_text, (10, 25))

        # Draw fruits
        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']
                value['y'] += value['speed_y']
                value['speed_y'] += g * value['t']
                value['t'] += 1

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))
                else:
                    generate_random_fruits(key)

                current_position = pygame.mouse.get_pos()
                if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60 and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                    path = os.path.join(image_path, 'half_' + key + '.png')
                    value['img'] = pygame.image.load(path)
                    value['speed_x'] += 10
                    score += 1
                    value['hit'] = True
            else:
                generate_random_fruits(key)

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and in_home_page:
            if start_button.collidepoint(event.pos):
                in_home_page = False