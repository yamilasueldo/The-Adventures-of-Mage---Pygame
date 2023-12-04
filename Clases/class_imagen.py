import pygame
from constantes_pygame import *

class Imagen:
    def __init__(self, path, width, height, x, y, screen):
        self.path = path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.screen = screen
    
    def cargar_imagen(self):
        surf = pygame.image.load(self.path).convert_alpha()
        surf = pygame.transform.scale(surf, (self.width, self.height))
        return surf

    def animar_imagen(self, lista_imaganes):
        for imagen in lista_imaganes:
            self.screen.blit(imagen, self.width, self.height)