import pygame 
from Personaje import Personaje
from GameObject import GameObject


class Contador(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,lista_imagenes:list,un_personaje:Personaje) -> None:
        super().__init__(tamaño, posicion)
        
        self._mi_personaje = un_personaje
        self._lista_paths = lista_imagenes
        self._imagenes_lista = self.convertir_imagenes_lista()
        self._imagen = self._imagenes_lista[0]
        
        self._string = ""
        self.actualizar()
        self.fuente = pygame.font.Font(None, 50)
        self.color_texto = (255, 0, 0)
        self.posicion_texto = (100, 0)    
    
    
    def actualizar(self):
        self._cantidad = self._mi_personaje._monedas
        self._string = "=" + str(self._cantidad)
    
    def dibujar(self, screen):
        
        screen.blit(self._imagen,(self._posicion[0],self._posicion[1]))
        texto = self.fuente.render(self._string, True, self.color_texto)
        screen.blit(texto, self.posicion_texto)

