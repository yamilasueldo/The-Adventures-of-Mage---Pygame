import pygame
from pygame.locals import *

from .GUI_form import Form
from .GUI_button_image import Button_Image
from .GUI_form_nivel_completado import FormNivelCompletado
from .GUI_form_nivel_perdido import FormNivelPerdido
from .GUI_form_pausa import FormPausa
#from constantes_pygame import DELTA_MS

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel,nombre_nivel,form_seleccion_nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "green", "black", -1, True) #pone 600 en vez de pantalla.get_width()
        nivel._slave = self._slave
        self.nivel = nivel
        self.nombre_nivel = nombre_nivel
        self.form_seleccion_nivel = form_seleccion_nivel
        self.nivel_finalizado = False

        self.btn_home = Button_Image(screen=self._slave,
                                    master_x= self._x,
                                    master_y= self._y,
                                    x = self._w - 60,
                                    y = 0,
                                    w = 50,
                                    h = 50,
                                    onclick= self.btn_home_click,
                                    onclick_param= "",
                                    path_image= "Recursos\GUI\Boton_home.png")
        
        self.btn_mute = Button_Image(screen=self._slave,
                                    master_x= self._x,
                                    master_y= self._y,
                                    x = self._w - 60,
                                    y = 60,
                                    w = 50,
                                    h = 50,
                                    onclick= self.btn_mute_click,
                                    onclick_param= "",
                                    path_image= "Recursos\GUI\Boton_sound.png")
        
        self._btn_pausa = Button_Image(screen=self._slave,
                                        master_x = self._x,
                                        master_y = self._y,
                                        x = self._w - 60,
                                        y = 120,
                                        w = 50,
                                        h = 50,
                                        onclick = self.btn_pausa_click,
                                        onclick_param = "",
                                        path_image = "Recursos\GUI\Boton_pausa.png")
        

        self.flag_mute = True

        self.lista_widgets.append(self._btn_pausa)
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_mute)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.nivel.update(lista_eventos)
            self.finalizar_nivel()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def btn_home_click(self, param):
        self.end_dialog()

    def btn_pausa_click(self, param):
        form_nivel_perdido = FormPausa(
                                        screen=self._master,
                                        x= (self._w/2) -250,
                                        y=50,
                                        w=500,
                                        h=500,
                                        active=True,
                                        path_image="Recursos\GUI\Fondo_menu.png")
        self.show_dialog(form_nivel_perdido)
        
            
    def finalizar_nivel(self):
        if len(self.nivel.enemies) == 0 or self.nivel.time_left == 0:
            if self.nivel.score > 0:
                if self.nombre_nivel == "level_one":
                    self.form_seleccion_nivel.nivel_uno_completado = True
                if self.nombre_nivel == "level_two":
                    self.form_seleccion_nivel.nivel_dos_completado = True
                self.form_nivel_completado()
            else:
                self.form_nivel_perdido()
        elif self.nivel.player.lives <= 0:
            self.form_nivel_perdido()
                
    def form_nivel_perdido(self):
        if self.nivel_finalizado:
                self.end_dialog()
        else:
            self.nivel_finalizado = True
            form_nivel_perdido = FormNivelPerdido(self._master,
                                            300,
                                            0,
                                            600,
                                            600,
                                            True,
                                            "Recursos\GUI\Fondo_menu.png")
            self.show_dialog(form_nivel_perdido)

    def form_nivel_completado(self):
        if self.nivel_finalizado:
                    self.end_dialog()
        else:
            puntaje_final = self.nivel.score + self.nivel.time_left * 100
            self.nivel_finalizado = True
            form_nivel_completado = FormNivelCompletado(self._master,
                                            300,
                                            0,
                                            600,
                                            600,
                                            True,
                                            "Recursos\GUI\Fondo_menu.png",
                                            puntaje_final,
                                            self.nombre_nivel)
            self.show_dialog(form_nivel_completado)
            
            

    def btn_mute_click(self, param):
        if self.flag_mute:
            # Silenciar el audio
            pygame.mixer.music.pause()
            pygame.mixer.pause()
            pygame.mixer.music.set_volume(0)  # Establecer volumen en 0
        else:
            # Restaurar el audio
            pygame.mixer.music.unpause()
            pygame.mixer.unpause()
            pygame.mixer.music.set_volume(1)  # Restaurar volumen original
        self.flag_mute = not self.flag_mute

    
