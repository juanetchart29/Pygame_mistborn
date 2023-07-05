import pygame
from Enemigo import Enemigo 
from Proyectil import Proyectil
from random import randint

class Arquero(Enemigo):
    
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagenes: dict) -> None:
        super().__init__(tamaño, posicion, diccionario_imagenes)

        self._que_hace = "quieto"
        self._bandera_tiempo= pygame.time.get_ticks()
        self._cool_down = 1000
        self._tiempo_ahora = pygame.time.get_ticks()
        
        self._bandera_disparo = True
        self._lista_proyectiles = []
        
    def accion_arquero(self,pantalla,un_personaje):
        if (self._rectangulo.y - 16) in range(un_personaje._rectangulo.y,un_personaje._rectangulo.y+ un_personaje._tamaño[1]):
            self._tiempo_ahora = pygame.time.get_ticks()
            if self._tiempo_ahora - self._bandera_tiempo > self._cool_down:
                self._que_hace = "dispara"
                self.lanzar_flecha()
        
        
        
    
    
        self.blitear_proyectiles(self,pantalla)
        self.hacer_daño_distancia(un_personaje)
    
    def lanzar_flecha(self):
        if self._bandera_disparo == True:
            nuevo_proyectil = Proyectil((50,5),(self._rectangulo.x-10,self._rectangulo.y+16),self._dict_imagenes["flecha"],randint(1,7),-1)
            self._lista_proyectiles.append(nuevo_proyectil)
            
        
                
    
    
    def blitear_proyectiles(self,pantalla):
       
        self._lista_proyectiles = [proyectil for proyectil in self._lista_proyectiles if proyectil._activo]
        for proyectil in self._lista_proyectiles:
            proyectil.lanzar_proyectil()
            pantalla.blit(proyectil._imagen, (proyectil._rectangulo.x, proyectil._rectangulo.y))
            
    def hacer_daño_distancia(self,un_personaje):
        for flecha in self._lista_proyectiles:
                          
            if un_personaje._rectangulo.colliderect(flecha._rectangulo) and un_personaje._vida > 0:
                un_personaje._vida -= 20
                flecha._activo = False
    
    def animacion_disparar(self,pantalla):
        imagenes_lista = self._dict_imagenes[self._que_hace]
        largo = len(imagenes_lista)
        if self._contador/4 >= largo:
            self._contador = 0
            self._bandera_disparo = False
        animacion = imagenes_lista[self._contador//4]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1

    