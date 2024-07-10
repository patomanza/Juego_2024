import pygame
from pygame.locals import *
from settings import *
from imagenes import *
from colisiones import *
from rectangulos import *
from modo_debug import *
from game_over import *
from clases import Personaje,Enemigo,Plataforma

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

# piso_3 = pygame.Rect(480,510,420,90)
# lados_piso_3 = obtener_rectangulos(piso_3)

#PATANLLA Y CLOCK FRAMES
pantalla = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")
clock = pygame.time.Clock()

#TIEMPO
timer_inicial = 60
fuente_timer = pygame.font.SysFont(None, 32)
timer_nivel = timer_inicial
texto_timer = f"Tiempo: {timer_nivel}"
pygame.time.set_timer(pygame.USEREVENT, 1000)

pantalla_inicio(botones_inicio)

mi_personaje = Personaje((posicion_x,posicion_y))

esqueleto = Enemigo((32,32),(360,300),'caminante',esqueleto_camina_der,(347,480))
lizard = Enemigo((32,32),(770,480),"estatico",lizard_dispara_der)
fliying_eye = Enemigo((48,48),(400,400),"volador",ojo_volador,(None,None),(340,500))

lista_enemigos = [esqueleto,lizard,fliying_eye]

plataforma_1 = Plataforma((133,16),(347,330))
plataforma_2 = Plataforma((53,16),(294,450))

piso_2 = Plataforma((80,90),(375,510))
piso_3 = Plataforma((240,90),(640,510))

rectangulo_escalon_izq_1 = Plataforma((28,120),(160,480))
rectangulo_escalon_izq_2 = Plataforma((54,150),(187,450))
rectangulo_escalon_izq_3 = Plataforma((28,180),(240,420))

rectangulo_escalon_der_1 = Plataforma((28,180),(560,420))
rectangulo_escalon_der_2 = Plataforma((28,150),(587,450))
rectangulo_escalon_der_3 = Plataforma((26,120),(614,480))

lista_plataformas = [plataforma_1,plataforma_2,piso_2,piso_3,
                    rectangulo_escalon_izq_1,rectangulo_escalon_izq_2,rectangulo_escalon_izq_3,
                    rectangulo_escalon_der_1,rectangulo_escalon_der_2,rectangulo_escalon_der_3]


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
            if timer_nivel == 0 or mi_personaje.vidas == 0:
                pantalla_fin(pantalla,botones_fin,mi_personaje.score)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()  
            if evento.key == pygame.K_ESCAPE:
                salir_juego()
    
    
    rectangulos_pantalla = limites_pantalla(pantalla)
    keys = pygame.key.get_pressed()
    
    mi_personaje.actualizar(keys, rectangulos_pantalla)
    mi_personaje.animar(pantalla)
    mi_personaje.aplicar_gravedad(lados_piso,lista_plataformas)
    mi_personaje.dibujar_balas(pantalla)
    mi_personaje.detectar_colision_enemigo(lista_enemigos)
    mi_personaje.actualizar_vida(pantalla)
    mi_personaje.dibujar_score(pantalla)
    
    for enemigo in lista_enemigos:
        enemigo.actualizar()
        enemigo.dibujar(pantalla)
    
    
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(pantalla,"orange",lados_piso[lado],1)
        
        for lado in piso_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"orange",piso_2.hitbox_plataforma[lado],1)
        
        for lado in piso_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"orange",piso_3.hitbox_plataforma[lado],1)
        
        for lado in mi_personaje.hitbox_personaje:
            pygame.draw.rect(pantalla, "red", mi_personaje.hitbox_personaje[lado], 1)
        
        # for lado in esqueleto.hitbox_enemigo:
        #     pygame.draw.rect(pantalla,"red",esqueleto.hitbox_enemigo[lado],1)
        
        # for lado in lizard.hitbox_enemigo:
        #     pygame.draw.rect(pantalla,"red",lizard.hitbox_enemigo[lado],1)
        
        # for lado in fliying_eye.hitbox_enemigo:
        #     pygame.draw.rect(pantalla,"red",fliying_eye.hitbox_enemigo[lado],1)
        
        for lado in plataforma_1.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_1.hitbox_plataforma[lado],1)
        
        for lado in plataforma_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",plataforma_2.hitbox_plataforma[lado],1)
        
        
        for lado in rectangulo_escalon_der_1.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_der_1.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_der_2.hitbox_plataforma:
            pygame.draw.rect(pantalla,"red",rectangulo_escalon_der_2.hitbox_plataforma[lado],1)
        
        for lado in rectangulo_escalon_der_3.hitbox_plataforma:
            pygame.draw.rect(pantalla,"white",rectangulo_escalon_der_3.hitbox_plataforma[lado],1)
    
    
    texto_timer_surface = fuente_timer.render(texto_timer, True, (255, 0, 0))
    
    pantalla.blit(texto_timer_surface, (670,10))
    
    
    pygame.display.flip()


salir_juego()

