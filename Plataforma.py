import pygame
from GameObject import GameObject


class Plataforma(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,lista_paths:list ) -> None:
        super().__init__(tamaño, posicion)
        
        self._lista_paths = lista_paths
        #lista de imagenes escaladas 
        if len(lista_paths) > 0:
            self._lista_imagenes = self.convertir_imagenes_lista()
            self._imagen = self._lista_imagenes[0]
            self._rectangulo = self._imagen.get_rect()
            self._rectangulo.x = self._posicion[0]
            self._rectangulo.y = self._posicion[1]
            
        else:
            self._rectangulo = pygame.Rect(self._posicion[0],self._posicion[1],self._tamaño[0],self._tamaño[1])
        #defino los rectangulos
        self._lados = self.get_rectangulos()

        


        

        
    
        
        
        
