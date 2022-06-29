#NUMPY
#QUE ES NUMPY
#LIBRERIA PARA EL CALCULO NUMERICO Y MANEJO DE ARREGLOS (ARRAY) (LISTA ORGANIZADAS DE NUMEROS)
#MÁS VELOZ Y EFICIENTE PARA MANEJAR LISTAS/ARREGLOS EN PYTHON
#AGREGA SOPORTE PARA GRANDES ARREGLOS, MULTIDIMENSIONALES Y MATRICES
#ES UTITLIZADA EN EL MUINDO DE LA INTELIGENCIA ARTIFICIAL Y LA CIENCIA DE DATOS
#COMO SE INSTALA:
#EN LA CONSOLA ACTIVAR AMBIENTE VIRTUAL DE MINICONDA
#pip install numpy
import numpy as np
def main():
    lista=[1,2,3,4,5,6,7,8,9,10]
    print(lista)
    #crear un arreglo en numpy
    arreglo=np.array(lista)
    print(arreglo)
    print(type(arreglo))#no es una lista es un arreglo
    #crear arreglo de dos dimensiones
    matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(matriz)
    matriz1=np.array([[2,1,1],[1,1,1],[1,0,1]])
    print(matriz1)
    print(str(matriz*matriz1))
    print(arreglo[0])
    print(arreglo[0]+arreglo[1])
    #indexacion matrices
    print(matriz[0])
    print(matriz[1,2])

if __name__=='__main__':
    main()



