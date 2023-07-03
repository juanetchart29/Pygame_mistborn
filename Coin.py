import pygame
from GameObject import GameObject


class Coin(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple, lista_imagen:list ,score:int) -> None:
        super().__init__(tamaño, posicion)
        self._score = score
        self._lista_paths = lista_imagen
        self._imagenes_lista = self.convertir_imagenes_lista()
        self._rectangulo = self._imagenes_lista[0].get_rect()
        self._rectangulo.x = posicion[0]
        self._rectangulo.y = posicion[1]
        self._contador = 0
        self._activo = True
        
    def animar_coin(self,pantalla): 
        
        largo = len(self._imagenes_lista)
        if self._contador/4 >= largo:
            self._contador = 0
        animacion = self._imagenes_lista[self._contador//4]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1
        
        
    