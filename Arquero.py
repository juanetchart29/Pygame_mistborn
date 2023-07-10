import pygame
from Enemigo import Enemigo 
from Proyectil import Proyectil

class Arquero(Enemigo):
    
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagenes: dict,path_flecha:list) -> None:
        super().__init__(tamaño, posicion, diccionario_imagenes)

    
        self._path_flecha = path_flecha
        self._que_hace = "quieto"
        self._bandera_tiempo= pygame.time.get_ticks()
        self._cool_down = 2000
        self._tiempo_ahora = pygame.time.get_ticks()
        
        self._bandera_disparo = False
        self._lista_proyectiles = []
        
    
        
    def accion_enemigo(self,pantalla,un_personaje,lista_enemigos):
        self.puede_disparar(un_personaje)
        self.animar_arquero(pantalla)
        self.lanzar_flecha()
    
        self.blitear_proyectiles(pantalla)
        self.hacer_daño_distancia(un_personaje,lista_enemigos)
    
    def lanzar_flecha(self):
        if self._bandera_disparo == True:
            nuevo_proyectil = Proyectil((50,5),(self._rectangulo.x-10,self._rectangulo.y+16),self._path_flecha,7,-1)
            nuevo_proyectil._activo = True
            self._lista_proyectiles.append(nuevo_proyectil)
            self._bandera_disparo = False
            
    def arquero_muerto(self,pantalla,un_personaje,lista_enemigos):
        self.blitear_proyectiles(pantalla)
        self.hacer_daño_distancia(un_personaje,lista_enemigos)
          
                
    def puede_disparar(self,un_personaje):
        if (self._rectangulo.y + 30) in range(un_personaje._rectangulo.y,un_personaje._rectangulo.y+ un_personaje._tamaño[1]):
            self._tiempo_ahora = pygame.time.get_ticks()
            if self._tiempo_ahora - self._bandera_tiempo > self._cool_down:
                self._bandera_tiempo = self._tiempo_ahora
                self._que_hace = "dispara"
                
    
    
    def blitear_proyectiles(self,pantalla):
       
        self._lista_proyectiles = [proyectil for proyectil in self._lista_proyectiles if proyectil._activo]
        for proyectil in self._lista_proyectiles:
            proyectil.lanzar_proyectil()
            pantalla.blit(proyectil._imagen, (proyectil._rectangulo.x, proyectil._rectangulo.y))
            
    def hacer_daño_distancia(self,un_personaje,lista_enemigos):
        for flecha in self._lista_proyectiles:
            for enemigo in lista_enemigos:
                if enemigo._rectangulo.colliderect(flecha._rectangulo) and enemigo != self :
                    enemigo._vida -= 20      
                    flecha._activo = False
            if un_personaje._rectangulo.colliderect(flecha._rectangulo) and un_personaje._vida > 0:
                un_personaje._vida -= 20
                flecha._activo = False
    
    def animar_arquero(self,pantalla):
        
        imagenes_lista = self._dict_imagenes[self._que_hace]
        largo = len(imagenes_lista)
        if self._contador//12 >= largo:
            self._contador = 0
            if self._que_hace =="dispara":
                self._bandera_disparo = True
                self._que_hace = "quieto"
                print(self._que_hace)
                
        animacion = imagenes_lista[self._contador//12]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1

    