import pygame
from Clases.class_personage import Personage
from Clases.class_reward import Reward

class Player(Personage):
    def __init__(self, animations: list, current_animation: str, position: tuple, speed):
        super().__init__(animations, current_animation, position, speed)

        self.collected_coins = 0
        self.lives = 3
        self.remaining_shots = 4
        self.murders = 0

        # self.sound_personage_hurt = pygame.mixer.Sound("Recursos\Sonidos\Personage_hurt.mp3")
        # self.sound_personage_hurt.set_volume(1)

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.current_animation = "walk_r"
            self.displacement_x = 1
            self.right_direction = True
        elif keys[pygame.K_LEFT]:
            self.current_animation = "walk_l"
            self.displacement_x = -1
            self.right_direction = False
        else:
            self.current_animation = "idle"
            self.displacement_x = 0

        if keys[pygame.K_SPACE]:
            if self.is_flying == False:
                self.current_animation = "jump"
                self.jump()
        if keys[pygame.K_f]:
            if self.remaining_shots > 0:
                self.current_animation = "throw"
        if keys[pygame.K_g]:
            self.current_animation = "attack"

    def check_collision_items(self, items):
        for item in items:
            if self.sides['main'].colliderect(item.sides['main']):
                item.apply(self)
                if isinstance(item, Reward):
                    items.remove(item)
        return items

    def attack_enemies(self, enemies):
        if self.current_animation == 'attack':
            for enemy in enemies:
                if self.right_direction:
                    if self.sides["right"].colliderect(enemy.sides["main"]):
                            enemy.displacement_y = -7
                            enemy.take_life()
                    else:
                        if self.sides["left"].colliderect(enemy.sides["main"]):
                            enemy.displacement_y = -7
                            enemy.take_life()
    
    #RECIBIR DAÑO
    def take_damage(self, enemies):
        for enemy in enemies:
            if enemy.current_animation == 'attack':
                if enemy.right_direction:
                    if enemy.sides["right"].colliderect(self.sides["main"]):
                        self.displacement_y = -7
                        self.take_life()
                    else:
                        if enemy.sides["left"].colliderect(self.sides["main"]):
                            self.displacement_y = -7
                            self.take_life()
    
    def update(self, screen, platforms:list, enemies:list, items:list):
        self.events()
        self.attack_enemies(enemies)
        self.check_collision_items(items)
        self.take_damage(enemies)
        return super().update(screen,platforms)
        
