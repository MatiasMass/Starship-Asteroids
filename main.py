import random
import pygame
from pygame.locals import *
from classes import *
from functions import *

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    # font 
    font = pygame.font.SysFont(None, 48)

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Window
    background_image = "images/background.jpg"
    window = Window(600, 700, "Starship vs Asteroids", background_image)


    asteroid_image = "images/asteroid.png"

    window.fill()
    draw_text("Starship vs Asteroids", font, window.get_surface(), 150, window.height / 3, BLACK)
    draw_text("Press 1, 2 or 3 to choose a starship", font, window.get_surface(), 20, window.height / 2, BLACK)

    pygame.display.update()
    
    starship_chose = choose_starship()



    starship_image = f"images/starship{starship_chose}.png"

    # Game loop
    while True:
        game_over_bool = False

        # Starship
        starship = Starship(starship_image, window.width / 2 , window.height - 150)

        # Bullets
        bullets = []

        # Asteroids
        asteroids = []

        for i in range(20):
                random_height = random.randint(50, 100)
                random_width = random.randint(50, 100)
                random_x = random.randint(0, window.width)
                random_y = random.randint(-window.height, 0)
                random_speed = random.randint(1, 5)

                asteroid = Asteroid(asteroid_image, random_width, random_height, random_x, random_y, random_speed)
                asteroids.append(asteroid)

        while not game_over_bool:

        
            # Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == K_d or event.key == K_RIGHT:
                        starship.move_right = True
                        starship.move_left = False
                    if event.key == K_a or event.key == K_LEFT:
                        starship.move_left = True
                        starship.move_right = False
                    if event.key == K_w or event.key == K_UP:
                        starship.move_up = True
                        starship.move_down = False
                    if event.key == K_s or event.key == K_DOWN:
                        starship.move_down = True
                        starship.move_up = False                   
                    if event.key == K_SPACE:
                        bullet_1 = Bullet(starship.rect.left, starship.rect.top + 10, 1)
                        bullet_2 = Bullet(starship.rect.right - 10, starship.rect.top, 2)
                        bullets.append(bullet_1)
                        bullets.append(bullet_2)


                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_d or event.key == K_RIGHT:
                        starship.move_right = False
                    if event.key == K_a or event.key == K_LEFT:
                        starship.move_left = False
                    if event.key == K_w or event.key == K_UP:
                        starship.move_up = False
                    if event.key == K_s or event.key == K_DOWN:
                        starship.move_down = False
                    if event.key == K_SPACE:
                        pass

            # Move starship
            if starship.move_right and starship.rect.right < window.width:
                starship.rect.move_ip(starship.speed, 0)
            if starship.move_left and starship.rect.left > 0:
                starship.rect.move_ip(-starship.speed, 0)
            if starship.move_up and starship.rect.top > 0:
                starship.rect.move_ip(0, -starship.speed)
            if starship.move_down and starship.rect.bottom < window.height:
                starship.rect.move_ip(0, starship.speed)


            # Update
            window.blit()
            
            # Draw
            starship.draw(window.get_surface())
            
            if len(asteroids) != 0:
                for asteroid in asteroids[::]:
                    asteroid.draw(window.get_surface())
                    asteroid.move()
                    if asteroid.rect.top > window.height:
                        asteroids.remove(asteroid)
                        continue

                    if asteroid.rect.colliderect(starship.rect):
                        game_over_bool = True
                        break
            else:
                for i in range(20):
                    random_height = random.randint(50, 100)
                    random_width = random.randint(50, 100)
                    random_x = random.randint(0, window.width)
                    random_y = random.randint(-window.height, 0)
                    random_speed = random.randint(1, 5)

                    asteroid = Asteroid(asteroid_image, random_width, random_height, random_x, random_y, random_speed)
                    asteroids.append(asteroid)
            
            for bullet in bullets[::]:
                bullet.rect.move_ip(0, -bullet.speed)
                bullet.draw(window.get_surface())

                for asteroid in asteroids[::]:
                    if bullet.rect.colliderect(asteroid.rect):
                        asteroids.remove(asteroid)
                        bullets.remove(bullet)
                        break

                if bullet.rect.bottom < 0:
                    if bullet in bullets:  # Verificar si el objeto aún está en la lista
                        bullets.remove(bullet)
                    continue


            pygame.display.update()

            # Clock
            pygame.time.Clock().tick(60)

        # Game over
        draw_text("Game Over", font, window.get_surface(), window.width / 2 - 100, window.height / 2 - 100, WHITE)
        draw_text("Press any key to play again", font, window.get_surface(), 100, window.height / 2 + 50, WHITE)

        pygame.display.update()
        wait()