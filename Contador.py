import pygame 
from Personaje import Personaje
from GameObject import GameObject



class Contador(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,lista_imagenes:list,un_personaje:Personaje) -> None:
        super().__init__(tamaño, posicion)
        
        self._mi_personaje = un_personaje
        self._lista_paths = lista_imagenes
        self._imagenes_lista = self.convertir_imagenes_lista()
        self._imagen_moneda = self._imagenes_lista[0]
        self._imagen_vida= self._imagenes_lista[1]
        
        self._vida = 100
        self._string1 = ""
        self._string2 = ""
        self.actualizar(un_personaje)
        self.fuente = pygame.font.Font(None, 50)
        self.color_texto = (255, 0, 0)
        self.posicion_texto1 = (self._posicion[0]+35,self._posicion[1])   
        self.posicion_texto2 = (self._posicion[0]+105,self._posicion[1])   
        
    
    def actualizar(self,un_personaje):
        self._cantidad = self._mi_personaje._monedas
        self._string1 = ":" + str(self._cantidad)
        self._vida = un_personaje._vida
        self._string2 = ":" + str(self._vida)
    
    def dibujar(self, screen):

        screen.blit(self._imagen_moneda,(self._posicion[0],self._posicion[1]))
        texto = self.fuente.render(self._string1, True, self.color_texto)
        screen.blit(texto, self.posicion_texto1)
        
        screen.blit(self._imagen_vida,(self._posicion[0]+70,self._posicion[1]))
        texto = self.fuente.render(self._string2, True, self.color_texto)
        screen.blit(texto, self.posicion_texto2)

    