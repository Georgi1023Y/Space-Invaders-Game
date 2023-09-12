import pygame
import sys
import time
import random

# Initializing Pygame
pygame.init()

# Global Variables
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 8
BULLET_SPEED = 10
ALIEN_SPEED = 2
ALIEN_DROP = 20
BLAST_SPEED = 5
# Sets blast interval in mileseconds
BLAST_INTERVAL = 500
blast_timer = 1
score = 0
alien_score = 10

# Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Background image loading and resizing
background_image = pygame.image.load("images/casey-horner-RmoWqDCqN2E-unsplash.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Rocket image loading and resizing
rocket_image = pygame.image.load("images/rocket-147466_1280.png")
rocket_image = pygame.transform.scale(rocket_image, (40, 80))

# Loads the alien image
alien_image = pygame.image.load("images/ufo-svgrepo-com.png")

# Resizes the alien image
alien_width = 50 
alien_height = 50  
alien_image = pygame.transform.scale(alien_image, (alien_width, alien_height))

# Blast image loading and resizing
blast_image = pygame.image.load("images/bullet-svgrepo-com.png")
blast_image = pygame.transform.scale(blast_image, (20, 20))

# Player creation
player_rect = rocket_image.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# Create a font for displaying the score
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
game_over = False

# Creating aliens list
aliens = []

# Creating blasts list
blasts = []

# Creating multiple rows of aliens
num_rows = 3
num_aliens_per_row = 13
alien_spacing_x = 10

# Creating multiple alien instances with different positions 
# Creates 3 rows
for row in range(num_rows):
    # Creates 13 columns
    for col in range(num_aliens_per_row):
        alien_rect = alien_image.get_rect()
        # This adjusts the x and y positions based on row and column
        alien_rect.x = col * (alien_width + alien_spacing_x)
        # It adds vertical spacing
        alien_rect.y = row * (alien_height + 10) + 50  
        # Adds allien_rect to the list of all aliens
        aliens.append(alien_rect)


# Main game functionality 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    
    # Automatically fire blasts based on the blast interval
    current_time = pygame.time.get_ticks()
    if current_time - blast_timer > BLAST_INTERVAL:
        blast = blast_image.get_rect()
        blast.centerx = player_rect.centerx  # Set blast's x-coordinate to the center of the rocket
        blast.centery = player_rect.top
        blasts.append(blast)
        blast_timer = current_time
          
    
    # Updates the blast positions and removes blasts at the top of the screen
    blasts = [blast for blast in blasts if blast.y > 0]

    # Showing the background image 
    screen.blit(background_image, (0, 0))

    # Showing the aliens
    for alien_rect in aliens:
        screen.blit(alien_image, alien_rect)

    # Showing the rocket image
    screen.blit(rocket_image, player_rect)

    # Showing the blasts on the screen
    for blast in blasts:
        blast.y -= BLAST_SPEED
        screen.blit(blast_image, blast)
    
    # Checks for collisions between blasts and aliens
    for blast in blasts:
        for alien_rect in aliens:
            if blast.colliderect(alien_rect):
                blasts.remove(blast)
                score += alien_score  # Increase the score when an alien is hit
                aliens.remove((alien_rect))
    
    # Displays the total score on the screen
    total_score_text = font.render("Total Score: " + str(score), True, (255, 255, 255))
    screen.blit(total_score_text, (10, 10))   
        
    # Refreshes the screen
    pygame.display.flip()
 
    clock.tick(60)


# Exits from the game
pygame.quit()
sys.exit()

