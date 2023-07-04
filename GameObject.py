import pygame





class GameObject :
    def __init__(self,tamaño:tuple,posicion:tuple) -> None:
        self._posicion = posicion
        self._tamaño = tamaño 
        #se puede eliminar
        self._rectangulo = "se asignan en las herencias"
        self._lista_paths = "se asigna en herencias"#esta bine esto para no copiar codigo ?
        self._dict_path = 0
        
        
    def get_rectangulos(self):
        diccionario = {}
        principal = self._rectangulo
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left,principal.bottom -6,principal.width,6)
        diccionario["right"] = pygame.Rect(principal.right -5,principal.top,16,principal.height)
        diccionario["left"] = pygame.Rect(principal.left,principal.top,6,principal.height)
        diccionario["top"] = pygame.Rect(principal.left,principal.top ,principal.width,10)#no tocar
        return diccionario

    def convertir_imagenes_lista(self):
        nueva_lista_imagenes = []
        for i in  range(len(self._lista_paths)): 
            imagen_cargada = pygame.image.load(self._lista_paths[i])
            imagen_cargada = pygame.transform.scale(imagen_cargada,self._tamaño)
            nueva_lista_imagenes.append(imagen_cargada)
        return nueva_lista_imagenes            


    def convertir_imagenes_diccioario(self):
        for keys,value in self._dict_path.items():
            nueva_lista_imagenes = []
            for ruta_imagen in value: 
                imagen_cargada = pygame.image.load(ruta_imagen)
                imagen_cargada = pygame.transform.scale(imagen_cargada,self._tamaño)
                #si la clave del diccionario termina con _i rota la imagen 
                if keys.endswith("_i"):
                    imagen_cargada = pygame.transform.flip(imagen_cargada,True,False) 
                    
                nueva_lista_imagenes.append(imagen_cargada)
                
            self._dict_path[keys] = nueva_lista_imagenes
        return self._dict_path
   
    
    