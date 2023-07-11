from GameObject import GameObject
import pygame
from Personaje import Personaje

class Trampa(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,lista_imagen:list) -> None:
        super().__init__(tamaño, posicion)
        
        self._lista_paths = lista_imagen
        self._lista_imagenes = self.convertir_imagenes_lista()
        self._imagen = self._lista_imagenes[0]
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.x = self._posicion[0]
        self._rectangulo.y = self._posicion[1]
    
    def blitear_trampa(self,pantalla):
        pantalla.blit(self._imagen,self._posicion)
    
    
    def hacer_daño(self,un_personaje:Personaje,lista_enemigos):
        if self._rectangulo.colliderect(un_personaje._rectangulo):
            un_personaje._vida -= 2
            
            #para que las trampas o un golpe te corra para atras
            
            # if un_personaje._bandera_lado == "derecha":
            #     un_personaje._rectangulo.x -= 40
            # else :
            #     un_personaje._rectangulo.x += 40
                
        for enemigo in lista_enemigos:
            if self._rectangulo.colliderect(enemigo._rectangulo):
                enemigo._vida -= 1.8