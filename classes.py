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
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y += self.speed

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

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


class Bullet:
    color = (255, 255, 255)
    speed = 10

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