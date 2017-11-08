#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y calcula su media y su desviación estándar.

def calcularPromedio(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma= suma + lista[i]

    return suma / len(lista)
def calcularDesviacion(lista):
    Sumatoria=0
    for i in lista:
        suma = (i - calcularPromedio(lista))**2
        Sumatoria = Sumatoria + suma
    varianza=Sumatoria/(len(lista)-(1))
    desviacion= (varianza)**0.5
    return desviacion





def main():
 lista=	[1,2,3,4,5,6]
 lista1=[95,21,73,24,15,69,71,80,49,100,85]

 print("De la lista dada el promedio es:",calcularPromedio(lista),"la desviacion estándar es:", calcularDesviacion(lista))
 print("De la lista dada el promedio es:", calcularPromedio(lista1), "la desviacion estándar es:", calcularDesviacion(lista1))


main()
