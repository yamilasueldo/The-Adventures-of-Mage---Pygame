import pygame, sys
from pygame.locals import *
from configuraciones import *
from Clases.class_enemigo import Enemigo
from Clases.class_nivel import *
from Clases.class_jugador import Jugador
#from Clases.class_item import Item
#from Clases.class_trampa import Trampa
from Clases.class_plataforma import Plataforma
from constantes_pygame import *
from Clases.class_moneda import crear_monedas





plataformas_enemigo_uno = [Plataforma(265,ALTURA_BASE_PLATAFORMA - 60 ,80,55,0),Plataforma(335,ALTURA_BASE_PLATAFORMA - 60 ,80,55,1),Plataforma(405,ALTURA_BASE_PLATAFORMA - 60 ,80,55,2)]

plataformas_enemigo_dos = [Plataforma(630,ALTURA_BASE_PLATAFORMA - 470 ,80,55,0),Plataforma(700,ALTURA_BASE_PLATAFORMA - 470 ,80,55,1),Plataforma(770,ALTURA_BASE_PLATAFORMA - 470 ,80,55,2)]

#(self, x, velocidad, plataformas,fotograma_por_sg,movimiento_por_sg,dic_animaciones, direccion=DIRECCION_D):

enemigo_uno = Enemigo( x=265, velocidad=2, plataformas=plataformas_enemigo_uno,fotograma_por_sg = 80,movimiento_por_sg=10,dic_animaciones=dic_animaciones_golem, direccion=DIRECCION_D)

enemigo_dos = Enemigo( x=630, velocidad=2, plataformas=plataformas_enemigo_uno,fotograma_por_sg = 80,movimiento_por_sg=10,dic_animaciones=dic_animaciones_golem, direccion=DIRECCION_D)

#PLATAFORMAS


lista_plataformas = []
lista_plataformas.append(Plataforma(-5,ALTURA_BASE_PLATAFORMA,80,80,4)) # x y w h plataforma
lista_plataformas.append(Plataforma(70,ALTURA_BASE_PLATAFORMA,80,80,5))
lista_plataformas.append(Plataforma(135,ALTURA_BASE_PLATAFORMA,80,80,5))

lista_plataformas.append(Plataforma(505,ALTURA_BASE_PLATAFORMA - 120 ,80,55,0))
lista_plataformas.append(Plataforma(575,ALTURA_BASE_PLATAFORMA - 120 ,80,55,1))
lista_plataformas.append(Plataforma(645,ALTURA_BASE_PLATAFORMA - 120 ,80,55,2))
lista_plataformas.append(Plataforma(585,ALTURA_BASE_PLATAFORMA - 160 ,50,50,9))

lista_plataformas.append(Plataforma(800,ALTURA_BASE_PLATAFORMA -10,50,50,6))
lista_plataformas.append(Plataforma(848,ALTURA_BASE_PLATAFORMA -10,50,50,7))
lista_plataformas.append(Plataforma(898,ALTURA_BASE_PLATAFORMA -10,50,50,8))
lista_plataformas.append(Plataforma(800,ALTURA_BASE_PLATAFORMA - 60 ,50,50,3))
lista_plataformas.append(Plataforma(848,ALTURA_BASE_PLATAFORMA - 60 ,50,50,4))
lista_plataformas.append(Plataforma(898,ALTURA_BASE_PLATAFORMA - 60 ,50,50,5))

lista_plataformas.append(Plataforma(1000,ALTURA_BASE_PLATAFORMA - 110 ,80,55,0))
lista_plataformas.append(Plataforma(1070,ALTURA_BASE_PLATAFORMA - 110 ,80,55,1))
lista_plataformas.append(Plataforma(1140,ALTURA_BASE_PLATAFORMA - 110 ,80,55,2))

lista_plataformas.append(Plataforma(1250,ALTURA_BASE_PLATAFORMA - 180 ,80,55,0))
lista_plataformas.append(Plataforma(1320,ALTURA_BASE_PLATAFORMA - 180 ,80,55,1))
lista_plataformas.append(Plataforma(1390,ALTURA_BASE_PLATAFORMA - 180 ,80,55,2))

lista_plataformas.append(Plataforma(870,ALTURA_BASE_PLATAFORMA - 250 ,80,55,0))
lista_plataformas.append(Plataforma(940,ALTURA_BASE_PLATAFORMA - 250 ,80,55,1))
lista_plataformas.append(Plataforma(1010,ALTURA_BASE_PLATAFORMA - 250 ,80,55,1))
lista_plataformas.append(Plataforma(1080,ALTURA_BASE_PLATAFORMA - 250 ,80,55,2))

lista_plataformas.append(Plataforma(570,ALTURA_BASE_PLATAFORMA - 270 ,80,55,0))
lista_plataformas.append(Plataforma(640,ALTURA_BASE_PLATAFORMA - 270 ,80,55,1))
lista_plataformas.append(Plataforma(710,ALTURA_BASE_PLATAFORMA - 270 ,80,55,2))

lista_plataformas.append(Plataforma(280,ALTURA_BASE_PLATAFORMA - 320 ,80,55,0))
lista_plataformas.append(Plataforma(350,ALTURA_BASE_PLATAFORMA - 320 ,80,55,1))
lista_plataformas.append(Plataforma(420,ALTURA_BASE_PLATAFORMA - 320 ,80,55,2))

lista_plataformas.append(Plataforma(0,ALTURA_BASE_PLATAFORMA - 400 ,80,55,0))
lista_plataformas.append(Plataforma(70,ALTURA_BASE_PLATAFORMA - 400 ,80,55,1))
lista_plataformas.append(Plataforma(140,ALTURA_BASE_PLATAFORMA - 400 ,80,55,1))
lista_plataformas.append(Plataforma(210,ALTURA_BASE_PLATAFORMA - 400 ,80,55,2))

lista_plataformas.append(Plataforma(320,ALTURA_BASE_PLATAFORMA - 500 ,80,55,0))
lista_plataformas.append(Plataforma(390,ALTURA_BASE_PLATAFORMA - 500 ,80,55,1))
lista_plataformas.append(Plataforma(460,ALTURA_BASE_PLATAFORMA - 500 ,80,55,2))


lista_plataformas.append(Plataforma(900,ALTURA_BASE_PLATAFORMA - 520 ,80,55,0))
lista_plataformas.append(Plataforma(970,ALTURA_BASE_PLATAFORMA - 520 ,80,55,1))
lista_plataformas.append(Plataforma(1040,ALTURA_BASE_PLATAFORMA - 520 ,80,55,1))
lista_plataformas.append(Plataforma(1110,ALTURA_BASE_PLATAFORMA - 520 ,80,55,2))
lista_plataformas.append(Plataforma(1090,ALTURA_BASE_PLATAFORMA - 560 ,50,50,10))

lista_plataformas.extend([plataformas_enemigo_uno,plataformas_enemigo_dos])

lista_monedas = crear_monedas(10)
lista_enemigos = [enemigo_uno,enemigo_dos]




#nivel_uno = Nivel(nombre_nivel="nivel_uno",jugador=mi_jugador, lista_enemigos=lista_enemigos, lista_plataformas=lista_plataformas, lista_monedas=lista_monedas,imagen_fondo = "Recursos\Fondos\Fondo_nivel_uno.png",cantidad_enemigos_a_derrotar=3,cantidad_puntos_requeridos=300)

class NivelUno(Nivel):
    def __init__(self,screen: pygame.Surface):
        #,nombre_nivel,jugador, lista_enemigos, lista_plataformas, lista_monedas,imagen_fondo,cantidad_enemigos_a_derrotar,cantidad_puntos_requeridos
#    def __init__(self,nombre_nivel, mi_jugador, pantalla:pygame.Surface):
        ANCHO = screen.get_width()
        ALTO = screen.get_height()
        nombre_nivel="nivel_uno"

        fondo = pygame.image.load("Recursos\Fondos\Fondo_nivel_uno.png")
        fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))
        cantidad_enemigos_a_derrotar = 3
        cantidad_puntos_requeridos = 300
    
        mi_jugador= Jugador(x=X_INICIAL,y=Y_INICIAL,velocidad_caminar=4, gravedad=8,fotograma_por_sg=80,movimiento_por_sg=10,altura_salto=70)

        super().__init(screen,nombre_nivel,mi_jugador,lista_enemigos,lista_plataformas,lista_monedas,fondo,cantidad_enemigos_a_derrotar,cantidad_puntos_requeridos)
