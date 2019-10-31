from Persona import Persona

persona1 = Persona
persona2 = Persona
persona3 = Persona


nombre = (input("ingrese un nombre"))
edad = int(input("Ingrese una edad"))
sexo = (input("Ingrese el sexo"))
peso = int(input("Ingrese peso"))
altura = float(input("Ingrese altura"))
dni = input("Ingrese dni")


persona1.datos( nombre , edad , sexo , peso , altura) # PRIMER METODO GUARDA EN LAS VARIABLES EL NOMBRE EDAD SEXO PESO Y ALTURA

persona2.anteriores(nombre , edad , sexo) # SEGUNDO METODO GUARDA EN LAS VARIABLES EL NOMBRE EDAD SEXO

persona3.cambiovalor(persona3 , nombre , edad , peso , altura , dni , sexo ) # 3º metodo que hace de setter para cambiar los valores de los atributos



print("------------------- CALCULO IMC -------------")


# METODO CALCULA IMC
#LO COMPROBAMOS EN LOS TRES OBJETOS

print("OBJETO PERSONA1")

if persona1.calculaimc(persona1)==-1:
    print("peso inferior al ideal")
elif persona1.calculaimc(persona1)==0:
    print("peso ideal")
else:
    print("sobrepeso")


    print("OBJETO PERSONA2")

if persona2.calculaimc(persona2)==-1:
    print("peso inferior al ideal")
elif persona2.calculaimc(persona2)==0:
    print("peso ideal")
else:
    print("sobrepeso")

    print("OBJETO PERSONA3")

if persona3.calculaimc(persona3)==0:
    print("peso inferior al ideal")
elif persona3.calculaimc(persona3)==0:
    print("peso ideal")
else:
    print("sobrepeso")


print("------------------- MAYORIA DE EDAD -------------")

#METODO MAYORIA DE EDAD
if persona1.esmayordeedad(persona1)==True:
    print("No es mayor de edad")
else:
    print("Es mayor de edad")

    print("OBJETO PERSONA2")

if persona1.esmayordeedad(persona1)==True:
    print("No es mayor de edad")
else:
    print("Es mayor de edad")

    print("OBJETO PERSONA3")

if persona1.esmayordeedad(persona1)==True:
    print("No es mayor de edad")
else:
    print("Es mayor de edad")






























