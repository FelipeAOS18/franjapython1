#Tarea 1
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
#  la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
# y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#  Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso
#  total del paquete que será enviado.

from calendar import c
from re import S
from this import s


print("Bienvenido a la tienda")
print("¿Quisiera llevar payasos?¿Cuantos?")
p=int(input(" "))
print("¿Quisiera llevar muñecas?¿Cuantas?")
m=int(input(" "))
t=(p*112)+(m*75)
t=str(t)
print("La cantidad de muñecas:"+ str(m)+"")
print("La cantidad de payasos:"+ str(p) +"")
print("El peso del pedido es de :"+str(t)+" g")
#Tarea 2
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
# "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal
#  calculado redondeado con dos decimales.

print("Ingrese su peso")
p=float(input(" "))
print("Ingrese su estatura")
c= float(input(" "))

i= p/(c*c)
s=round(i, 2)
s=str(s)
print("Su indice de masa corporal es :")
print(""+str(s))