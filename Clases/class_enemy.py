import pygame
from Clases.class_personage import Personage
import random

class Enemy(Personage):
    def __init__(self, animations: list, current_animation: str, position: tuple, speed, can_move:bool, can_jump:bool, can_throw:bool, can_attack:bool):
        super().__init__(animations, current_animation, position, speed)
        self.displacement_x = 0
        self.behavior = 0
        self.behavior_count = 0
        self.has_direction = False
        self.lives = 2
        self.can_move = can_move
        self.can_jump = can_jump
        self.can_throw = can_throw
        self.can_attack = can_attack

    def generate_random_direction(self):
        if self.has_direction == False:
            self.displacement_x = random.choice([1, -1])
            self.has_direction = True

    #generar comportamiento aleatorio cada cierto tiempo
    def generate_random_behavior_time(self, seconds):
        time = seconds * 30
        self.behavior_count += 1
        if self.behavior_count > time:
            self.behavior = random.choice([1,2,3])
            self.behavior_count = 0

    def do_behavior(self):
        if self.displacement_x == 1:
            self.current_animation = "walk_r"
            self.right_direction = True
            if self.is_colliding == True:
                self.displacement_x = -1
                self.is_colliding == False
            self.generate_random_behavior_time(2)

        elif self.displacement_x == -1:
            self.current_animation = "walk_l"
            self.right_direction = False
            if self.is_colliding == True:
                self.displacement_x = 1
                self.is_colliding == False
            self.generate_random_behavior_time(2)

        else:
            self.current_animation = "idle"
            self.behavior_count += 1
            if self.can_move:
                if self.behavior_count > 60:
                    self.behavior_count = 0
                    self.generate_random_direction()
            self.generate_random_behavior_time(2)

        if self.behavior == 1:
            if self.can_jump:
                if not self.is_flying and not self.is_colliding:
                    self.current_animation = "jump"
                    self.jump()
                self.behavior = 0
            else:
                self.behavior = 0

        elif self.behavior == 2:
            if self.can_throw:
                if not self.is_flying and not self.is_colliding:
                    self.current_animation = "throw"
                    if self.behavior_count > 45:
                        self.behavior_count = 0
                        self.behavior = 0
                    else:
                        self.behavior_count += 1
            else:
                self.behavior = 0
            
        elif self.behavior == 3:
            if self.can_attack:
                if not self.is_flying and not self.is_colliding:
                    self.current_animation = "ataca"
                    self.behavior_count += 1
                    if self.behavior_count > 60:
                        self.behavior_count = 0
                        self.behavior = 0
            else:
                self.behavior = 0


    def update(self, screen, platforms: list):
        self.do_behavior()
        return super().update(screen, platforms)