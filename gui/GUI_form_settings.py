import pygame
from pygame.locals import *
#from sql import *

from .GUI_slider import Slider
from .GUI_label import Label
from .GUI_form import Form
from .GUI_button_image import Button_Image

from .GUI_checkbox import CheckBox
from Clases.class_level import Level
from constantes_pygame import *

class FormSettings(Form):
    def __init__(self, screen, x, y, w, h,color_background,color_border = COLOR_NEGRO,border_size=-1, active=True, path_image=""):
        super().__init__(screen, x, y, w, h,color_background,color_border,border_size,active)

        # aux_imagen = pygame.image.load(path_image)
        # aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        # self._slave = aux_imagen
        self.screen = screen

        self.volumen_musica = 0.1
        self.flag_musica = True

        self.flag_sonidos = True
        pygame.mixer.init()

        self.label_titulo = Label(self._slave, 100, 0, 400, 80, "SETTINGS", "Recursos\Fuentes\Fuente.ttf", 25, "Black", "Recursos\GUI\Interfaz1.png")
        self._btn_musica = CheckBox(screen=self._slave, x = 65, y = 210, master_x = x, master_y = y, w = 100, h = 100,
                                    path_image_on= "Recursos\GUI\Boton_nosound.png", path_image_off= "Recursos\GUI\Boton_sound.png")
        
        self.slider_volumen_musica = Slider(self._slave, x, y,180, 250, 250, 15, self.volumen_musica, "Green", "White")
        self.label_volumen_musica = Label(self._slave, 450, 232, 100, 50, "10%", "Recursos\Fuentes\Fuente.ttf", 15, "Black", "Recursos\GUI\Interfaz1.png")

        self._btn_salir = Button_Image(screen=self._slave, x = 290, y = 400, master_x = x, master_y = y, w = 100, h = 100,
                                    onclick = self.btn_salir_click, onclick_param = "", path_image = "Recursos\GUI\Boton_home.png")
        
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(self._btn_musica)
        self.lista_widgets.append(self.slider_volumen_musica)
        self.lista_widgets.append(self.label_volumen_musica)

        self.lista_widgets.append(self._btn_salir)
        self.render()

    def render(self):
        self._slave.fill(self._color_background)

    def btn_musica_click(self):
        if self._btn_musica.get_esta_prendido():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.flag_musica = not self.flag_musica

    def update_volumen_musica(self, lista_eventos):
        self.volumen_musica = self.slider_volumen_musica.value
        self.slider_volumen_musica.update(lista_eventos)
        self.label_volumen_musica.update(lista_eventos)
        self.label_volumen_musica.set_text(f"{round(self.volumen_musica*100)}%")
        pygame.mixer.music.set_volume(self.volumen_musica)

    def btn_salir_click(self, param):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen_musica(lista_eventos)
                self.btn_musica_click()

        else:
            self.hijo.update(lista_eventos)
        return super().update(lista_eventos)


    