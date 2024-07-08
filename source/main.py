import pygame
from pygame.locals import *
from settings import *
from imagenes import *
from colisiones import *
from sys import exit
from rectangulos import *
from modo_debug import *




#PISO 800*60

#https://www.onlinegdb.com/lSg2Dbq1R

def salir_juego():
    pygame.quit()
    exit()
    



def pantalla_inicio(botones):
    continuar = True

    pygame.mixer.music.load("source\Recursos\musica\star_wars_soundtrack.wav")
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


def reiniciar_juego():
    global timer_nivel, texto_timer

    timer_nivel = timer_inicial  # Reinicia el timer al valor inicial
    texto_timer = f"Tiempo: {timer_nivel}"


def pantalla_fin(botones, puntuacion_final):
    continuar = True
    
    pantalla.blit(fondo, (0, 0))
    
    fuente_puntuacion = pygame.font.SysFont(None, 48)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación final: {puntuacion_final}", True, (255, 255, 255))
    texto_puntuacion_rect = texto_puntuacion.get_rect(center= (WIDTH// 2, HEIGHT // 3))
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir_juego()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos, rect):
                        if boton == "start":
                            reiniciar_juego()
                            continuar = False
                        elif boton == "exit":
                            salir_juego()
        
        
        
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto_puntuacion, texto_puntuacion_rect)
        pantalla.blit(start_button, (button_x, start_button_y))  # Botón para volver a jugar
        pantalla.blit(exit_button, (button_x, exit_button_y))    # Botón para salir del juego
        
        pygame.display.flip()
    
    pygame.mixer.music.stop()

def aplicar_gravedad(salta:bool):
    
    if hitbox_personaje['main'].colliderect(lados_piso['top']):
        desplazamiento_y = 0
        gravedad = 2
        salta = False
        hitbox_personaje['main'].bottom = lados_piso['top'].bottom
    elif salta:
        desplazamiento_y += gravedad
        for lado in hitbox_personaje:
            hitbox_personaje[lado].y += desplazamiento_y
        
        if desplazamiento_y > velocidad_caida:
            desplazamiento_y = velocidad_caida






pygame.init()

#TEXTO
fuente_score = pygame.font.SysFont(None,32)
texto_score = fuente_score.render("Score: ",True, RED)
score = 0

# PISO
piso = pygame.Rect(0,510,267,90)
lados_piso = obtener_rectangulos(piso)
piso_2 = pygame.Rect(347,510,53,90)
lados_piso_2 = obtener_rectangulos(piso_2)
piso_3 = pygame.Rect(480,510,420,90)
lados_piso_3 = obtener_rectangulos(piso_3)


#PATANLLA Y CLOCK FRAMES
pantalla = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")
clock = pygame.time.Clock()

#TIEMPO
timer_inicial = 30
fuente_timer = pygame.font.SysFont(None, 32)
timer_nivel = timer_inicial
texto_timer = f"Tiempo: {timer_nivel}"
pygame.time.set_timer(pygame.USEREVENT, 1000)

pantalla_inicio(botones_inicio)
que_hace = 'quieto'

is_running = True
while is_running:
    clock.tick(FPS)
    
    #bliteos pantalla
    pantalla.blit(texto_score,(365,50))
    pantalla.blit(mapa,(0,0))
    hitbox_personaje = obtener_rectangulos(personaje_pos)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == pygame.USEREVENT:
            timer_nivel -= 1
            texto_timer = f"Tiempo: {timer_nivel}"
            if timer_nivel == 0:
                pantalla_fin(botones_fin,score)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()  
    
    
    
    keys = pygame.key.get_pressed()
    is_moving = False
    
    
    #   MOVIMIENTO
    if keys[pygame.K_RIGHT] and hitbox_personaje["right"].x < rectangulos_pantalla["right"].right - velocidad_x:
        personaje_pos.x += velocidad_x
        is_moving = True
        direccion = 'derecha'
    elif keys[pygame.K_LEFT] and hitbox_personaje["left"].x > rectangulos_pantalla["left"].left + velocidad_x:
        personaje_pos.x -= velocidad_x
        is_moving = True
        direccion = 'izquierda'
    elif keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        desplazamiento_y = potencia_salto
    
    
    
    # hitbox_personaje["main"].bottom = lados_piso["top"].bottom
    
    rectangulos_pantalla = limites_pantalla(pantalla)
    
    if is_moving:
        anim_counter += 1
        if anim_counter >= anim_correr_speed:
            anim_counter = 0
            anim_index = (anim_index + 1) % len(personaje_corre)
    elif is_jumping:
        anim_counter += 1
        if anim_counter >= anim_saltar_speed:
            anim_counter = 0
            anim_index = (anim_index + 1) % len(personaje_salta)
    else:
        anim_counter += 1
        if anim_counter >= anim_idle_speed:
            anim_counter = 0
            anim_index = (anim_index + 1) % len(personaje_idle)
    
    
    #ANIMACION IDLE Y CORRER
    if is_moving and not is_jumping: 
        if direccion == 'derecha':
            pantalla.blit(personaje_corre[anim_index], personaje_pos.topleft)
        else:
            pantalla.blit(personaje_corre_izq[anim_index], personaje_pos.topleft)
    elif is_jumping:
        if direccion == 'derecha':
            pantalla.blit(personaje_salta[anim_index],personaje_pos.topleft)
        else: 
            pantalla.blit(personaje_salta_izq[anim_index],personaje_pos.topleft)
    else:
        if direccion == 'derecha':
            pantalla.blit(personaje_idle[anim_index], personaje_pos.topleft)
        else:
            pantalla.blit(personaje_idle_izq[anim_index], personaje_pos.topleft)
    
    
    # control de gravedad
    
    if is_jumping and direccion == 'derecha':
        print(is_jumping)
        pantalla.blit(personaje_salta[anim_index],personaje_pos.topleft)
        for lado in hitbox_personaje:
            hitbox_personaje[lado].y += desplazamiento_y
        
        if desplazamiento_y + gravedad < velocidad_caida:
            desplazamiento_y += gravedad
    elif is_jumping and direccion == 'izquierda':
        print(is_jumping)
        pantalla.blit(personaje_salta_izq[anim_index],personaje_pos.topleft)
        for lado in hitbox_personaje:
            hitbox_personaje[lado].y += desplazamiento_y
        
        if desplazamiento_y + gravedad < velocidad_caida:
            desplazamiento_y += gravedad
    if hitbox_personaje['main'].colliderect(lados_piso['top']):
        print(is_jumping)
        desplazamiento_y = 0
        gravedad = 1
        is_jumping = False
        hitbox_personaje['main'].bottom = lados_piso['top'].bottom
    
    
    
    
    
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(pantalla,"orange",lados_piso[lado],1)
        
        for lado in lados_piso_2:
            pygame.draw.rect(pantalla,"orange",lados_piso_2[lado],1)
        
        for lado in lados_piso_3:
            pygame.draw.rect(pantalla,"orange",lados_piso_3[lado],1)
        
        for lado in hitbox_personaje:
            pygame.draw.rect(pantalla, "red", hitbox_personaje[lado], 1)
        
        for lado in rectangulos_pantalla:
            pygame.draw.rect(pantalla,"blue",rectangulos_pantalla[lado],1)
    
    texto_timer_surface = fuente_timer.render(texto_timer, True, (255, 0, 0))
    
    pantalla.blit(texto_timer_surface, (670,10))
    
    pygame.display.flip()


salir_juego()

