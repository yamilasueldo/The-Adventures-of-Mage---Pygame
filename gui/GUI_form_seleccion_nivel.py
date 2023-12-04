import pygame
from pygame.locals import *

from gui.GUI_button import Button
from gui.GUI_label import Label
from gui.GUI_button_image import Button_Image
from gui.GUI_form_menu_score import Form
from manejador_niveles import Manejador_niveles
from gui.GUI_form_contenedor_nivel import FormContenedorNivel
from constantes_pygame import*


class FormSeleccionNivel(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("Recursos/Fondos/Fondo1.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        self.manejador_niveles = Manejador_niveles(self._master)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self.screen = screen
        self.nivel_uno_completado = False
        self.nivel_dos_completado = False
        
        self._slave = aux_imagen


        #### CONTROLES ####
        self.btn_nv1 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=100,
                                    y=100,
                                    w=450,
                                    h=110,
                                    path_image="Recursos\GUI\Interfaz3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="level_one",
                                    font="Recursos\Fuentes\Fuente.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.btn_nv2 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=100,
                                    y=230,
                                    w=450,
                                    h=110,
                                    path_image="Recursos\GUI\Interfaz3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="level_two",
                                    font="Recursos\Fuentes\Fuente.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.btn_nv3 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=100,
                                    y=380,
                                    w=450,
                                    h=110,
                                    path_image="Recursos\GUI\Interfaz3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="level_three",
                                    font="Recursos\Fuentes\Fuente.ttf",
                                    font_size=15,
                                    font_color="green3")
        
        self.btn_home = Button_Image(self._slave,
                                    x,
                                    y,
                                    x= 850,
                                    y= 400,
                                    w= 50,
                                    h= 50,
                                    path_image="Recursos\GUI\Boton_home.png",
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    font="Recursos\Fuentes\Fuente.ttf",
                                    font_size=15,
                                    font_color=COLOR_MARRON)
        self.label_nv1 = Label(self._slave,
                                x=100,
                                y=100,
                                w=450,
                                h=110,
                                text="LEVEL 1",
                                font="Recursos\Fuentes\Fuente.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="Recursos\GUI\Interfaz3.png")
        self.label_nv2 = Label(self._slave,
                                x=100,
                                y=230,
                                w=450,
                                h=110,
                                text="LEVEL 2",
                                font="Recursos\Fuentes\Fuente.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="Recursos\GUI\Interfaz3.png")
        self.label_nv3 = Label(self._slave,
                                x=100,
                                y=380,
                                w=450,
                                h=110,
                                text="LEVEL 3",
                                font="Recursos\Fuentes\Fuente.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="Recursos\GUI\Interfaz3.png")

###############################################################

        #### AGREGO LOS CONTROLES A UNA LISTAS ####
        self.lista_widgets.append(self.btn_nv1)
        self.lista_widgets.append(self.btn_nv2)
        self.lista_widgets.append(self.btn_nv3)
        self.lista_widgets.append(self.label_nv1)
        self.lista_widgets.append(self.label_nv2)
        self.lista_widgets.append(self.label_nv3)
        self.lista_widgets.append(self.btn_home)
    

    def update(self, lista_eventos): 
        if self.verificar_dialog_result():
                self.screen.blit(self.fondo,(0,0))
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        if nombre_nivel == "level_two":
            if self.nivel_uno_completado:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1")
        elif nombre_nivel == "level_three":
            if self.nivel_uno_completado and self.nivel_dos_completado:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1 y 2")
        else:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
            self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()