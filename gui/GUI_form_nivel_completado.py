import pygame
from pygame.locals import *
import sqlite3

from .GUI_label import *
from .GUI_form import *
from .GUI_button_image import *
from .GUI_checkbox import *
from .GUI_textbox import *
from constantes_pygame import COLOR_NARANJA, COLOR_MARRON


class FormNivelCompletado(Form):
    def __init__(self, screen, x, y, w, h, active, path_image, puntuacion_jugador, nombre_nivel):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.puntuacion_jugador = puntuacion_jugador
        self.nombre_nivel = nombre_nivel
        self.datos_guardados = False

        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "Level Completed", "Recursos/Fuentes/Fuente.ttf", 30, "Black", "Recursos\GUI\Interfaz1.png")
        self.label_puntuacion = Label(self._slave, 100, 120, 480, 100, f"YOU HAVE SCORED {self.puntuacion_jugador} POINTS!", "Recursos/Fuentes/Fuente.ttf", 20, "White", "Recursos\GUI\Interfaz1.png")
        self.label_pedir_nombre = Label(self._slave, 100, 240, 480, 100, "YOUR NAME:", "Recursos/Fuentes/Fuente.ttf", 20, "White", "Recursos\GUI\Interfaz1.png")
        self.textbox_nombre_jugador = TextBox(
                                    screen= self._slave,
                                    master_x= x,
                                    master_y= y, 
                                    x= 200, 
                                    y= 355, 
                                    w= 200, 
                                    h= 70, 
                                    color_background= COLOR_NARANJA,
                                    color_background_seleccionado= COLOR_MARRON, 
                                    color_border= COLOR_MARRON, 
                                    color_border_seleccionado= COLOR_NARANJA, 
                                    border_size= 2,
                                    font= "Recursos/Fuentes/Fuente.ttf",
                                    font_size= 20,
                                    font_color= "Black")



        self._btn_guardar = CheckBox(screen=self._slave, master_x = x, master_y = y, x = 405, y = 350, w = 80, h = 80,
                                    path_image_on= "Recursos\GUI\Boton_guardar.png", path_image_off= "Recursos\GUI\Boton_guardado.png")
        
        
        self._btn_home = Button_Image(screen=self._slave,
                                        x = 290,
                                        y = 450,
                                        master_x = x,
                                        master_y = y,
                                        w = 100,
                                        h = 100,
                                        onclick = self.btn_home_click,
                                        onclick_param = "",
                                        path_image = "Recursos/GUI/Boton_home.png")
        
        
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(self.label_puntuacion)
        self.lista_widgets.append(self.label_pedir_nombre)
        self.lista_widgets.append(self.textbox_nombre_jugador)
        self.lista_widgets.append(self._btn_guardar)
        self.lista_widgets.append(self._btn_home)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.btn_guardar_click()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def renombrar_nivel(self):
        nombre_nivel = self.nombre_nivel
        if nombre_nivel == "level_one":
            nombre_nivel = "1"
        elif nombre_nivel == "level_two":
            nombre_nivel = "2"
        else:
            nombre_nivel = "3"
        return nombre_nivel

    
    def btn_guardar_click(self):
        if self._btn_guardar.get_esta_prendido():
            if self.datos_guardados == False:
                self.nombre_jugador = self.textbox_nombre_jugador.get_text()
                nombre_nivel = self.renombrar_nivel()
                if len(self.nombre_jugador) > 0:
                    self.guardar_datos_en_db(nombre_nivel, self.nombre_jugador, self.puntuacion_jugador)
                    self.datos_guardados = True

    def guardar_datos_en_db(self, nivel, nombre, puntaje):
        with sqlite3.connect("datos_jugadores.db") as conexion:
            try:
                conexion.execute('''
                                create table if not exists Puntuaciones
                                (
                                    id integer primary key autoincrement,
                                    nivel text,
                                    nombre text,
                                    puntaje integer
                                )
                                ''')
                conexion.execute("insert into Puntuaciones(nivel, nombre, puntaje) values(?,?,?)", (nivel, nombre, puntaje))
                print("Datos insertados en la base de datos con exito!")
            except:
                print("Hubo un error al intentar insertar los datos en la base de datos :(")

