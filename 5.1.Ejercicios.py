#Ejercicio 1
#Escribir un programa que pregunte el nombre por consola
#Y un numero entero e imprimir por pantalla el nombre
# tantas veces como el numero introdujo

from ast import Return
from this import d


nombre= (input("introdusca su nombre: "))
print(nombre)

numero= int(input("Ingrese un numero: "))

numero1= numero*nombre
print(nombre*numero)

#Ejercicio 2
#Escribir un programa que muestre por pantalla el resultado
#de la siguiente operacion artimetica
D= (((3+2)/(2*5))**2)
print(D)

#Ejercicio 3 
#Escribir un programa que lea un enetero positivo n
#introducido por el usuario y despues muentre por pantalla
#La suma de los n primero posivos puede ser calculada
#Dela siguiente forma

n=int(input("Introdusca un numero entero positivo: "))
if n<0:
    print("Dije entero positivo ")
    n=int(input("Introdusca un numero entero positivo porfavor: "))
    Suma= ((n*(n+1))/2)
    Suma=str(Suma)
    n=str(n)
    print(Suma)
    print("La suma de los primeros numeros enteros desde 1 hasta"+n+"es"+Suma)

else:
    Suma= ((n*(n+1))/2)
    Suma=str(Suma)
    n=str(n)
    print(Suma)
    print("La suma de los primeros numeros enteros desde 1 hasta "+n+" es "+Suma)


