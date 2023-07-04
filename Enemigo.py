from GameObject import GameObject



class Enemigo(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,diccionario_imagenes:dict) -> None:
        super().__init__(tamaño, posicion)
        
        
        self._dict_path = diccionario_imagenes
        self._dict_imagenes = self.convertir_imagenes_diccioario()
        self.lista_imagen_inicial = next(iter(self._dict_imagenes.values()))
        self._imagen = self.lista_imagen_inicial[0]
        
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.x = self._posicion[0]
        self._rectangulo.y = self._posicion[1]
        

        
        self._contador =0

    
    
