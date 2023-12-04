import pygame
from Clases.class_enemy import Enemy
from configuraciones import *
from Clases.class_projectile import Projectile
class Boss(Enemy):
    def __init__(self, animations: list, current_animation: str, position: tuple, speed, can_move: bool, can_jump: bool, can_throw: bool, can_attack: bool):
        super().__init__(animations, current_animation, position, speed, can_move, can_jump, can_throw, can_attack)

        self.lives = 3


    def throw_projectile(self):
        if self.right_direction:
            pos_x = self.sides["right"].x + 10
            speed = 10
            animation = "projectile_boss_r"
        else:
            pos_x = self.sides["left"].x - 40
            speed = -10
            animation = "projectile_boss_l"
        pos_y = self.sides["bottom"].y - 50
        projectile = Projectile(dic_projectiles, animation, (pos_x, pos_y), speed)
        self.projectiles.append(projectile)
    
    def throw(self, screen):
        if not self.is_flying:
            if self.right_direction:
                animation = "throw_r"
            else:
                animation = "throw_l"
            self.change_rect(animation)
            self.draw(screen, animation)

    def attack(self, screen):
        if self.is_flying == False:
            if self.right_direction:
                animation = "attack_r"
            else:
                animation = "attack_l"
            self.change_rect(animation)
            self.draw_animations(screen, animation)

    def update(self, screen, platforms:list):
        self.check_collision_platforms_h(platforms)
        self.check_collision_platforms_v(screen, platforms)
        self.draw_animations(screen)
        self.do_behavior()
