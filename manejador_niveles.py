import pygame
from Clases.Niveles.Level_One import LevelOne
from Clases.Niveles.Level_Two import LevelTwo
from Clases.Niveles.Level_Three import LevelThree

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {'level_one': LevelOne,'level_two': LevelTwo, 'level_three': LevelThree} 
    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)