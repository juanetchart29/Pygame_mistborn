from GameObject import GameObject



class Enemigo(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple,diccionario_imagenes:dict) -> None:
        super().__init__(tamaño, posicion)
        
        self._vida = 100
        
        self._dict_path = diccionario_imagenes
        try :
            self._dict_imagenes = self.convertir_imagenes_diccioario()
        except:
            self._dict_imagenes = self._dict_path
        self.lista_imagen_inicial = next(iter(self._dict_imagenes.values()))
        self._imagen = self.lista_imagen_inicial[0]
        
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.x = self._posicion[0]
        self._rectangulo.y = self._posicion[1]
        self._lados = self.get_rectangulos()
        
        

        
        self._contador =0
        
    def animar_enemigo(self,pantalla):
    
        imagenes_lista = self._dict_imagenes[self._que_hace]
        largo = len(imagenes_lista)
        if self._contador/4 >= largo:
            self._contador = 0
        animacion = imagenes_lista[self._contador//4]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1

    
    
