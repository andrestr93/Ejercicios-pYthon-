from Electrodomestico.Electrodomestico import Electrodomestico
from Electrodomestico.Lavadora import Lavadora


class Television (Electrodomestico):


    def __init__(self, resolucion=20, cfourk= False):
       self.resolucion = resolucion
       self.fourk = cfourk
       Electrodomestico.__init__(self, preciobase=100, color="blanco", consumoenergetico="F", peso=5)

    def getresoolucionfourk(self):
        return self.resolucion , self.fourk
    def preciofinal(self):
        precio = 0
        if self.resolucion>40:
            (precio * 30)/100
        elif self.resolucion>80:
            precio = precio + 50













