import pygame
from Enemigo import Enemigo


class Ogros(Enemigo):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagenes: dict,rango_movimiento_x:int,velocidad:int,tipo:str) -> None:
        super().__init__(tamaño, posicion, diccionario_imagenes)

        self._rango_movimiento = rango_movimiento_x
        self._vida = 120
        self._velocidad  = velocidad
        self._velocidad_x = velocidad
        
        self._velocidad_y = 0
        
        self._direccion = 1
        self._tipo = tipo
        
        self._bandera_lado = "derecha"
        
        if self._tipo == "vuelta":
            self._direccion *= -1
            self._bandera_lado = "izquierda"
            
        self._daño = 1
        #que movimiento
        #gravedad
        self._gravedad = -1
        
        self._bandera_piso = True
        
       
        #animacion
        self._que_hace = "camina_derecha_i"


    def accion_enemigo(self,un_personaje,pantalla,lista_plataformas:list):
        #se me ocurre filtrarlos desde un inicio por el tipo en vez de por la velocidad
            
        if self._velocidad_x >= 0:
            self._bandera_lado = "derecha"
            if self._rectangulo.colliderect(un_personaje._rectangulo):
                self._que_hace = "ataca_derecha_i"
                un_personaje._vida -= self._daño
            else:
                self._que_hace = "camina_derecha_i"
                if self._tipo == "ida_vuelta":
                    self.mover_enemigo_estable()
                else :
                    self._rectangulo.x += self._velocidad_x
                    self.movimiento_ogros(lista_plataformas)
                
        elif self._velocidad_x < 0:
            self._bandera_lado = "izquierda"    
            if self._rectangulo.colliderect(un_personaje._rectangulo):
                self._que_hace = "ataca_izquierda"
                un_personaje._vida -= self._daño
            else:
                self._que_hace = "camina_izquierda"
                if self._tipo == "ida_vuelta":
                    self.mover_enemigo_estable()
                else:
                    self._rectangulo.x += self._velocidad_x
                    self.movimiento_ogros(lista_plataformas)
                    
        self.animar_enemigo(pantalla)
            
           
    def movimiento_ogros(self,lista_plataformas):
        for plataforma in lista_plataformas:
            if self._rectangulo.colliderect(plataforma._lados["top"]):
                self._bandera_piso = True
                break
            else:
                self._bandera_piso = False
                
        self.verificar_colision_x(lista_plataformas)
                
        if self._bandera_piso == False:
            self._velocidad_y -= self._gravedad
            self._rectangulo.y += self._velocidad_y
            self._velocidad_x = 0
            
        else:
            self._velocidad_x = self._velocidad
            self._velocidad_y =  0
            
        self._lados = self.get_rectangulos()
        
            
            
    def verificar_colision_x(self,lista_plataformas):
        for plataforma in lista_plataformas:
      
            if plataforma._lados["right"].colliderect(self._lados["left"]) :
                if self._velocidad_x == 0:
                    pass
                elif self._velocidad_x < 0  : 
                    self._rectangulo.left = plataforma._rectangulo.right
                    self._velocidad *= -1
            if plataforma._lados["left"].colliderect(self._lados["right"]) :
                if self._velocidad_x == 0:
                    pass
                elif self._velocidad_x > 0  : 
                    self._rectangulo.right = plataforma._rectangulo.left
                    self._velocidad *= -1
                
        

        
            
            

    
    def mover_enemigo_estable(self):  
        if self._rectangulo.x + self._velocidad_x > self._posicion[0] + self._rango_movimiento:
            self._velocidad_x *= -1
        if self._rectangulo.x + self._velocidad_x < self._posicion[0] - self._rango_movimiento:
            self._velocidad_x *= -1
        
        self._rectangulo.x += self._velocidad_x
        
    
    def ataque_ogro(self,un_personaje):
        if self._velocidad_x >= 0:
            if self._rectangulo.colliderect(un_personaje._rectangulo):
                self._que_hace = "ataca_derecha_i"
                un_personaje._vida -= self._daño
        else:    
            if self._rectangulo.colliderect(un_personaje._rectangulo):
                self._que_hace = "ataca_izquierda"
                un_personaje._vida -= self._daño