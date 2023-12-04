import pygame
from constantes_pygame import *
from Clases.class_imagen import *

pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)

# Declaro todas las imagenes y musica 

mage_img = pygame.image.load("Recursos\Personages\Mage\Mage.png").convert_alpha()
mage_img = pygame.transform.scale(mage_img, (150, 150))
mage_img_pos = mage_img.get_rect(center = (ANCHO_PANTALLA/2, 350))

flag_bajando = True

pygame.mixer.init()
pygame.mixer.music.load("Recursos/Sonidos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

#abra pantalla de inicio
fondo_start = Imagen("Recursos\Fondos\Fondo0.jpg", ANCHO_PANTALLA, ALTO_PANTALLA, 0,0, pantalla)
fondo_start = Imagen.cargar_imagen(fondo_start)

game_over_pantalla_fade = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
game_over_pantalla_fade.fill((0, 0, 0))
game_over_pantalla_fade.set_alpha(60)

def dibujar_start(pantalla):
    #bliteo el fondo y un fade para oscurecer la imagen, creo y bliteo las fuentes
    global flag_bajando

    pantalla.blit(fondo_start, (0,0))
    pantalla.blit(game_over_pantalla_fade, (0, 0))

    #caption e icono
    pygame.display.set_caption("The Adventures of Mage")
    icono = pygame.image.load("Recursos\Personages\Mage\Icono.png")
    pygame.display.set_icon(icono)

    texto_titulo = pygame.font.Font("Recursos\Fuentes\Fuente.ttf", 60)
    texto_titulo_outline = pygame.font.Font("Recursos\Fuentes\Fuente.ttf", 60)
    boton_start = pygame.font.Font("Recursos\Fuentes\Fuente.ttf", 40)
    boton_start_outline = pygame.font.Font("Recursos\Fuentes\Fuente.ttf", 40)
    controles = pygame.font.Font("Recursos\Fuentes\Fuente.ttf", 10)


    #surfaces
    #titulo
    texto_titulo = texto_titulo.render("The Adventures of Mage", False, COLOR_MARRON).convert()
    texto_titulo_rect = texto_titulo.get_rect(center = (ANCHO_PANTALLA/2, 180))
    #titulo outline
    texto_titulo_outline = texto_titulo_outline.render("The Adventures of Mage", False, (5, 26, 8)).convert()
    texto_titulo_outline_rect = texto_titulo_outline.get_rect(center = (ANCHO_PANTALLA/2, 186))
    #start
    boton_start = boton_start.render("PRESS ENTER", False, COLOR_BLANCO).convert()
    boton_start_rect = boton_start.get_rect(center = (ANCHO_PANTALLA/2, 270))
    #start outline
    boton_start_outline = boton_start_outline.render("PRESS ENTER", False, (5, 26, 8)).convert()
    boton_start_outline_rect = boton_start_outline.get_rect(center = (ANCHO_PANTALLA/2, 274))
    controles_rect = texto_titulo.get_rect(center = (ANCHO_PANTALLA/2+100, ALTO_PANTALLA-30))


    pantalla.blit(texto_titulo_outline, texto_titulo_outline_rect)
    pantalla.blit(texto_titulo, texto_titulo_rect)
    pantalla.blit(boton_start_outline, boton_start_outline_rect)
    pantalla.blit(boton_start, boton_start_rect)
  
    # Controla la oscilacion del personaje del inicio (unicamente visual)
    if flag_bajando:
        mage_img_pos.y += 1 #baja
        if mage_img_pos.y == 300:
            flag_bajando = False
    else:
        mage_img_pos.y -= 1
        if mage_img_pos.y == 270:
            flag_bajando = True
    pantalla.blit(mage_img, (mage_img_pos.x, mage_img_pos.y))