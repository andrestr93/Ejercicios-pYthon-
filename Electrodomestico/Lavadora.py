from Electrodomestico.Electrodomestico import Electrodomestico
class Lavadora (Electrodomestico):
    def __init__(self, carga = 5):
        self.carga = carga

        Electrodomestico.__init__( self , preciobase=100, color="blanco", consumoenergetico="F", peso=5)

    def getcartga (self):
        return self.carga

    def preciofinal(self):
        precio = 0
        if self.carga > 30:
            precio = precio + 50
    




