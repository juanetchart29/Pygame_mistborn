from GameObject import GameObject
import pygame

class Portal(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,path_portal:list) -> None:
        super().__init__(tamaño, posicion)
        
        
        self._lista_paths = path_portal
        self._lista_imagenes = self.convertir_imagenes_lista()
        self._imagen = self._lista_imagenes[0]
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.x = self._posicion[0]
        self._rectangulo.y = self._posicion[1]
        
        self._next_lvl = False
        
    def funciones_portal(self,un_personaje,pantalla):
        self.avanzar_nivel(un_personaje)
        self.blitear_portal(pantalla)    
        
        
        
    def avanzar_nivel(self,un_personaje):
        if self._rectangulo.colliderect(un_personaje._rectangulo):
            self._next_lvl = True
        else:
            self._next_lvl = False
            
    def blitear_portal(self,pantalla):
        pantalla.blit(self._imagen,self._posicion)