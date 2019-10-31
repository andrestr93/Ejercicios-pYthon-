class Electrodomestico:
    def __init__(self, preciobase=100, color="blanco", consumoenergetico="F", peso=5):
        self.preciobase = preciobase
        self.color = color
        self.consumoenergetico = consumoenergetico
        self.peso= peso

    def getatributos(self):
        return self.preciobase , self.consumoenergetico , self.color ,self.peso

    def comprobarconsumoenergetico(self):
        if self.consumoenergetico == "A" or "B" or "C" or "D" or "E":
            return self.consumoenergetico
        else:
            return self.consumoenergetico


    def comprobarcolor (self):
        if self.color == "blanco" or "negro" or "rojo" or "azul" or "gris":
            return self.color
        else:
            return self.color

    def preciofinal(self):

        precio = 0
        if self.consumoenergetico =="A":
            precio = 100
        elif self.consumoenergetico=="B":
            precio = 80
        elif self.consumoenergetico=="C":
            precio = 60
        elif self.consumoenergetico=="D":
            precio = 50
        elif self.consumoenergetico=="E":
            precio = 30
        elif self.consumoenergetico=="F":
            precio = 10
        return  precio

    def tamano(self):
        precio = 0
        if self.peso<0 or self.peso>=19:
            precio = 10
        if self.peso>=20 or self.peso<49:
            precio = 50
        if self.peso >= 50 or self.peso < 79:
            precio = 80
        if self.peso>80:
            precio = 100
        return precio









