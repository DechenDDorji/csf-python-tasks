import pygame
import random

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_SPEED = 1.5
PADDLE_SPEED = 3
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

background = pygame.image.load("images/background.png")
left_paddle = pygame.image.load("images/left_paddle.png")
right_paddle = pygame.image.load("images/right_paddle.png")
ball = pygame.image.load("images/ball.png")

paddle_collider_width = left_paddle.get_width()
paddle_collider_height = left_paddle.get_height()
ball_collider_width = ball.get_width()
ball_collider_height = ball.get_height()

paddle_width = paddle_collider_width
paddle_height = paddle_collider_height
ball_width = ball_collider_width
ball_x = SCREEN_WIDTH // 2 - ball_width // 2
ball_y = SCREEN_HEIGHT // 2 - ball_width // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED
left_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2
right_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2

left_score = 0
right_score = 0

font = pygame.font.Font(None, 36)
left_score_text = font.render(f"Left: {left_score}", True, WHITE)
right_score_text = font.render(f"Right: {right_score}", True, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < SCREEN_HEIGHT - paddle_height:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < SCREEN_HEIGHT - paddle_height:
        right_paddle_y += PADDLE_SPEED

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - ball_width:
        ball_dy = -ball_dy

    if ball_x <= 0 and left_paddle_y < ball_y < left_paddle_y + paddle_height:
        ball_dx = -ball_dx
    elif ball_x >= SCREEN_WIDTH - ball_width and right_paddle_y < ball_y < right_paddle_y + paddle_height:
        ball_dx = -ball_dx
    elif ball_x < 0:
        right_score += 1
        ball_x = SCREEN_WIDTH // 2 - ball_width // 2
        ball_y = SCREEN_HEIGHT // 2 - ball_width // 2
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED

    elif ball_x > SCREEN_WIDTH:
        left_score += 1
        ball_x = SCREEN_WIDTH // 2 - ball_width // 2
        ball_y = SCREEN_HEIGHT // 2 - ball_width // 2
        ball_dx = -BALL_SPEED
        ball_dy = BALL_SPEED

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    screen.blit(left_paddle, (0, left_paddle_y))
    screen.blit(right_paddle, (SCREEN_WIDTH - paddle_width, right_paddle_y))
    screen.blit(ball, (ball_x, ball_y))

    left_score_text = font.render(f"Left: {left_score}", True, WHITE)
    right_score_text = font.render(f"Right: {right_score}", True, WHITE)

    screen.blit(left_score_text, (20, 20))
    screen.blit(right_score_text, (SCREEN_WIDTH - 160, 20))

    pygame.display.update()

pygame.quit()