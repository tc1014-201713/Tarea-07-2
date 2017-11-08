#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y calcula su promedio.

def calcularPromedio(lista):
    promedio = sum(lista) / len(lista)
    suma = 0
    for i in lista:
        if i>=promedio:
            suma += 1
    return suma





def main():
    lista=[70,	80,	90]
    lista1=	[95,21,73,24,15,69,71,80,49,100,85]
    print("De la lista dada",lista,"los números que son mayores o iguales al promedio son:",calcularPromedio(lista))
    print("De la lista dada", lista1, "los números que son mayores o iguales al promedio son:", calcularPromedio(lista1))

main()