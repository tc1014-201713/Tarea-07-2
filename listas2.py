#Javier Pascal Flores A01375925
#Encogind:UTF-8
from math import sqrt
import statistics
#regresa los numeros pares en una lista
def ejercicio1(lista):
    listapares=[]
    for i in lista:
        if i % 2 == 0:
            listapares.append(i)
    return listapares
#regresa los valores que son mayores a un elemento previo
def ejercicio2(lista):
    resultM = []
    for i in range(0,len(lista)-1):
        if lista[i] < lista[i+1]:
            resultM.append(lista[i+1])
    return resultM
#Regresa una pareja de datos intecambiados
def ejercicio3(lista):
    Intercambiada = lista[::1]
    x = 1
    if len(Intercambiada) % 2 == 1:
        x = 2
    for i in range(0, len(Intercambiada) - x, 2):
        y = Intercambiada[i]
        Intercambiada[i] = Intercambiada[i + 1]
        Intercambiada[i + 1] = y
    return Intercambiada
#Regresa el menor y mayor intercambiados
def ejercicio4(lista):
    result=lista[::1]
    if len(lista)!=0:
        maximo=(max(result))
        minimo=(min(result))
        result[result.index(maximo)]=minimo
        result[result.index(minimo)] = maximo
    else:
        result=[]
    return result
#datos mayores o iguales al promedio
def ejercicio5(lista):
    result=[]
    if len(lista)!=0:
       promedio=sum(lista)/len(lista)
    else:
       return 0
    for i in lista:
        if i >= promedio:
            result.append(i)
    return len(result)
#regresa dupla con la media y desviacion estandar
def ejercicio6(lista):
    if len(lista)==0 or len(lista)==1:
        return"(0,0)"
    else:
        suma = 0
        for i in lista:
            suma += i
        promedio = suma / len(lista)
        varianza=sum((i - promedio)**2 for i in lista) / (len(lista)-1)
        desviacion=sqrt(varianza)
        #result="(" + str(promedio) + ", " + str(desviacion) + ")"
        return (promedio,desviacion)





def main():
    listas = [[80, 90, 100], [5, 9, 3, 22, 19, 31, 10, 7], [], [8], [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55],
              [6,5,4,3], [5, 7, 3]]
    ejercicios = {"Problema 1. Regresa una lista con los valores pares de la lista original.": ejercicio1,
                 "Problema 2. Regresa una lista con los valores mayores a un elemento previo.": ejercicio2,
                 "Problema 3. Regresa una lista con cada pareja de datos intercambiados.": ejercicio3,
                 "Problema 4. Regresa una lista con el valor mayor y menor intercambiados.": ejercicio4,
                 "Problema 5. Regresa el numero de datos mayores o iguales al promedio de los valores.": ejercicio5,
                 "Problema 6. Regresa una dupla con el promedio y la desviación estándar de los datos.": ejercicio6}

    # Toma cada función y la evalua con cada lista
    for frase, funcion in ejercicios.items():
        print(frase)
        for i in listas:
            print("Con la lista " + str(i) + ", regresa " + str(funcion(i)))
        print("")
main()

