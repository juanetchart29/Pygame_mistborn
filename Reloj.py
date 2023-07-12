import pygame

class Reloj:
    def __init__(self, tiempo_inicial:int,posicion):
        self.tiempo = tiempo_inicial
        self.cooldown = pygame.time.get_ticks()  
        self.cooldown_intervalo = 1000 
        self.fuente = pygame.font.Font(None, 50)
        self.color_texto = (255, 255, 255)
        self.posicion_texto = posicion

    def actualizar(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.cooldown >= self.cooldown_intervalo:
            self.tiempo -= 1
            if self.tiempo < 0:
                self.tiempo = 0
            self.cooldown = tiempo_actual

    def dibujar(self, screen):
        texto = self.fuente.render(str(self.tiempo), True, self.color_texto)
        screen.blit(texto, self.posicion_texto)

    def acaba_el_tiempo(self):
        if self.tiempo <=0:
            
            return True
        else: return False
        
