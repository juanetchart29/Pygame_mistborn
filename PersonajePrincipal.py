
from Personaje import Personaje


class PersonajePrincipal(Personaje):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagen: dict, contador_pasos: int, nombre: str,potencia_salto:int,score:int,daño_ataque:int) -> None:
        super().__init__(tamaño, posicion, diccionario_imagen, contador_pasos, nombre,potencia_salto)
        
        self._score = score 
        self._daño_ataque = daño_ataque 
           
    
    
    
    def colision_objeto(self):
        pass
