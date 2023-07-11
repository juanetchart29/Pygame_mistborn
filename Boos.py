import pygame
from Enemigo import Enemigo
from random import randint 
from Proyectil import Proyectil


class Boos(Enemigo):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagenes: dict,velocidad:int,lista_path_proyectil) -> None:
        super().__init__(tamaño, posicion, diccionario_imagenes)
        self._patron = 1
        
        self._vida = 800
        self._velocidad_x = velocidad

        self._modulo_velocidad = velocidad
        self._direccion = -1
        
        self._path_proyectil= lista_path_proyectil
        self._lista_proyectiles = []
        
        self._bandera_tiempo= pygame.time.get_ticks()
        self._coul_down = 600
        self._tiempo_ahora = pygame.time.get_ticks()
        
        #could down ataque
        self._bandera_tiempo_ataque= pygame.time.get_ticks()
        self._coul_down_ataque = 400
        self._tiempo_ahora_ataque = pygame.time.get_ticks()
        
        
        
    def accion_enemigo(self,pantalla,lista_plataformas,lista_enemigos,un_personaje):
        if self._vida > 0:
            self.movimiento_jefe(lista_plataformas)
            self.lanzar_proyectil(un_personaje)
            self.blitear_proyectiles(pantalla)
            self.hacer_daño_distancia(un_personaje,lista_enemigos)
            pantalla.blit(self._dict_imagenes["enemigo"][0],(self._rectangulo.x,self._rectangulo.y))
    
    def ataque_jefe(self,lista_enemigos):
        for enemigo in lista_enemigos:
            if enemigo != self:
                pass     

    def lanzar_proyectil(self,un_personaje):
        if un_personaje._rectangulo.x in range(int(self._rectangulo.x),int(self._rectangulo.x+self._posicion[0])):
            self._tiempo_ahora_ataque = pygame.time.get_ticks()
            if self._tiempo_ahora_ataque - self._bandera_tiempo_ataque >self._coul_down_ataque :
                self._bandera_tiempo_ataque = self._tiempo_ahora_ataque
                print("entra")
                nuevo_proyectil = Proyectil((40,40),(self._rectangulo.x+self._tamaño[0]/2,self._rectangulo.y+self._tamaño[1]),self._path_proyectil,10,-2)
                nuevo_proyectil._activo = True
                self._lista_proyectiles.append(nuevo_proyectil)
            
    def hacer_daño_distancia(self,un_personaje,lista_enemigos):
        for flecha in self._lista_proyectiles:
            for enemigo in lista_enemigos:
                if enemigo._rectangulo.colliderect(flecha._rectangulo) and enemigo != self and enemigo._vida > 0:
                    enemigo._vida -= 120      
                    flecha._activo = False
            if un_personaje._rectangulo.colliderect(flecha._rectangulo) and un_personaje._vida > 0:
                un_personaje._vida -= 50
                flecha._activo = False        
            
    def blitear_proyectiles(self,pantalla):
        self._lista_proyectiles = [proyectil for proyectil in self._lista_proyectiles if proyectil._activo]
        for proyectil in self._lista_proyectiles:
            proyectil.lanzar_proyectil()
            pantalla.blit(proyectil._imagen, (proyectil._rectangulo.x, proyectil._rectangulo.y))
            
    def movimiento_jefe(self,lista_plataformas:list):
        self._rectangulo.x += self._velocidad_x
        if self._tiempo_ahora - self._bandera_tiempo > self._coul_down:
            self._patron = int(randint(1,3))
        if self._patron == 3:
            self._velocidad_x = 0
        else:
            if self._patron % 2 == 0:
                self._direccion*= -1    
            self._velocidad_x = self._modulo_velocidad * self._direccion
        self.verificar_colision_x(lista_plataformas)
        self._lados = self.get_rectangulos()
        
        
    def verificar_colision_x(self,lista_plataformas):
        for plataforma in lista_plataformas:
      
            if plataforma._lados["right"].colliderect(self._lados["left"]) :
                if self._velocidad_x < 0  : 
                    self._rectangulo.left = plataforma._rectangulo.right
                    self._direccion *= -1
            if plataforma._lados["left"].colliderect(self._lados["right"]) :
                if self._velocidad_x == 0:
                    pass
                elif self._velocidad_x > 0  : 
                    self._rectangulo.right = plataforma._rectangulo.left
                    self._direccion *= -1
                
        