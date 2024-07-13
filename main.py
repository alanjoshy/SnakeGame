import pygame
import random

# pygame setup
pygame.init()
square_width = 1100
pixel_width = 50
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def generate_starting_position():
    x_position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    y_position_range = (pixel_width // 2, screen_height - pixel_width // 2, pixel_width)
    return [random.randrange(*x_position_range), random.randrange(*y_position_range)]

def reset():
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return [snake_pixel.copy()]

def is_out_of_bounds():
    return (snake_pixel.bottom > screen_height or snake_pixel.top < 0 or 
            snake_pixel.left < 0 or snake_pixel.right > screen_width)

# playground

# snake
snake_pixel = pygame.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

# target 
target = pygame.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if is_out_of_bounds():
        snake = reset()
        snake_length = 1

    if snake_pixel.center == target.center:
        target.center = generate_starting_position()
        snake_length += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, -pixel_width)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_LEFT]:
        snake_direction = (-pixel_width, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (pixel_width, 0)

    snake_pixel.move_ip(snake_direction)

    # Ensure the snake list is updated with the correct length
    snake.append(snake_pixel.copy())
    if len(snake) > snake_length:
        del snake[0]

    # RENDER YOUR GAME HERE
    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 10

pygame.quit()
