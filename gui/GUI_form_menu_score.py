import pygame
from pygame.locals import *

from .GUI_label import Label
from .GUI_form import Form
from .GUI_button_image import Button_Image
from constantes_pygame import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, active, path_image, score, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w, h))

        self._slave = aux_imagen
        self._score = score

        self._margen_y = margen_y


        self.fondo = pygame.image.load("Recursos/Fondos/Fondo1.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        self.screen = screen
        self.label_titulo = Label(self._slave, 110, 0, 420, 100, "RANKING", "Recursos\Fuentes\Fuente.ttf", 25, COLOR_BLANCO, "Recursos\GUI\interfaz1.png")

        lbl_nivel = Label(self._slave, x= 70, y= 140, w= 150, h= 60, text= "LEVEL",
                        font= "Recursos\Fuentes\Fuente.ttf", font_size= 20, font_color= "White", path_image= "Recursos\GUI\interfaz1.png")
        
        lbl_jugador = Label(self._slave, x= 255, y= 140, w= 140, h= 60, text= "PLAYER",
                        font= "Recursos\Fuentes\Fuente.ttf", font_size= 20, font_color= "White", path_image= "Recursos\GUI\interfaz1.png")
        
        lbl_puntaje = Label(self._slave, x= 440, y= 140, w= 140, h= 60, text= "SCORE",
                        font= "Recursos\Fuentes\Fuente.ttf", font_size= 20, font_color= "White", path_image= "Recursos\GUI\interfaz1.png")
        
        
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(lbl_nivel)
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        try:
            pos_inicial_y = margen_y
            for j in self._score:
                pos_inicial_x = margen_x
                for n,s in j.items():
                    cadena = ""
                    cadena = f"{s}"
                    item = Label(self._slave, pos_inicial_x, pos_inicial_y, 170, 50, cadena, "Recursos\Fuentes\Fuente.ttf", 20,
                                    "White", "Recursos\GUI\interfaz1.png")
                    self.lista_widgets.append(item)
                    pos_inicial_x += 185
                pos_inicial_y += 50 + espacio
        except:
            self.label_no_hay_datos = Label(self._slave, 100, 250, 480, 120, "No hay datos para mostrar", "Recursos\Fuentes\Fuente.ttf", 20, "White", "Recursos\GUI\interfaz1.png")
            self.lista_widgets.append(self.label_no_hay_datos)


        self._btn_home = Button_Image(screen=self._slave,
                                        x = 290,
                                        y = 430,
                                        master_x = x,
                                        master_y = y,
                                        w = 100,
                                        h = 100,
                                        onclick = self.btn_home_click,
                                        onclick_param = "home",
                                        path_image = "Recursos\GUI\Boton_home.png")
        
        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, param):
        self.end_dialog()


    def update(self, lista_eventos):
        if self.active:
            self.screen.blit(self.fondo, (0,0))
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()

