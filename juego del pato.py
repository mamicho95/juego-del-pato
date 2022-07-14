import sys, pygame
from pygame.locals import *
from time import sleep
from random import randint
import  time
WIDTH = 800
HEIGHT = 600
pygame.init()
pygame.display.set_caption("Pato McDonald")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ms=pygame.font.SysFont("Pixel Bug",40)
mensaje=ms.render("Press SPACE To Reset ",0,(255,255,255))
over=pygame.mixer.Sound("sonido/perdiste.wav") 
verti =400
hori =10
cont=6
direc=True
jugable=True
i=0
sprites={}
puntos=0
cronometro=0
vidas=3
dificultad=0

#=================IMAGEN====================================

def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error and message:
                raise SystemExit and message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
perdiste = imagen("imagenes/gameover.jpg")
perdiste = pygame.transform.scale(perdiste, (WIDTH, HEIGHT))
#======================TECLADO===============================

def teclado():
    teclado = pygame.key.get_pressed()
    global cont, direc,hori,verti     
    if teclado[K_d]:
        hori+=7
        if hori>730:
                hori-=7        
        direc=True
    if teclado[K_a]:
        hori-=7
        if hori<0:
                hori+=7
        direc=False
    if teclado[K_w]:
        verti-=7
        if verti<0:
                verti+=7
    if teclado[K_s]:
        verti+=7
        if verti>430:
                verti-=7   
    return 

class enemy:
    def __init__(self,p,i):
        self.pantalla=p
        self.imagen=i
        self.x=-120
        self.y=(randint(0,695))
    def aparecer(self):
        self.y=self.y+6    
        if self.y>=395:
                self.y=-180
                self.x=(randint(0,695))            
        img = pygame.transform.scale(self.imagen, (100, 100))
        self.pantalla.blit(img, ( self.x, self.y))
    def colision(self,perder):

        global vidas,hori,verti,direc,dificultad
        if hori+40>self.x and hori<self.x+70 and verti+30>self.y and verti<self.y+60 :
                verti=400
                hori=10
                direc=True
                vidas=vidas-1
                dificultad=0
                self.y=-120
                self.x=(randint(0,695))
                pygame.mixer.music.stop()
                perder.play()
                sleep(3)
                pygame.mixer.music.play(-1)        

def sprite():
    global cont
    sprites[0]=(143,0,215,66)
    sprites[1]=(0,0,71,66)
    p=6
    global i 
    if cont==p:
        i=0
    if cont==p*2:
        i=1
        cont=0
    return

def main():
    global hori,verti,direc,cont,puntos,cronometro,vidas,dificultad
    pygame.mixer.music.load("sonido/fondo.mp3")
    pygame.mixer.music.play(-1)
    fuente=pygame.font.SysFont("Pixel Bug",25)
    score=pygame.font.SysFont("Pixel Bug",25)
    vida=pygame.font.SysFont("Pixel Bug",25)
    fondo = imagen("imagenes/fondo1.png")
    puntos=0
    cronometro=0
    vidas=3
    tiempo=0
    ####################pato####################
    mario = imagen("imagenes/sprites_mario.png",True)    
    mario_inv=pygame.transform.flip(mario,True,False);
    cuac=pygame.mixer.Sound("sonido/patocuac.wav")
    perder=pygame.mixer.Sound("sonido/perder.wav")    
    ##################enemigo###################
    by=(randint(0,390))
    bx=(randint(0,695))  
    enemigo = imagen("imagenes/enemigo.png",True)
    bonus = imagen("imagenes/bonus.png",True)  
    clock = pygame.time.Clock()
    fps=0
    caca=enemy(screen,enemigo)
    caca1=enemy(screen,enemigo)
    caca2=enemy(screen,enemigo)
    caca3=enemy(screen,enemigo)
    caca4=enemy(screen,enemigo)
    caca5=enemy(screen,enemigo)
    caca6=enemy(screen,enemigo)
    caca7=enemy(screen,enemigo)
    caca8=enemy(screen,enemigo)
    caca9=enemy(screen,enemigo)
    caca.y=-100
    caca1.y=-200
    caca2.y=-300
    caca3.y=-400
    caca4.y=-500
    caca5.y=-600
    segundos=0
    while True:
        cont=cont+1
        segundos=segundos+1
        dificultad=dificultad+1
        tiempo=round((segundos/6)/10)
        cronometro=tiempo
        sprite()
        teclado()
        time = clock.tick(60)
        reloj=fuente.render("Time "+str(tiempo),0,(255,255,255))
        puntaje=score.render("Score  "+str(puntos),0,(255,255,255))
        life=vida.render("Lives "+str(vidas),0,(255,255,255))
        fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
        enemigo = pygame.transform.scale(enemigo, (100, 100))
        enemigo1 = pygame.transform.scale(enemigo, (100, 100))
        bonus = pygame.transform.scale(bonus, (100, 100))
        screen.blit(fondo, (0, 0))
        screen.blit(reloj, ( 610, 550))
        screen.blit(puntaje, ( 220, 550))
        screen.blit(life, ( 55, 550))
        if fps==140:
              by=(randint(0,390))
              bx=(randint(0,695))
              fps=0
        fps=fps+1      
        screen.blit(bonus, ( bx, by))
        caca.colision(perder) 
        caca.aparecer()
        caca1.colision(perder) 
        caca1.aparecer()
        caca2.colision(perder) 
        caca2.aparecer()
        caca3.colision(perder) 
        caca3.aparecer()
        caca4.colision(perder) 
        caca4.aparecer()
        caca5.colision(perder) 
        caca5.aparecer()
        if dificultad==0:
            caca.y=-100
            caca1.y=-200
            caca2.y=-300
            caca3.y=-400
            caca4.y=-500
            caca5.y=-600
        if direc==True: 
            screen.blit(mario, (hori,verti),(sprites[i]))
        if direc==False: 
            screen.blit(mario_inv, ( hori, verti),(sprites[i]))
        if hori+40>bx and hori<bx+70 and verti+30>by and verti<by+60 :
              by=(randint(0,390))
              bx=(randint(0,695))
              fps=0
              puntos=puntos+100
              cuac.play()
        pygame.display.flip()
        if vidas==0:
               over.play() 
        while vidas==0:
                pygame.display.update()
                pygame.mixer.music.stop()
                screen.blit(perdiste, ( 0, 0))
                screen.blit(reloj, ( 350, 390))
                screen.blit(puntaje, ( 350, 350))
                screen.blit(mensaje, ( 200, 500))
                
                for acto in pygame.event.get():
                    if acto.type == pygame.QUIT:
                        exit()
                    if acto.type == pygame.KEYDOWN:
                        if acto.key == pygame.K_SPACE :
                            over.stop()
                            main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    return 0 

main()
