import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catcher 🍓")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)

# Basket setup
basket_width = 100
basket_height = 30
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 60
basket_speed = 10

# Fruit setup
fruit_radius = 20
fruit_x = random.randint(20, WIDTH - 20)
fruit_y = -fruit_radius
fruit_speed = 5

score = 0

def draw_basket(x, y):
    pygame.draw.rect(screen, BROWN, (x, y, basket_width, basket_height), border_radius=10)

def draw_fruit(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), fruit_radius)  # Red fruit

def show_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def reset_fruit():
    return random.randint(20, WIDTH - 20), -fruit_radius

# Game loop
running = True
while running:
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move fruit
    fruit_y += fruit_speed

    # Collision detection
    if (
        basket_y < fruit_y + fruit_radius < basket_y + basket_height and
        basket_x < fruit_x < basket_x + basket_width
    ):
        score += 1
        fruit_x, fruit_y = reset_fruit()

    # If fruit falls off screen
    if fruit_y > HEIGHT:
        score -= 1 if score > 0 else 0
        fruit_x, fruit_y = reset_fruit()

    # Draw elements
    draw_basket(basket_x, basket_y)
    draw_fruit(fruit_x, fruit_y)
    show_score(score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
