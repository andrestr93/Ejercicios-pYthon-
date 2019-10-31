import random
class Persona():
    def __init__(self):
        self.__nombre=""
        self.__sexo="mujer"
        self.__altura=0
        self.__edad=25
        self.__dni=0
        self.__peso=0

    def calculaimc(self):
        resultado = 0
        resultado = self.__peso/(self.__altura * 2)
        if resultado < 18.5:
            return -1  # -1 si su peso es inferior al ideal

        elif resultado >= 24.9:
            return 0  # si su peso es el indicado

        else:
            return 1  # si su pedo sobrepasa la media

    def esmayordeedad(self):
        if self.__edad < 18:
            return True

        else:
            return False

    def introducirSexo(sexo):
        sexo = "M"

    def toString():
        return Persona.__getattribute__(nombre, edad, dni, sexo, altura, peso)

    def generadni(minimo, maximo):
         if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
            return random(minimo, maximo)

    i = 0

    def datos(  nombre, edad, sexo, peso , altura ):
        print("su nombre es " ,nombre , " su edad es "  ,edad, " su sexo es "  ,sexo , "su peso es", peso , "su altura es" , altura)


    def anteriores (nombre , edad  , sexo ):
        print("su nombre es ", nombre, " su edad es ", edad, " su sexo es ", sexo)


    def cambiovalor (self ,  nombre , edad , peso , altura ,dni , sexo ):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__dni = dni
        self.__sexo = sexo
























