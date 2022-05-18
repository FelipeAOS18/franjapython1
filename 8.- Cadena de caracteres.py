#CADENA DE CARACTEREWS
#FELIPE OLGUIN
from tkinter import N


nombre= input("¿CUAL ES SU NOMBRE?: ")
nombre= nombre.upper()# Todo mayuscula
print(nombre)
nombre=nombre.capitalize()# Inicial en mayuscula
print(nombre)
nombre=nombre.strip()#para espacios
print(nombre)
nombre=nombre.lower()#minusculas
print(nombre)
nombre=nombre.replace("e","a")#cambiar letras
nombre=nombre.replace("i","o")
nombre=nombre.replace("g","")
print(nombre)

print(nombre[0])#mostrar caracter de poscion indicada
letra=nombre[2]#
print(letra)
largo_cadena=len(nombre)
print(largo_cadena)
largo_texto=len("Franja  ")
print(largo_texto)
cadena_texto= "Franja   "
cadena_texto=cadena_texto.strip()
print(len(cadena_texto))