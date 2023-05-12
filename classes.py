import pygame
from pygame.locals import *

class Asteroid:

    def __init__(self, image_path, width, height, x, y, speed):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.health = 100
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y += self.speed

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw_health_bar(self, surface):
        bar_width = self.rect.width  # Anchura de la barra de vida igual al tamaño del asteroide
        bar_height = 5  # Altura de la barra de vida
        bar_x = self.rect.x  # Posición X de la barra de vida igual a la posición X del asteroide
        bar_y = self.rect.y + self.rect.width + 5  # Posición Y de la barra de vida debajo del asteroide

        # Calcula el porcentaje de vida actual del asteroide
        health_percentage = self.health / 100.0

        # Calcula la longitud del rectángulo de la barra de vida según el porcentaje de vida
        bar_length = int(bar_width * health_percentage)

        # Dibuja el fondo de la barra de vida (en rojo)
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))

        # Dibuja la parte llena de la barra de vida (en verde)
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_length, bar_height))

class Window:
    def __init__(self, width, height, caption, image_path):
        self.width = width
        self.height = height
        self.caption = caption
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load(image_path).convert()
        self.background_image = pygame.transform.scale(self.background, (self.width, self.height))
        pygame.display.set_caption(self.caption)

    def draw(self):
        pygame.display.update()

    def fill(self):
        self.surface.fill((255, 255, 255))

    def blit(self):            
        self.surface.blit(self.background_image, (0, 0))

    def draw(self, image, posx, posy):
        self.surface.blit(image, (posx, posy))

    def get_surface(self):
        return self.surface

class Starship:
    move_left = move_right = move_up = move_down = False
    speed = 10

    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.height -= 50
        self.rect.y = self.rect.y - self.rect.height / 2

    def draw(self, surface):
        # dibujar rectangulo rojo
        # pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
        surface.blit(self.image, self.rect.topleft)

    def keyboard_events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_d or event.key == K_RIGHT:
                self.move_right = True
                self.move_left = False
            if event.key == K_a or event.key == K_LEFT:
                self.move_left = True
                self.move_right = False
            if event.key == K_w or event.key == K_UP:
                self.move_up = True
                self.move_down = False
            if event.key == K_s or event.key == K_DOWN:
                self.move_down = True
                self.move_up = False                   


        if event.type == KEYUP:

            if event.key == K_d or event.key == K_RIGHT:
                self.move_right = False
            if event.key == K_a or event.key == K_LEFT:
                self.move_left = False
            if event.key == K_w or event.key == K_UP:
                self.move_up = False
            if event.key == K_s or event.key == K_DOWN:
                self.move_down = False
            if event.key == K_SPACE:
                pass

class Bullet:
    color = (255, 255, 255)
    speed = 13

    def __init__(self, x, y, number):
        self.number = number
        self.rect = pygame.Rect(0, 0, 10, 20)
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self):
        self.rect.y -= self.speed

    def __str__(self):
        return f"Bullet number {self.number}"