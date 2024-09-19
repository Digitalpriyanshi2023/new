import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Dodger")

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Load images
player_img = pygame.Surface((50, 30))
player_img.fill(WHITE)

asteroid_img = pygame.Surface((50, 50))
asteroid_img.fill(RED)

# Player settings
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 50
player_speed = 5

# Asteroid settings
asteroid_speed = 5
asteroids = []

def spawn_asteroid():
    x = random.randint(0, SCREEN_WIDTH - 50)
    y = -50
    asteroids.append(pygame.Rect(x, y, 50, 50))

def draw_asteroids():
    for asteroid in asteroids:
        screen.blit(asteroid_img, asteroid.topleft)

def update_asteroids():
    global asteroids
    for asteroid in asteroids:
        asteroid.y += asteroid_speed
    asteroids = [a for a in asteroids if a.y < SCREEN_HEIGHT]

def check_collision():
    player_rect = pygame.Rect(player_x, player_y, 50, 30)
    for asteroid in asteroids:
        if player_rect.colliderect(asteroid):
            return True
    return False

def game_over():
    print("Game Over")
    pygame.quit()
    quit()

# Game loop
running = True
spawn_timer = pygame.time.get_ticks()
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    # Spawn new asteroids
    if pygame.time.get_ticks() - spawn_timer > 1000:
        spawn_asteroid()
        spawn_timer = pygame.time.get_ticks()
    
    # Update and draw asteroids
    update_asteroids()
    draw_asteroids()
    
    # Draw the player
    screen.blit(player_img, (player_x, player_y))
    
    # Check for collisions
    if check_collision():
        game_over()
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
