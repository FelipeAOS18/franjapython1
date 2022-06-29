
def dia(numero_dia): 
    if numero_dia == 1: 
        print("lunes")
    if numero_dia == 2:
        print("martes") 
    if numero_dia == 3:
        print("miercoles")
    if numero_dia == 4:
        print("jueves")
    if numero_dia == 5:
        print("viernes")
    if numero_dia == 6 :
        print("sabado")
    if numero_dia == 7:
        print("domingo")

print( "menciona un numero para determinar tu dia ") 
numero_dia = int (input())
print(numero_dia)
dia(numero_dia)

