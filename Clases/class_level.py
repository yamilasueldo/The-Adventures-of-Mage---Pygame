import pygame, sys
from pygame.locals import *
from mode import *
#from hud import *
from configuraciones import *
from Clases.class_platform import Platform
from Clases.class_reward import Reward
from Clases.class_trap import Trap

from Clases.class_enemy import Enemy
from Clases.class_boss import Boss

class Level():
    def __init__(self, screen, player, img_background):
        self._slave = screen
        self.player = player
        self.img_background = img_background
        self.score = 0
        self.time_left = 60
        
        self.dynamite = pygame.image.load("Recursos\Items\dinamita.png")
        self.dynamite = pygame.transform.scale(self.dynamite,(30,30))


        self.timer_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.timer_event, 1000)

        self.sound_enemy_dead = pygame.mixer.Sound("Recursos\Sonidos\Personage_hurt.mp3")
        self.sound_enemy_dead.set_volume(1)

        # TODO SONIDOS

    def update(self, list_events):
        for event in list_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    change_mode()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == self.timer_event:
                self.time_left -=1
        self.update_screen()
        self.developer_mode()
        self.draw_hud()
        self.calculate_score()

    def update_screen(self):
        self._slave.blit(self.img_background,(0,0))
        for platform in self.platforms:
            platform.update(self._slave)
        for enemy in self.enemies:
            enemy.update(self._slave, self.platforms)
            if enemy.lives == 0:
                self.enemies.remove(enemy)
                self.sound_enemy_dead.play()
                self.player.murders += 1
        for item in self.items:
            item.update(self._slave)
        self.player.update(self._slave, self.platforms, self.enemies, self.items)
        self.check_collisions_projectiles()

    def check_collisions_projectiles(self):
        for projectil in self.player.projectiles:
            projectil.update(self._slave, self.player, self.enemies, self.platforms)
        for enemy in self.enemies:
            for projectil in enemy.projectiles:
                projectil.update(self._slave, enemy, self.player, self.platforms)
    
    def calculate_score(self):
        self.score = self.player.collected_coins * 50 + self.player.murders * 100
    
    def draw_hud(self):
        pygame.draw.rect(self._slave,COLOR_NEGRO,(420,0,440,40),border_radius=5)  #dibujo la barra para el hud
        font = pygame.font.SysFont("Arial",20)
        lives = font.render(f": {self.player.lives}", True, "White")
        self._slave.blit(heart_reward[0],(430,-8))
        self._slave.blit(lives,(455,4))

        dynamites = font.render(f": {self.player.remaining_shots}", True, "White")

        self._slave.blit(dynamites,(570,5))
        self._slave.blit(self.dynamite,(550,2))
        if self.time_left >=10:
            temporizador = f"00:{self.time_left}"
        else:
            temporizador = f"00:0{self.time_left}"
        time = font.render(temporizador, True, "Red")
        self._slave.blit(time,(630,5))

        score = font.render(f"SCORE: {self.score}", True, "White")
        self._slave.blit(score,(720,5))

    def developer_mode(self):
        if get_mode():
            for side in self.player.sides:
                pygame.draw.rect(self._slave, COLOR_NARANJA, self.player.sides[side], 2)
                for projectil in self.player.projectiles:
                    for side in projectil.sides:
                        pygame.draw.rect(self._slave, COLOR_NARANJA, projectil.sides[side], 2)
            
            for platform in self.platforms:
                for side in platform.sides:
                    pygame.draw.rect(self._slave, COLOR_AZUL, platform.sides[side], 2)
            
            for item in self.items:
                for side in item.sides:
                    if isinstance(item, Reward):
                        pygame.draw.rect(self._slave, COLOR_VERDE, item.sides[side], 2)
                    if isinstance(item, Trap):
                        pygame.draw.rect(self._slave, COLOR_ROJO, item.sides[side], 2)
                        
            for enemy in self.enemies:
                for side in enemy.sides:
                    pygame.draw.rect(self._slave, COLOR_AZUL, enemy.sides[side], 2)
                for projectil in enemy.projectiles:
                    for side in projectil.sides:
                        pygame.draw.rect(self._slave, COLOR_AZUL, projectil.sides[side], 2)

    def draw_background(self, background):
        '''POSICIONES OBJETOS :
        0 -> Vacio
        1 -> Plataforma Piedra
        2 -> Plataforma Pasto
        3 -> Recompensa Moneda
        4 -> Recompensa Corazon
        5 -> Recompensa Dinamita
        6 -> Trampa 
        7 -> Enemigo (Camina y Ataca)
        8 -> Enemigo (Quieto(der) y Lanza)
        9 -> Enemigo (Quieto(izq) y Lanza)
        10 -> BOSS (Camina, Salta, Lanza y Ataca)
        '''
        self.platforms = []
        self.enemies = []
        self.items = []
        size = 40 
        row_counter = 0 
        for row in background:
            column_counter = 0 
            for chart in row: # CHART
                if chart == 1:
                    self.platforms.append(Platform(dic_platforms,'stone',(column_counter * size, row_counter * size)))
                if chart == 2:
                    self.platforms.append(Platform(dic_platforms,'grass',(column_counter * size, row_counter * size)))
                if chart == 3:
                    self.items.append(Reward(dic_rewards,'coin',(column_counter * size, row_counter * size)))
                if chart == 4: 
                    self.items.append(Reward(dic_rewards,'heart',(column_counter * size, row_counter * size)))
                if chart == 5:
                    self.items.append(Reward(dic_rewards,'fire',(column_counter * size, row_counter * size)))
                if chart == 6:
                    self.items.append(Trap(dic_traps,'stake',(column_counter * size, row_counter * size-10)))
                if chart == 7:
                    self.enemies.append(Enemy(dic_enemy,'idle_r',(column_counter * size, row_counter * size), 4, True, False, False, True))
                if chart == 8:
                    self.enemies.append(Enemy(dic_enemy,'idle_r',(column_counter * size, row_counter * size), 4, False, False, True, False))
                if chart == 9 :
                    self.enemies.append(Enemy(dic_enemy,'idle_l',(column_counter * size, row_counter * size), 4, False, False, True, False))
                if chart == 10:
                    self.enemies.append(Boss(dic_enemy_boss,'idle_r',(column_counter * size, row_counter * size), 4, True, True, True, True))
                column_counter += 1
            row_counter += 1
                                    




        


# import pygame, sys
# from pygame.locals import *
# # from modo import *
# from hud import *
# from configuraciones import COLOR_NEGRO,obtener_rectangulos
# from sql import *
# from constantes_pygame import TAMAÑO_PANTALLA


# class Nivel:
#     def __init__(self,screen,nombre_nivel,jugador, lista_enemigos, lista_plataformas, lista_monedas,imagen_fondo,cantidad_enemigos_a_derrotar,cantidad_puntos_requeridos):
#         self._slave = screen
#         self.nombre_nivel = nombre_nivel
#         self.puntuacion = 0
#         self.tiempo_restante = 60
#         self.imagen_fondo = pygame.image.load(imagen_fondo)
#         self.imagen_fondo = pygame.transform.scale(imagen_fondo, (screen.get_width(), screen.get_height()))
#         self.reloj = pygame.time.Clock()
#         self.jugador = jugador
#         self.enemigos = lista_enemigos
#         self.plataformas = lista_plataformas
#         self.monedas = lista_monedas
#         self.nivel_terminado = False
#         self.enemigos_derrotados = []
#         self.enemigos_requeridos = cantidad_enemigos_a_derrotar
#         self.puntaje_requerido = cantidad_puntos_requeridos
#         self.puntaje = 0

#         self.timer_event = pygame.USEREVENT + 0
#         pygame.time.set_timer(self.timer_event, 1000)

#     # def manejar_eventos(self, lista_eventos):
#     #     for evento in pygame.event.get():
#     #         if evento.type == pygame.QUIT:
#     #             pygame.quit()
#     #             sys.exit()

#         #self.jugador.eventos(lista_eventos)

#     def update_platforms(self):
#         for plataforma in self.plataformas:
#             plataforma.update(self._slave)

#     def update_enemies(self):
#         for enemigo in self.enemigos:
#             enemigo.update(self._slave)
#             if not enemigo.esta_vivo:
#                 self.enemigos_derrotados.append(enemigo)
#                 self.enemigos.remove(enemigo)
#                 #aplico sonido
#                 #self.jugador.derrotados += 1

#     def update_coins(self):
#         for moneda in self.monedas:
#             moneda.update()

#     def update_screen(self):
#         self._slave.blit(self.imagen_fondo,(0,0))
#         self.update_platforms()
#         self.update_enemies()
#         self.update_coins()
#         self.jugador.update(self.plataformas, self.enemigos, self.monedas)
#         #CONTROL COLISION PROYECTILES        

#     def calcular_puntaje(self):
#         self.puntaje = self.jugador.puntaje 

#     def update(self, lista_eventos):
#         for evento in lista_eventos:
#             if evento.type == pygame.KEYDOWN:
#                 # if evento.key == pygame.K_TAB:
#                 #     cambiar_modo()
#                 if evento.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#             if evento.type == self.timer_event:
#                 self.tiempo_restante -= 1
#         self.update_screen()
#         #self.modo_programador()
#         #self.dibujar_grilla()
# #        self.blitear_barra_superior()
#         self.tiempo_restante = dibujar_hud(self._slave,self.jugador.vidas,self.jugador.puntaje)
#         self.calcular_puntaje()

#     def fue_completado(self):
#         fue_completado = False
#         if (self.enemigos_derrotados >= self.enemigos_requeridos) or (self.calcular_puntaje() >= self.puntaje_requerido):
#             fue_completado = True
#         return fue_completado


#     def fue_terminado(self):
#         fue_terminado = False
#         if (self.enemigos_derrotados >= self.enemigos_requeridos) or self.tiempo_restante == 0 :
#             fue_terminado = True
#             #self.fue_terminado = True
#         return fue_terminado

# #     def draw(self):
# #         self._slave.fill(COLOR_NEGRO)
# #         self.jugador.draw(self._slave)
# #         for enemigo in self.enemigos:
# #             enemigo.draw(self._slave)

# #         pygame.display.flip()

# #     # def ejecutar_nivel(self):
# #     #     while True:
# #     #         delta_ms = self.reloj.tick(FPS)

# #     #         lista_teclas = pygame.key.get_pressed()
# #     #         self.manejar_eventos(lista_teclas)
# #     #         self.update(delta_ms)
# #     #         self.draw()
