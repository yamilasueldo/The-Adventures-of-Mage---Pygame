import pygame
from Clases.class_object import Object
from Clases.class_projectile import Projectile
#from Clases.Niveles.Nivel_uno import *
from configuraciones import *
from constantes_pygame import *

class Personage(Object):
    def __init__(self, animations: list, current_animation: str, position: tuple, speed):
        super().__init__(animations, current_animation, position)

        #MOVIMIENTO
        self.displacement_y = 0
        self.displacement_x = 0

        #GRAVEDAD
        self.speed = speed
        self.gravity = GRAVITY
        self.jump_power = JUMP_POWER
        self.is_flying = True

        if self.current_animation == 'idle_r':
            self.right_direction = True
        elif self.current_animation == 'idle_l':
            self.right_direction = False
        
        self.is_colliding = False # ESTA COLISIONANDO ?
        self.lives = 3
        self.remaining_shots = 100
        self.step_counter = 0
        self.shots_counter = 0
        self.got_hurt = False #RECIBIO UN TIRO ?
        self.take_shot = False #LANZO UN TIRO ?

        self.projectiles = []
        
        #SONIDOS
        self.sound_projectil = pygame.mixer.Sound("Recursos\Sonidos\Projectil.mp3")
        self.sound_projectil.set_volume(1)

        self.sound_projectil_colliding = pygame.mixer.Sound("Recursos\Sonidos\Projectil_colliding.wav")
        self.sound_projectil_colliding.set_volume(1)

        self.sound_personage_hurt = pygame.mixer.Sound("Recursos\Sonidos\Personage_hurt.mp3")
        self.sound_personage_hurt.set_volume(1)

    def move(self):
        for side in self.sides:
            self.sides[side].x += self.displacement_x * self.speed
    
    def jump(self):
        self.displacement_y = self.jump_power
        self.is_flying = True
    
    def take_life(self):
        if not self.got_hurt:
            self.lives -= 1
            self.sound_personage_hurt.play()
            self.got_hurt = True
        elif self.step_counter > 5:
            self.step_counter = 0
            self.got_hurt = False
        else:
            self.step_counter += 1

    def apply_gravity(self, screen):
        self.salta(screen)
        self.displacement_y += self.gravity
        self.is_flying = True
        for side in self.sides:
            self.sides[side].y += self.displacement_y

    def check_collision_platforms_h(self, platforms:list):
        self.move()
        self.is_colliding = False
        for platform in platforms:
            if self.sides['main'].colliderect(platform.sides['main']):
                self.is_colliding = True
                if self.displacement_x < 0: #SE ESTA MOVIENDO A LA IZQ
                    self.sides['main'].left = platform.sides['main'].right
                    self.sides = get_rects(self.sides['main'])
                elif self.displacement_x > 0: # SE ESTA MOVIENDO A LA DER
                    self.sides['main'].right = platform.sides['main'].left
                    self.sides = get_rects(self.sides['main'])

    def check_collision_platforms_v(self, screen, platforms:list):
        self.apply_gravity(screen)
        for platform in platforms:
            if self.sides['main'].colliderect(platform.sides['main']):
                if self.displacement_y > 0: #ESTA BAJANDO
                    self.sides['main'].bottom = platform.sides['main'].top
                    self.sides = get_rects(self.sides['main'])
                    self.displacement_y = 0
                    self.is_flying = False
                elif self.displacement_y < 0: #ESTA SUBIENDO
                    self.sides['main'].top = platform.sides['main'].bottom
                    self.sides = get_rects(self.sides['main'])
                    self.displacement_y = 0
            #    self.sides = get_rects(self.sides['main'])

    def change_rect(self, animation:str):
        new_rect = self.animations[animation][0].get_rect()
        new_rect.x = self.rect.x
        new_rect.y = self.rect.y
        self.rect = new_rect
        self.sides = get_rects(self.rect)

    #ANIMAR ACCIONES
    def throw_projectile(self):
        if self.right_direction:
            pos_x = self.sides['right'].x + 10
            speed = 8
            animation = "projectile_player_r"
        else: 
            pos_x = self.sides['left'].x - 40
            speed = - 8
            animation = "projectile_player_l"
        pos_y = self.sides['bottom'].y - 31
        projectile = Projectile(dic_projectiles, animation, (pos_x,pos_y), speed)
        self.projectiles.append(projectile)

    def salta(self, screen):
        if self.is_flying:
            if self.right_direction:
                animation = "jump_r"
            else:
                animation = "jump_l"
            self.change_rect(animation) #rectangulo (para que cuando salte tenga el rectangulo de quieto y eliminar el bug de que queda trabado)
            self.draw(screen, animation)
    


    def walk_r(self, screen):
        if not self.is_flying:
            self.change_rect('walk_r')
            self.draw(screen, 'walk_r')
    
    def walk_l(self, screen):
        if not self.is_flying:
            self.change_rect('walk_l')
            self.draw(screen, 'walk_l')

    def idle(self, screen):
        if not self.is_flying:
            if self.right_direction:
                animation = "idle_r"
            else:
                animation = "idle_l"
            self.change_rect(animation)
            self.draw(screen, animation)

    def throw(self, screen):
        if not self.is_flying:
            if self.right_direction:
                animation = "throw_r"

            else:
                animation = "throw_l"
            self.change_rect(animation)
            self.draw(screen, animation)
    
    def attack(self, screen):
        if not self.is_flying:
            if self.right_direction:
                animation = "attack_r"
            else:
                animation = "attack_l"
            self.change_rect(animation)
            self.draw(screen,animation)
    
    def draw_animations(self, screen):
        match self.current_animation:
            case 'walk_r':
                self.walk_r(screen)
            case'walk_l':
                self.walk_l(screen)
            case 'idle':
                self.idle(screen)
            case 'jump':
                self.salta(screen)
            case 'throw':
                self.throw(screen)
                if self.take_shot == False:
                    self.throw_projectile()
                    self.sound_projectil.play()
                    self.remaining_shots = -1
                    self.take_shot = True
                elif self.shots_counter < 5:
                    self.shots_counter += 1
                else:
                    self.shots_counter = 0
                    self.take_shot = False
            case 'attack':
                self.attack(screen)
                self.sound_projectil_colliding.play()

    def update(self, screen, platforms:list):
        self.check_collision_platforms_h(platforms)
        self.check_collision_platforms_v(screen,platforms)
        self.draw_animations(screen)           
