import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dashing Race")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 90
car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_img.fill(BLUE)

# Enemy car settings
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 90
enemy_img = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
enemy_img.fill(RED)

# Road lines
LINE_WIDTH, LINE_HEIGHT = 10, 60

# Fonts
font = pygame.font.SysFont(None, 36)

# Game variables
def main():
    clock = pygame.time.Clock()
    car_x = WIDTH // 2 - CAR_WIDTH // 2
    car_y = HEIGHT - CAR_HEIGHT - 10
    car_speed = 7
    enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
    enemy_y = -ENEMY_HEIGHT
    enemy_speed = 6
    score = 0
    lines = [i * 150 for i in range(5)]
    running = True
    game_over = False

    while running:
        screen.fill(GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT] and car_x > 0:
                car_x -= car_speed
            if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
                car_x += car_speed

            # Move enemy
            enemy_y += enemy_speed
            if enemy_y > HEIGHT:
                enemy_y = -ENEMY_HEIGHT
                enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
                score += 1
                enemy_speed += 0.2  # Increase difficulty

            # Collision detection
            car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)
            if car_rect.colliderect(enemy_rect):
                game_over = True

            # Draw road lines
            for i in range(len(lines)):
                lines[i] += enemy_speed
                if lines[i] > HEIGHT:
                    lines[i] = -LINE_HEIGHT
                pygame.draw.rect(screen, WHITE, (WIDTH//2 - LINE_WIDTH//2, lines[i], LINE_WIDTH, LINE_HEIGHT))

            # Draw car and enemy
            screen.blit(car_img, (car_x, car_y))
            screen.blit(enemy_img, (enemy_x, enemy_y))

            # Draw score
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))
        else:
            over_text = font.render("Game Over!", True, RED)
            screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 40))
            score_text = font.render(f"Final Score: {score}", True, BLACK)
            screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
            restart_text = font.render("Press R to Restart", True, BLUE)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 40))
            if keys[pygame.K_r]:
                main()
                return

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
