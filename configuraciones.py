import pygame
from constantes_pygame import *
import random
#from Clases.class_moneda import Moneda

#para el enemigo
def calcular_largo_plataformas(lista_plataformas):
    largo = 0
    for plataforma in lista_plataformas:
        largo += plataforma.lados['main'].x
    return largo 


def obtener_animaciones(path_parcial,cantidad,w,h,girar = False):#
    lista_imagenes = []
    i = 1
    for i in range(cantidad):
        path = path_parcial + str(i) + ".png"
        imagen = pygame.image.load(path)
        imagen = pygame.transform.scale(imagen,(w,h))
        if girar :
            imagen =  pygame.transform.flip(imagen, True, False)
        lista_imagenes.append(imagen)
    return lista_imagenes


def reescalar_imagenes(lista_imagenes, tamaño):
        for imagen in range(len(lista_imagenes)):
            lista_imagenes[imagen] = pygame.transform.scale(lista_imagenes[imagen], tamaño)

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def get_rects(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario


#PLAYER
dic_player = {
    "idle_r": obtener_animaciones("Recursos\Personages\Mage\Idle\idle",14,60,60),
    "idle_l": obtener_animaciones("Recursos\Personages\Mage\Idle\idle",14,60,60),
    "walk_r": obtener_animaciones("Recursos\Personages\Mage\Walk\Walk",6,60,60), #path cantidad w h flip
    "walk_l":obtener_animaciones("Recursos\Personages\Mage\Walk\Walk",6,60,60,True),
    "jump_r": obtener_animaciones("Recursos\Personages\Mage\Jump\Jump",7,60,60),
    "jump_l": obtener_animaciones("Recursos\Personages\Mage\Jump\Jump",7,60,60,True),
    "throw_r": obtener_animaciones("Recursos/Personages/Mage/Throw/throw",7,60,60),
    "throw_l": obtener_animaciones("Recursos/Personages/Mage/Throw/throw",7,60,60, True),
    "attack_r": obtener_animaciones("Recursos\Personages\Mage\Push\Push",4,60,60),
    "attack_l": obtener_animaciones("Recursos\Personages\Mage\Push\Push",4,60,60,True)
    }


dic_enemy = {
    "idle_r": obtener_animaciones("Recursos\Personages\Enemy\Idle\idle",13,40,40),
    "idle_l": obtener_animaciones("Recursos\Personages\Enemy\Idle\idle",13,40,40,True),
    "walk_r": obtener_animaciones("Recursos\Personages\Enemy\Walk\walk",15,40,40),
    "walk_l": obtener_animaciones("Recursos\Personages\Enemy\Walk\walk",15,40,40,True),
    'jump_r': obtener_animaciones("Recursos\Personages\Enemy\Jump\Jump",6,40,40),
    'jump_l': obtener_animaciones("Recursos\Personages\Enemy\Jump\Jump",6,40,40,True),
    'throw_r': obtener_animaciones("Recursos\Personages\Enemy\Throw\Throw",12,40,40),
    'throw_l': obtener_animaciones("Recursos\Personages\Enemy\Throw\Throw",12,40,40,True),
    'attack_r': obtener_animaciones("Recursos/Personages/Enemy/Attack/attack",12,40,40),
    'attack_l': obtener_animaciones("Recursos/Personages/Enemy/Attack/attack",12,40,40,True)
}

dic_enemy_boss = {
    "idle_r": obtener_animaciones("Recursos\Personages\Knight\Idle\idle",12 ,60,60),
    "idle_l": obtener_animaciones("Recursos\Personages\Knight\Idle\idle",12 ,60,60,True),
    "walk_r":obtener_animaciones("Recursos\Personages\Knight\Walk\walk",6,60,60),
    "walk_l": obtener_animaciones("Recursos\Personages\Knight\Walk\walk",6,60,60,True),
    "jump_r": obtener_animaciones("Recursos\Personages\Knight\Jump\jump",7,60,60),
    "jump_l" : obtener_animaciones("Recursos\Personages\Knight\Jump\jump",7,30,30,True),
    "throw_r" : obtener_animaciones("Recursos\Personages\Knight\Throw\Throw",6,30,30),
    'throw_l': obtener_animaciones("Recursos\Personages\Knight\Throw\Throw",6,30,30,True),
    'attack_r': obtener_animaciones("Recursos/Personages/Knight/Attack/attack",5,60,60),
    'attack_l': obtener_animaciones("Recursos/Personages/Knight/Attack/attack",5,60,60,True)
}




# #ANIMACIONES JUGADOR


#PLATFORMS
stone_platform = [pygame.image.load("Recursos\Platforms\Platform0.png")]
grass_platform = [pygame.image.load("Recursos\Platforms\Platform1.png")]

reescalar_imagenes(stone_platform, (40,40))
reescalar_imagenes(grass_platform, (40,40))

dic_platforms = {"grass": grass_platform, 'stone': stone_platform}

#REWARDS
coin_reward = obtener_animaciones("Recursos\Items\moneda",6,20,20)
heart_reward = obtener_animaciones("Recursos\Items\corazon",4,40,40)
fire_reward = [pygame.image.load("Recursos\Items\dinamita.png")]
reescalar_imagenes(fire_reward, (20,20))

dic_rewards = {
    "coin": coin_reward,
    'heart': heart_reward,
    'fire': fire_reward
}

#TRAPS
stake_trap = obtener_animaciones("Recursos\Items\estaca",5,20,50)

dic_traps = {"stake": stake_trap}

#PROJECTILES
projectile_player_r = [pygame.image.load("Recursos\Items\Fire.png")]
projectile_player_l = girar_imagenes(projectile_player_r, True, False)

projectile_boss_r = obtener_animaciones("Recursos/Items/Fuego",9,40,12)
projectile_boss_l = obtener_animaciones("Recursos/Items/Fuego",9,40,12, True)

reescalar_imagenes(projectile_player_r, (35,7))
reescalar_imagenes(projectile_player_l, (35, 7))

dic_projectiles = {"projectile_player_r" : projectile_player_r,
                        "projectile_player_l" : projectile_player_l,
                        "projectile_boss_r" : projectile_boss_r,
                        "projectile_boss_l" : projectile_boss_l}



