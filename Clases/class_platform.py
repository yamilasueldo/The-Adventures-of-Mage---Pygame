import pygame
from Clases.class_object import Object

class Platform(Object):
    def __init__(self, animations: list, current_animation: str, position: tuple):
        super().__init__(animations, current_animation, position)
