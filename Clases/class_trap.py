import pygame
from Clases.class_item import Item

class Trap(Item):
    def __init__(self, animations: list, current_animation: str, position: tuple):
        super().__init__(animations, current_animation, position)

        self.sound_personage_hurt = pygame.mixer.Sound("Recursos\Sonidos\Personage_hurt.mp3")
        self.sound_personage_hurt.set_volume(1)

    def apply(self, player):
        player.lives -= 1
        player.displacement_y = -7
        self.sound_personage_hurt.play()

