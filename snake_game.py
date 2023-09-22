import pygame
from pygame.locals import *
import random

pygame.init()
red = (255, 0, 0)
blue = (51, 153, 255)
gray = (192, 192, 192)
green = (51, 102, 0)
yellow = (255, 255, 0)

x = 800
y = 640
screen = pygame.display.set_mode((x, y))

pygame.display.set_caption("Snake Game")

snake = 10
snake_speed = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 32)
score_font = pygame.font.SysFont('comicsansms', 32)

def user_score(score):
    number = score_font.render("Score: " + str(score), True, red)
    screen.blit(number, [0, 0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake, snake])

def message(msg):
    msg = font.render(msg, True, red)
    screen.blit(msg, [x / 6, y / 3])

def game_loop():
    gameOver = False
    gameClose = False

    x1 = x / 2
    y1 = y / 2
    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, x - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, y - snake) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            screen.fill(gray)
            message("You lost!! Press P to Play again and Q to quit the game")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake
        if x1 > x or x1 < 0 or y1 > y or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(gray)
        pygame.draw.rect(screen, yellow, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, x - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, y - snake) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

game_loop()
