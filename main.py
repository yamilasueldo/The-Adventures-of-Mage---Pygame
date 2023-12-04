import pygame
import sys
#print(sys.path)
from pygame.locals import *
from pantalla_start import dibujar_start
from constantes_pygame import *

from gui.GUI_form_menu_principal import FormMenuPrincipal
#from sql import *
from mode import change_mode


# Inicializa Pygame
pygame.init()

# Declara reloj y dimensiones de la pantalla
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

# Declaro la flag de la pantalla de start
flag_start = True

# 
# Creo el objeto del formulario del menu principal
form_principal = FormMenuPrincipal( 
                                screen=PANTALLA,
                                x=ANCHO_PANTALLA/2 -300,
                                y= 0, 
                                w=600,
                                h=600,
                                path_image= "Recursos/GUI/fondo_menu.png",
                                active= True)


# Crea la base de datos
#crear_base()

while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    delta_ms = RELOJ.tick(FPS)
    for evento in lista_eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Pantalla de start
    if flag_start:
            if pygame.key.get_pressed()[pygame.K_RETURN] == False:
                dibujar_start(PANTALLA)
            else:
                flag_start = False

    # Menu principal
    else:
        PANTALLA.blit(pygame.transform.scale(pygame.image.load("Recursos\Fondos\Fondo1.jpg"), (ANCHO_PANTALLA, ALTO_PANTALLA)), (0,0))
        
        form_principal.update(lista_eventos)


    pygame.display.update()

