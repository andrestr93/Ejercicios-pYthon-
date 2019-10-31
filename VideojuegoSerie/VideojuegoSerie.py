class Serie:

    def __init__(self , titulo = "" , numtemporadas = 0  , entregado = False , genero ="" , creador ="" ):
        self.titulo = titulo
        self.numtemporadas = numtemporadas
        self.entregado = entregado
        self.genero = genero
        self.creador =creador

    def getserie(self):
        return self.creador, self.__titulo, self.__numtemporadas, self.__genero , self.entregado

    def setserie(self, titulo, creador, numtemporadas, genero , entregado):
        self.__titulo = titulo
        self.__creador = creador
        self.__numtemporadas = numtemporadas
        self.__genero = genero
        self.entregado = entregado

    def entregadoserie (self , v):
        self.entregado= True

    def entregaserie (self):
        return self.entregado




serie1 = Serie("Prison Break" ,  10 , False , "accion" , "Andrew colman")
serie2 = Serie("Juego de Tronos" ,  3 , True, "accion" , "Andrew")
serie3 = Serie("Rick and Morty" ,  4 ,  False , "comedia" , "Json")
serie4 = Serie("Paradise Police" ,  15 ,  True , "comedia" , "Francis")
serie5 = Serie("Elite" , 16 , False , "juvenil" , "Andres")



class Videojuego:

    def __init__(self , titulo = "" , horasestimadas = 0  , entregado = False , genero ="" , compania ="" ):
        self.titulo = titulo
        self.horasestimadas = horasestimadas
        self.entregado = entregado
        self.genero = genero
        self.compania =compania


    def getvideojuego(self):
        return self.__titulo, self.__horasestimadas, self.__genero, self.__compania

    def entregadojuego(self , v):
        self.entregado = True


    def entregajuego (self):
        return self.entregado


    def setvideojuego(self, titulo, genero, horasestimadas, compania):
        self.__titulo = titulo
        self.__horasestimadas = horasestimadas
        self.__compania = compania
        self.__genero = genero

juego1  = Videojuego( "Resident evil" ,  50 ,  False ,  "terror" , "Capcom")
juego2 = Videojuego("Detroit Become" ,  100 , False , "drama" , "esquare fenix")
juego3 = Videojuego("Street Fghiter" ,  200 , True , "lucha" , "esquare fenix")
juego4 = Videojuego("Fornite" ,  80 , False , "drama" , "esquare fenix")
juego5 = Videojuego("Rayman" ,  180 , True , "drama" , "esquare fenix")

listaseries = [serie1 , serie2 , serie3 , serie4 , serie5]
listajuegos = [juego1 , juego2 , juego3 , juego4 , juego5]

print("------------------------------------JUEGOS-----------------------------------")
#ENTREGA JUEGO
print("juegos entregados")
juego1.entregadojuego(juego1)
print("juego 1 entregado " , juego1.entregajuego())


def cuentajuegos ():
    conjuegos = 0
    for  i in listajuegos:
        if i.entregado==True:
            conjuegos += 1
        return conjuegos

print("Juegos entregados " ,cuentajuegos())

def juegomashoras():
    horasmax = 0
    titulo =""
    for i in listajuegos:
        if i.horasestimadas>horasmax:
            horasmax = i.horasestimadas
            titulo=i.titulo

    return horasmax , titulo


print("juego con mayor horas " , juegomashoras())


print("------------------------------------SERIES-----------------------------------")
#ENTREGA SERIE
print("series entregadas")
serie5.entregadoserie(serie5)
print("serie 5 entregada " , serie5.entregado)

def seriemastemporadas():
    temporadas = 0
    titulo =""
    for i in listaseries:
        if i.numtemporadas>temporadas:
            temporadas=i.numtemporadas
            titulo = i.titulo
    return temporadas , titulo

print("serie con mas temporadas "  , seriemastemporadas())


def cuentaseries ():
    conseries = 0
    for  i in listaseries:
        if i.entregado==True:
            conseries += 1
        return conseries

print("Series entregadas " ,cuentaseries())












































































