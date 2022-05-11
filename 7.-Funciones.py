#funciones

# def imprimir_mensaje():
    # print("Mensaje bienvenida")
    # print("APRENDIENDO PYTHON")
# imprimir_mensaje()#Repiticion de mensaje
# imprimir_mensaje()#x2
# imprimir_mensaje()#x3

#parametros
# def saludo(nombre, apellido):
    # print("Hola "+ nombre +" "+apellido)
# entrada_texto=input("INGRESE SU NOMBRE: ")
# entrada_tex=input("INGRESE SU APELLIDO: ")
# saludo(entrada_texto, entrada_tex)


#condicionales con parametros
# def suma(numero1,numero2):
#     sm = numero1+ numero2
#     sm=str(sm)
#     print("Sumado es "+ sm)
# def resta(numero1,numero2):
#     rs = numero1 - numero2
#     rs=str(rs)
#     print("La resta es: "+rs)
# def dividir(numero1,numero2):
#     dv = numero1 / numero2
#     dv=str(dv)
#     print("La division es: "+dv)
# def multiplicar(numero1,numero2):
#     ml = numero1 * numero2
#     ml=str(ml)
#     print("La multiplicacion es: "+ml)
# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese otro numero: "))
# print("Quiere restarlos o sumarlos")
# print("""1 PARA SUMAR 
# 2 PARA RESTAR 
# 3 PARA DIVIDIR 
# 4 PARA MULTIPLICAR""")

# determinar=int(input(""))
# if determinar==1:
#     suma(num1,num2)
# elif determinar==2:
#     resta(num1,num2)
# elif determinar==3:
#     dividir(num1,num2)
# elif determinar==4:
#     multiplicar(num1,num2)

def suma(a,b):
    resultado=a+b
    print("Resultado es "+str(resultado))
    return resultado

def resta(a,b):
    resultado=a-b
    print("Resultado es "+str(resultado))
    return resultado

def dividir(a,b):
    resultado= a/b
    print("Resultado es "+str(resultado))
    return resultado
def multiplicar(a,b):
    resultado= a*b
    print("Resultado es "+str(resultado))
    return resultado

print("""1 PARA SUMAR 
2 PARA RESTAR 
3 PARA DIVIDIR 
4 PARA MULTIPLICAR""")
determinar=int(input(""))
num1=int(input("Ingrese Numero 1:  "))
num2=int(input("Ingrese Numero 2:  "))

if determinar==1:
    suma(num1,num2)
elif determinar==2:
    resta(num1,num2)
elif determinar==3:
    dividir(num1,num2)
elif determinar==4:
    multiplicar(num1,num2)
else :
    pass