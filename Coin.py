from GameObject import GameObject


class Coin(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagen: dict,score:int) -> None:
        super().__init__(tamaño, posicion, diccionario_imagen)
        self._score = score