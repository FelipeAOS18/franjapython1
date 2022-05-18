#
#Escribir un programa que identifique
#si una palabra es palindromo o no
#Luz azul
#Ana
#Anita lava la tina 
#Yo hago yoga hoy
# intento de ejecutar 
# print("Ingrese su palabra:")
# palabra=input(":  ")
# palabra=palabra.strip()
# palabra=palabra.lower()
# palabra1=palabra[::-1]
# palabra1=palabra1.strip()
# if palabra==palabra1 :
#     print("La palabra es palindromo")
#     print("La palabra ingresada es: "+palabra)
#     print("La palabra invertida es:  "+palabra1)
# else :
#     print("La palabra no es palindromo")
#     print("La palabra ingresada es: "+palabra)
#     print("La palabra invertida es:  "+palabra1)

#DESARROLLO DEL PROFE
#funcion principal main/run


def palindromo(palabra):
    palabra=palabra.replace(" ","")
    palabra=palabra.lower()
    palabra_invertida=palabra[::-1]
    if palabra==palabra_invertida:
        return True
    else:
        return False
def main():
    palabra=input("Ingrese una frase: ")
    es_palindromo=palindromo(palabra)
    if es_palindromo:
        print("Es palindromo ")
    else:
        print("No es palindromo")

    pass
#punto de entrada
#buena practica
if __name__== "__main__":
    main()
