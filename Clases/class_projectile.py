import pygame
from Clases.class_item import Item
from configuraciones import * 

class Projectile(Item):
    def __init__(self, animations: list, current_animation: str, position: tuple,speed):
        super().__init__(animations, current_animation, position)
        self.speed = speed

        self.sound_personage_hurt = pygame.mixer.Sound("Recursos\Sonidos\Personage_hurt.mp3")
        self.sound_personage_hurt.set_volume(1)

    def move(self):
        for side in self.sides:
            self.sides[side].x += self.speed
    
    def apply(self, personage):
        personage.lives -= 1
        personage.displacement_y = -7
        self.sound_personage_hurt.play()
    
    def check_goal(self, pitcher, receiver, platforms):
        for platform in platforms:
            if platform.sides['main'].colliderect(self.sides['main']):
                pitcher.projectiles.remove(self)
                break  # Termina el bucle si se encuentra una plataforma
        else:  # Este bloque se ejecuta si el bucle for termina sin un break
            for personage in (receiver if isinstance(receiver, list) else [receiver]):
                if personage.sides['main'].colliderect(self.sides['main']):
                    self.apply(personage)
                    try:
                        pitcher.projectiles.remove(self)
                    except:
                        print(f"No se pudo remover el proyectil")
        return pitcher.projectiles

    def update(self, screen, pitcher, receiver, platforms):
        self.move()
        self.check_goal(pitcher,receiver,platforms)
        return super().update(screen)
