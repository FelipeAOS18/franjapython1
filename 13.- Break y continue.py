#break y continue

# def main():
#     #imprimir  los numeros pares 
#     for contador in range(1,101):
#         if contador % 2 == 0:
#             continue
#         #print (contador)
#     for numero in range( 1, 100):
#         print(numero)
#         if numero ==8:
#             break
texto=input("ingrese un texto ")
for letra in texto:
    if letra=='j':
        break
    print(letra)
if __name__ == '__main__':
    main ()

