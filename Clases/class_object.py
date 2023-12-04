import pygame
from configuraciones import get_rects

class Object():
    def __init__(self, animations:list, current_animation:str, position:tuple):
        #ANIMACIONES
        self.pos_fotogram = 0
        self.current_animation = current_animation
        self.animations = animations

        #RECTANGULOS
        self.rect = self.animations[current_animation][0].get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.sides = get_rects(self.rect)

    def draw(self, screen, current_animation):
        animation = self.animations[current_animation]
        if self.pos_fotogram >= len(animation):
            self.pos_fotogram = 0
        screen.blit(animation[self.pos_fotogram],self.sides['main'])
        self.pos_fotogram +=1

    def update(self,screen):
        self.draw(screen,self.current_animation)