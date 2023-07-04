import pygame
import re
from settings import *
from GameObject import GameObject
from Plataforma import Plataforma
from Proyectil import Proyectil
from Coin import Coin


class Personaje(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_paths: dict,contador_pasos:int,nombre:str,potencia_salto : int,daño_ataque :int,score:int,lista_imagen_proyectil:list) -> None:
        super().__init__(tamaño, posicion)
        
    #IMAGENES
        self._dict_path = diccionario_paths
        self._dict_imagenes = self.convertir_imagenes_diccioario()
        #establezco la primer lista del diccionario
        self.lista_imagen_inicial = next(iter(self._dict_imagenes.values()))
        #establezco la primer imagen como el elemento [0] de la primer lista
        #para obtener los rectangulos
        self._imagen = self.lista_imagen_inicial[0]
        self._imagen_proyectil = lista_imagen_proyectil
        
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
        self._potencia_super_salto = -20
    #PROYECTILES 
        self._lista_proyectiles = []
        self._call_down = True
     
    #USUARIO
        self._contador = 0
        self._nombre = nombre 
        self._vida = 100
        self._daño_ataque = daño_ataque
        self._score = score
        self._monedas = 0
    #BANDERAS
        self._con_vida = True
        self._bandera_ataque = False
    #TAMAÑO ATAQUE 
        self._tamaño_ataque = (100,90)

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
    def update(self,pantalla,lista_enemigos:list,lista_plataformas):
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
                self.tirar_proyectil(pantalla,1)
            case "empujando_i":
                self.tirar_proyectil(pantalla,-1)
    
        self.atacar(pantalla,lista_enemigos)
        self.ataque_proyectil(pantalla,lista_enemigos,lista_plataformas)
        
    
    #mUEVO EL RECTANGULO EN EL EJE X
    def mover_personaje_x(self,x):
        if x == 1 and (self._rectangulo.x + self._velocidad_x)< W:
            for lado in self._lados:
                self._lados[lado].x += self._velocidad_x
        
        elif x == -1 and (self._rectangulo.x - self._velocidad_x)> 0:
            for lado in self._lados:
                self._lados[lado].x -= self._velocidad_x
   
  

            
    def verificar_colision_x(self,lista_plataformas:list):
        for plataforma in lista_plataformas:
            if plataforma._lados["right"].colliderect(self._lados["left"]) and self._bandera_lado =="izquierda" :
                self._velocidad_x = 0
            if plataforma._lados["left"].colliderect(self._lados["right"]) and self._bandera_lado == "derecha":
                self._velocidad_x = 0
            if plataforma._lados["bottom"].colliderect(self._lados["top"]):
                self._rectangulo.top = plataforma._rectangulo.bottom +1
                self._velocidad_y = -1
          
 
    #APLICO GRAVEDAD
    def aplicar_gravedad(self,pantalla,piso:Plataforma,lista_plataformas):  
        #si esta en el aire
        
        if (self._bandera_suelo == False):
            self.verificar_colision_x(lista_plataformas)
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
        
        
        self.verificar_colision_x(lista_plataformas)
        
        if piso._lados["top"].colliderect(self._rectangulo):
            self._bandera_suelo = True
            self._velocidad_y = 0
            self._rectangulo.bottom = piso._rectangulo.top + 3
        else: 
            self._bandera_suelo = False
        #si colisiona con una piso 
       

            

        self._lados = self.get_rectangulos()
        
        
    #ver como hacer para que haga la animacion 
    def tirar_proyectil(self,pantalla,x):
                 
        if self._que_hace.startswith("empujando_")  :
                # self.animacion_especifica(pantalla)
            if self._call_down == True:
                proyectil_vin = Proyectil((15,15),(self._rectangulo.x+self._tamaño[0],self._rectangulo.y+self._tamaño[1]/2),self._imagen_proyectil,40,x)
                proyectil_vin._activo = True
                self._lista_proyectiles.append(proyectil_vin)
        else: 
            self._call_down = False
        
    def blitear_proyectiles(self,pantalla):
        self._lista_proyectiles = [proyectil for proyectil in self._lista_proyectiles if proyectil._activo]
        for proyectil in self._lista_proyectiles:
            proyectil.lanzar_proyectil()
            pantalla.blit(proyectil._imagen, (proyectil._rectangulo.x, proyectil._rectangulo.y))
            
    def ataque_proyectil(self,pantalla,lista_enemigos,lista_plataformas):
    
        self.blitear_proyectiles(pantalla)
        self.hacer_daño_distancia(lista_enemigos)
        self.chocar_proyectil_plataforma(lista_plataformas)
        

    def agarrar_moneda(self,moneda:Coin):
        if self._rectangulo.colliderect(moneda._rectangulo):
            moneda._activo = False
            self._monedas += 1
            if moneda._cura:
                if self._vida +50 > 100:
                    
                    self._vida = 100
                else:
                    self._vida+= 50
    
    
    def animacion_especifica(self,pantalla):
        imagenes_lista = self._dict_imagenes[self._que_hace]
        largo = len(imagenes_lista)
        if self._contador//4 >= largo:
            self._contador = 0
        animacion = imagenes_lista[self._contador//4]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1
        
    def hacer_daño_mele(self,lista_enemigos:list):
        self._acaba_atacar = True
        for enemigo in lista_enemigos:
            if enemigo._rectangulo.colliderect(self._rectangulo_ataque) and self._bandera_ataque :
                if self._acaba_atacar:
                    enemigo._vida -= 3
                    self._acaba_atacar = False
            else :
                self._acaba_atacar = True
            

    def hacer_daño_distancia(self,lista_enemigos):
        for moneda in self._lista_proyectiles:
            for enemigo in lista_enemigos:                
                if enemigo._rectangulo.colliderect(moneda._rectangulo) and enemigo._vida > 0:
                    enemigo._vida -= 20
                    moneda._activo = False
    def chocar_proyectil_plataforma(self,lista_plataforma):
        for moneda in self._lista_proyectiles:
            for plataforma in lista_plataforma:
                if moneda._rectangulo.colliderect(plataforma._rectangulo):
                    moneda._activo = False     
                           
    def animar_ataque_d(self,pantalla):
        imagenes_lista = self._dict_imagenes["ataque_d"]
        largo = len(imagenes_lista)
        if self._contador//8 >= largo:
            self._contador = 0
            self._bandera_ataque = False
            
        animacion = imagenes_lista[self._contador//8]
        imagen_agrandada = pygame.transform.scale(animacion,self._tamaño_ataque)
        self._rectangulo_ataque = imagen_agrandada.get_rect()
        self._rectangulo_ataque.center =(self._rectangulo.x+50,self._rectangulo.y+20)
        pantalla.blit(imagen_agrandada,(self._rectangulo.x,self._rectangulo_ataque.y))
        self._contador += 1
        
    def animar_ataque_i(self,pantalla):
        imagenes_lista = self._dict_imagenes["ataque_i"]
        largo = len(imagenes_lista)
        if self._contador//8 >= largo:
            self._contador = 0
            self._bandera_ataque = False
            
        animacion = imagenes_lista[self._contador//8]
        imagen_agrandada = pygame.transform.scale(animacion,self._tamaño_ataque)
        self._rectangulo_ataque = imagen_agrandada.get_rect()
        self._rectangulo_ataque.center =(self._rectangulo.x,self._rectangulo.y+20)
        pantalla.blit(imagen_agrandada,(self._rectangulo_ataque.x,self._rectangulo_ataque.y))
        self._contador += 1
    
        
    def atacar(self,pantalla,lista_enemigos:list):
        if self._bandera_ataque == True:
            if self._bandera_lado == "derecha":
                self.animar_ataque_d(pantalla)
                self._bandera_lado = "derecha"
            else :
                self.animar_ataque_i(pantalla)
                self._bandera_lado = "izquierda"
                
            self.hacer_daño_mele(lista_enemigos)
        else: 
            self.animar(pantalla)
        
            