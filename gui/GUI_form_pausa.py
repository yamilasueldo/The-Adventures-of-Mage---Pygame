import pygame
from pygame.locals import *

from gui.GUI_label import Label
from gui.GUI_form import Form
from gui.GUI_button_image import Button_Image
from gui.GUI_form_settings import FormSettings

class FormPausa(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self._btn_jugar = Button_Image(screen=self._slave,
                                        master_x = x,
                                        master_y = y,
                                        x = 180,
                                        y = 120,
                                        w = 150,
                                        h = 150,
                                        path_image = "Recursos\GUI\Boton_play.png",
                                        onclick = self.btn_jugar_click,
                                        onclick_param = ""
                                        )

        self.btn_ajustes = Button_Image(screen=self._slave,
                                        master_x = 290,
                                        master_y = 400,
                                        x = 230,
                                        y = 300,
                                        w = 60,
                                        h = 60,
                                        path_image= "Recursos\GUI\Boton_config.png",
                                        onclick = self.btn_ajustes_click,
                                        onclick_param = ""
                                        )
        
        self.label_titulo = Label(self._slave, 50, 0, 400, 90, "PAUSED GAME", "Recursos/Fuentes/Fuente.ttf", 30, "Black", "Recursos\GUI\interfaz0.png")

        self.lista_widgets.append(self._btn_jugar)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.label_titulo)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_jugar_click(self, param):
        self.end_dialog()

    def btn_ajustes_click(self, param):
        form_ajustes = FormSettings(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "Recursos\GUI\interfaz0.png")
        self.show_dialog(form_ajustes)