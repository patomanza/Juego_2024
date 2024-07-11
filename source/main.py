import pygame
from pygame.locals import *
from settings import *
from imagenes import *
from colisiones import *
from rectangulos import *
from modo_debug import *
from game_over import *
from clases import Personaje,Enemigo,Plataforma,Trampa,PowerUp

def pantalla_inicio(botones):
    continuar = True
    
    pygame.mixer.music.load("source/Recursos/musica/star_wars_soundtrack.wav")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(-1)
    reproduciendo_musica = True
    
    
    pantalla.blit(fondo,(0,0))
    pantalla.blit(music_button,(750,550))
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir_juego()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos,rect):
                        if boton == "start":
                            continuar = False
                        elif boton == "exit":
                            salir_juego()
                        elif boton == "options":
                            print("MOSTRAR OPCIONES")
            if evento.type  == KEYDOWN:
                if evento.key == K_m:
                    if reproduciendo_musica:
                        pygame.mixer.music.set_volume(0)
                        pantalla.blit(muted_music,(750,550))
                    else:
                        pygame.mixer.music.set_volume(0.01)
                        pantalla.blit(music_button,(750,550))
                    reproduciendo_musica = not reproduciendo_musica
        
        
        
        pantalla.blit(start_button, (button_x,start_button_y))
        pantalla.blit(options_button, (button_x,options_button_y))
        pantalla.blit(exit_button, (button_x,exit_button_y))
        
        
        pygame.display.flip()
    
    
    pygame.mixer.music.stop()


pygame.init()

piso = pygame.Rect(0,510,160,90)
lados_piso = obtener_rectangulos(piso)


#PATANLLA Y CLOCK FRAMES
pantalla = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Alien invaders")
clock = pygame.time.Clock()

#TIEMPO
timer_inicial = 60
fuente_timer = pygame.font.SysFont(None, 32)
timer_nivel = timer_inicial
texto_timer = f"Tiempo: {timer_nivel}"
pygame.time.set_timer(pygame.USEREVENT, 1000)

pantalla_inicio(botones_inicio)

mi_personaje = Personaje((posicion_x,posicion_y))

esqueleto = Enemigo((32,32),(340,223),'caminante',esqueleto_camina_der,(315,455))
lizard = Enemigo((32,32),(770,478),"estatico",lizard_dispara,(None,None),(None,None),True,lizard_fireball,fireball_explota)

fliying_eye_1 = Enemigo((32,32),(484,370),"volador",ojo_volador,(None,None),(260,460))
fliying_eye_2 = Enemigo((32,32),(298,370),"volador",ojo_volador,(None,None),(260,460))

bat_1 = Enemigo((48,48),(0,210),"caminante",bat_girado,(0,250))
bat_2 = Enemigo((48,48),(750,210),"caminante",bat_girado,(530,800))

lista_enemigos = [esqueleto,lizard,fliying_eye_1,fliying_eye_2,bat_1,bat_2]

plataforma_1 = Plataforma((133,16),(321,255))
plataforma_2 = Plataforma((53,16),(294,450))    
plataforma_3 = Plataforma((54,16),(480,450))
plataforma_4 = Plataforma((27,16),(586,345))
plataforma_5 = Plataforma((27,16),(161,345))
plataforma_6 = Plataforma((27,16),(534,255))
plataforma_7 = Plataforma((27,16),(214,255))
plataforma_8 = Plataforma((135,16),(0,255))
plataforma_9 = Plataforma((160,16),(640,255))

piso_2 = Plataforma((80,90),(375,510))
piso_3 = Plataforma((160,90),(640,510))

rectangulo_escalon_izq_1 = Plataforma((28,120),(160,480))
rectangulo_escalon_izq_2 = Plataforma((54,150),(187,450))
rectangulo_escalon_izq_3 = Plataforma((28,180),(240,420))

rectangulo_escalon_der_1 = Plataforma((28,180),(560,420))
rectangulo_escalon_der_2 = Plataforma((28,150),(587,450))
rectangulo_escalon_der_3 = Plataforma((26,120),(614,480))

lista_plataformas = [plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,
                    plataforma_6,plataforma_7,plataforma_8,plataforma_9,
                    piso_2,piso_3,rectangulo_escalon_izq_1,rectangulo_escalon_izq_2,
                    rectangulo_escalon_izq_3,rectangulo_escalon_der_1,rectangulo_escalon_der_2,rectangulo_escalon_der_3]


trampa_pinchos = Trampa((80,32),(374,485),spikes)
lista_trampas = [trampa_pinchos]


corazon_extra = PowerUp((16,16),(60,230),"vida_extra",corazon_extra)
battery = PowerUp((16,16),(402,472),"aumento_vel_y_salto",battery_powerup)

lista_powerups = [corazon_extra,battery]


pygame.mixer.music.load("source/Recursos/musica/SuperGrottoEscape.ogg")
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(0)

is_running = True
while is_running:
    clock.tick(FPS)
    pantalla.blit(mapa,(0,0))
    
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == pygame.USEREVENT:
            timer_nivel -= 1
            texto_timer = f"Tiempo: {timer_nivel}"
            if timer_nivel == 0 or mi_personaje.vidas == 0 or lista_enemigos == []:
                pantalla_fin(pantalla,botones_fin,mi_personaje.score)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()  
            if evento.key == pygame.K_ESCAPE:
                salir_juego()
    
    
    rectangulos_pantalla = limites_pantalla(pantalla)
    keys = pygame.key.get_pressed()
    
    mi_personaje.actualizar(keys, rectangulos_pantalla,lista_enemigos,lista_plataformas)
    mi_personaje.animar(pantalla)
    mi_personaje.aplicar_gravedad(lados_piso,lista_plataformas)
    mi_personaje.dibujar_balas(pantalla)
    mi_personaje.detectar_colision_enemigo(lista_enemigos)
    mi_personaje.actualizar_vida(pantalla)
    mi_personaje.dibujar_score(pantalla)    
    
    for enemigo in lista_enemigos:
        enemigo.actualizar(lista_plataformas,mi_personaje)
        enemigo.dibujar(pantalla)
        enemigo.dibujar_bala(pantalla)

    for trampa in lista_trampas:
        trampa.actualizar()
        trampa.dibujar(pantalla)
        trampa.detectar_colision(mi_personaje)
    
    for powerup in lista_powerups:
        powerup.dibujar(pantalla)
        powerup.detectar_colision(mi_personaje,lista_powerups)
    
    
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(pantalla,"orange",lados_piso[lado],1)
        
        for lado in piso_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"orange",piso_2.hitbox_plataforma[lado],1)
        
        for lado in piso_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"orange",piso_3.hitbox_plataforma[lado],1)
        
        for lado in mi_personaje.hitbox_personaje:
            pygame.draw.rect(pantalla, "red", mi_personaje.hitbox_personaje[lado], 1)
        
        for lado in esqueleto.hitbox_enemigo:
            pygame.draw.rect(pantalla,"red",esqueleto.hitbox_enemigo[lado],1)
        
        for lado in lizard.hitbox_enemigo:
            pygame.draw.rect(pantalla,"red",lizard.hitbox_enemigo[lado],1)
        
        for lado in fliying_eye_1.hitbox_enemigo:
            pygame.draw.rect(pantalla,"red",fliying_eye_1.hitbox_enemigo[lado],1)
        
        for lado in bat_1.hitbox_enemigo:
            pygame.draw.rect(pantalla,"red",bat_1.hitbox_enemigo[lado],1)
        
        
        for lado in plataforma_4.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_4.hitbox_plataforma[lado],1)
        
        for lado in plataforma_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_2.hitbox_plataforma[lado],1)
        
        for lado in plataforma_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_3.hitbox_plataforma[lado],1)
        
        for lado in plataforma_1.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_1.hitbox_plataforma[lado],1)
        
        for lado in plataforma_5.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_5.hitbox_plataforma[lado],1)
        
        for lado in plataforma_6.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_6.hitbox_plataforma[lado],1)
            
        for lado in plataforma_7.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_7.hitbox_plataforma[lado],1)
        
        for lado in plataforma_8.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_8.hitbox_plataforma[lado],1)
        
        for lado in plataforma_9.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_9.hitbox_plataforma[lado],1)
        
        
        for lado in rectangulo_escalon_der_1.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_der_1.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_der_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_der_2.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_der_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"white",rectangulo_escalon_der_3.hitbox_plataforma[lado],1)
        
        
        for lado in rectangulo_escalon_izq_1.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_izq_1.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_izq_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_izq_2.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_izq_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"white",rectangulo_escalon_izq_3.hitbox_plataforma[lado],1)
    
    
    texto_timer_surface = fuente_timer.render(texto_timer, True, (255, 0, 0))
    
    pantalla.blit(texto_timer_surface, (670,10))
    
    
    
    pygame.display.flip()

pygame.mixer.stop()

salir_juego()

