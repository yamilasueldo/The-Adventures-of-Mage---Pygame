import pygame
from pygame.locals import *
import sqlite3

from .GUI_label import Label
from .GUI_form import Form
from .GUI_button_image import Button_Image
from .GUI_form_menu_score import FormMenuScore
from .GUI_form_seleccion_nivel import FormSeleccionNivel
from .GUI_form_settings import FormSettings
from constantes_pygame import *


class FormMenuPrincipal(Form):
    def __init__(self, screen, x, y, w, h, path_image, active = True):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("Recursos\Fondos\Fondo1.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.screen = screen


        self.label_titulo = Label(
                            screen=self._slave,
                            x= 200,
                            y= 0,
                            w= 200,
                            h= 110,
                            text="MENU",
                            font= "Recursos/Fuentes/Fuente.ttf",
                            font_size= 18,
                            font_color= "White",
                            path_image="Recursos/GUI/interfaz0.png")

        #BOTONES
        self.btn_config = Button_Image(screen=self._slave,master_x= x,master_y=y,x= 400,y=400,w= 60,h= 60,path_image= "Recursos/GUI/Boton_config.png",onclick= self.btn_settings_click, onclick_param="a", font="Recursos\Fuentes\Fuente.ttf", font_size=1, font_color="whitesmoke")
        self.btn_play = Button_Image(self._slave, x, y, 250,350, 150, 150,"Recursos/GUI/Boton_play.png", self.btn_play_click, "a", font="Recursos\Fuentes\Fuente.ttf", font_size=1, font_color="whitesmoke")
        self.btn_raking = Button_Image(self._slave, x, y, 150, 400, 60, 60, "Recursos/GUI/Boton_raking.png", self.btn_ranking_click, "x")
        self.label_instrucciones = Label(
                            screen=self._slave,
                            x= 100,
                            y=150,
                            w= 400,
                            h= 200,
                            text="Throw (F) - Attack (G) - Jump (Space) ",
                            font= "Recursos/Fuentes/Fuente.ttf",
                            font_size= 12,
                            font_color= COLOR_MARRON,
                            path_image="Recursos/GUI/table.png") 


        #### AGREGO LOS CONTROLES A UNA LISTAS ####
        self.lista_widgets.append(self.btn_raking)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_config)
        self.lista_widgets.append(self.label_instrucciones)
        self.lista_widgets.append(self.label_titulo)


        #musica
        pygame.mixer.music.load("Recursos/Sonidos/intro.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.screen.blit(self.fondo, (0,0))
            if self.active:
                self.draw()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        
    def btn_play_click(self, param):
        frm_jugar = FormSeleccionNivel(screen=self._master,
                                x = 300,
                                y = 0,
                                w = 600,
                                h = 600,
                                active = True,
                                path_image="Recursos/GUI/Fondo_menu.png"
                                )
        self.show_dialog(frm_jugar)


    def btn_settings_click(self,param):
        form_settings = FormSettings(self._master,
                                    x=300,
                                    y=0,
                                    w=600,
                                    h=600,
                                    color_background=COLOR_NEGRO,
                                    color_border=COLOR_NARANJA,
                                    border_size=2,
                                    active=True,
                                    path_image="") #Recursos/GUI/Fondo_menu.png
        self.show_dialog(form_settings)

    def btn_ranking_click(self, texto):
        lista_puntajes = self.obtener_top_tres_jugadores_db()
        form_ranking = FormMenuScore(screen=self._master,
                                        x=300,
                                        y=0,
                                        w=700,
                                        h=600,
                                        #color_background= COLOR_NARANJA,
                                        #color_border= COLOR_NARANJA,
                                        active=True,
                                        path_image="Recursos/GUI/fondo_menu.png",
                                        score=lista_puntajes,
                                        margen_y=240,
                                        margen_x=70,
                                        espacio=3
                                        )
        self.show_dialog(form_ranking)

    def obtener_top_tres_jugadores_db(self):
        with sqlite3.connect("datos_jugadores.db") as conexion:
            try:
                lista_puntajes = []
                cursor = conexion.execute("select * from Puntuaciones order by puntaje desc limit 3")
                for fila in cursor:
                    dic = {}
                    dic["Nivel"] = fila[1]
                    dic["Jugador"] = fila[2]
                    dic["Puntaje"] = fila[3]
                    lista_puntajes.append(dic)
                print("Datos seleccionados con exito")
                return lista_puntajes
            except:
                print("Hubo un error al intentar seleccionar los datos de la base de datos :(")
