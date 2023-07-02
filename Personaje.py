import pygame
import re
from settings import *
from GameObject import GameObject
from Plataforma import Plataforma
from Proyectil import Proyectil



class Personaje(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_paths: dict,contador_pasos:int,nombre:str,potencia_salto : int,daño_ataque :int,score:int) -> None:
        super().__init__(tamaño, posicion)
        
    #IMAGENES
        self._dict_path = diccionario_paths
        self._dict_imagenes = self.convertir_imagenes_diccioario()
        #establezco la primer lista del diccionario
        self.lista_imagen_inicial = next(iter(self._dict_imagenes.values()))
        #establezco la primer imagen como el elemento [0] de la primer lista
        #para obtener los rectangulos
        self._imagen = self.lista_imagen_inicial[0]
        
    #RECTANGULOS            
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.center = self._posicion
        self._lados = self.get_rectangulos()
    
    #MOVIMIENTO X
        self._contador_pasos = 0
        self._que_hace = "quieto_d"
        self._bandera_lado = "derecha"
        self._velocidad_x = 0
        self._contador_pasos = contador_pasos
        
    #MOVIMIENTO Y (GRAVEDAD)
        self._velocidad_y = 0
        self._potencia_salto = -potencia_salto
        self._bandera_suelo = True
        self._aceleracion = 2
        
    #USUARIO
        self._nombre = nombre 
        self._vida = 100
        self._daño_ataque = daño_ataque
        self._score = score
   
#---imagenes
    #cargo las imagenes de las listas de los diccionarios y las escalo.
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
#/--imagenes
   
    #ANIMAR IMAGENES
    def animar(self,pantalla):
        animacion = self._dict_path[self._que_hace]
        largo = len(animacion)
        
        if self._contador_pasos >= largo:
            self._contador_pasos = 0
        
        pantalla.blit(animacion[self._contador_pasos],self._rectangulo)
        self._contador_pasos += 1
        

        
        
        
    #MUEVO AL PERSONAJE SEGUN SELF._QUE_HACE Y LO ANIMO
    def update(self,pantalla,proyectil):
        match self._que_hace:
            case "corre_d":
                self.mover_personaje_x(1)
            case "corre_i":
                self.mover_personaje_x(-1)
            case "salta_i":
                if self._bandera_suelo:
                    self._velocidad_y= self._potencia_salto
                self._bandera_suelo = False
            case "salta_d":
                if self._bandera_suelo:
                    self._velocidad_y= self._potencia_salto
                self._bandera_suelo = False
            case "empujando_d":
                proyectil._lanzar_proyectil(1)
            case "empujando_i":
                proyectil._lanzar_proyectil(-1)
                
        self.animar(pantalla)
    
    #mUEVO EL RECTANGULO EN EL EJE X
    def mover_personaje_x(self,x):
        if x == 1 and (self._rectangulo.x + self._velocidad_x)< W:
            for lado in self._lados:
                self._lados[lado].x += self._velocidad_x
        
        elif x == -1 and (self._rectangulo.x - self._velocidad_x)> 0:
            for lado in self._lados:
                self._lados[lado].x -= self._velocidad_x
   
  
    
#    #animo como empuja el proyectil
#     def proyectil(self,pantalla):
#         if self._bandera_lado == "derecha":
#             self._que_hace = "empujando_d"            
#         else:
#             self._que_hace = "empujando_i"
#         self.anima(pantalla)
            
    
          
 
    #APLICO GRAVEDAD
    def aplicar_gravedad(self,pantalla,piso:Plataforma):  
        #si esta en el aire
        if (self._bandera_suelo == False):
            if self._velocidad_y < 0 :
                if self._bandera_lado == "derecha":
                    self._que_hace = "salta_d" 
                    self.animar(pantalla)
                if self._bandera_lado == "izquierda":
                    self._que_hace = "salta_i" 
                    self.animar(pantalla)
                
            if self._velocidad_y == 0:
                self._que_hace = "suspendido" 
                self.animar(pantalla)
            
            if self._velocidad_y > 0 :
                if self._bandera_lado == "derecha":
                    self._que_hace = "cae_d" 
                    self.animar(pantalla)
                if self._bandera_lado == "izquierda":
                    self._que_hace = "cae_i" 
                    self.animar(pantalla)
                    
            for lado in self._lados:
                self._lados[lado].y += self._velocidad_y
             
            if self._velocidad_y + self._aceleracion < -(self._potencia_salto):
                self._velocidad_y += self._aceleracion 
        

        #si colisiona con una plataforma 
        if self._rectangulo.colliderect(piso._rectangulo): 
            if self._rectangulo.colliderect(piso._lados["left"]):

                print("auxilio")
            
         
            elif self._rectangulo.colliderect(piso._lados["top"]):
                self._bandera_suelo = True
                self._velocidad_y = 0
                self._rectangulo.bottom = piso._rectangulo.top + 5
        else: 
            self._bandera_suelo = False

            
        # if self._rectangulo.colliderect(piso._lados["right"]):
        #     self._velocidad_x = 0
        #     self._rectangulo.left = piso._rectangulo.right +5
            
        # if self._rectangulo.colliderect(piso._lados["bottom"]):
        #     self._velocidad_y = 0
        #     self._rectangulo.top = piso._rectangulo.bottom +5



       
    
        self._lados = self.get_rectangulos()