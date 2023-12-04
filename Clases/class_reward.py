import pygame
from Clases.class_item import Item

class Reward(Item):
    def __init__(self, animations: list, current_animation: str, position: tuple):
        super().__init__(animations, current_animation, position)

        self.sound_coin = pygame.mixer.Sound("Recursos\Sonidos\Coin.mp3")
        self.sound_coin.set_volume(1)

        self.sound_heart = pygame.mixer.Sound("Recursos\Sonidos\Heart.mp3")
        self.sound_heart.set_volume(1)

        self.sound_dynamite = pygame.mixer.Sound("Recursos\Sonidos\Dynamite.mp3")
        self.sound_dynamite.set_volume(1)

    def apply(self, player):
        if self.current_animation == 'coin':
            self.sound_coin.play()
            player.collected_coins += 1
        elif self.current_animation == 'heart':
            self.sound_heart.play()
            player.lives += 1
        elif self.current_animation == 'dynamite':
            self.sound_dynamite.play()
            player.remaining_shots += 1

