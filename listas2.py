# encondig:UTF-8
#Autor Angel Ramírez Martínez  A01273759
#Descripción: Programa que realiza diferentes operaciones con listas

#Determinación de variables globales con listas.
lista1 = [1,2,3,4,5]
lista2 = []
lista3 = [5]
lista4=[1,0,3,2,8,5]
lista5=[1,1,1,2,3,4,5,6,6,6,7]
lista6=[1,2,3]
lista7=[1,3,2,4,8,6,9,7,8]
lista8=[6,9]
lista9=[95,21,73,24,15,69,71,80,49,100,85]

#Función que encuentra los pares de una lista que le llega como parámetro.
def encontrarPares(lista):
    listaPares=[]
    for element in lista:
        if element%2==0:
            listaPares.append(element)
    return listaPares
#Función que regresa los regresa una lista con los valores que son mayores a un elemento previo de la lista original
def regresarElementosMayores(lista):
    listaMayores=[]
    for index in range(len(lista)):
        if index<len(lista)-1:
            if lista[index]<lista[index+1]:
                listaMayores.append(lista[index+1])
    return listaMayores

def intercambiarElementos(lista):
    elementosIntercabiados=[]
    if len(lista)%2==0:
        for index in range(0,len(lista),2):
            elementosIntercabiados.append(lista[index+1])
            elementosIntercabiados.append(lista[index])
        return elementosIntercabiados
    else:
        for index in range(0,len(lista)-1,2):
            elementosIntercabiados.append(lista[index+1])
            elementosIntercabiados.append(lista[index])
        elementosIntercabiados.append(lista[len(lista)-1])
        return elementosIntercabiados

def cambiarValoresMaxyMin(lista):
    maxyMinIntercambiados = lista[:]
    if len(lista)>=2:
        for index in range(len(lista)):
            if lista[index]== min(lista):
                indexminimo=index
            elif lista[index]==max(lista):
                indexmaximo=index
        maxyMinIntercambiados.remove(lista[indexminimo])
        maxyMinIntercambiados.remove(lista[indexmaximo])
        maxyMinIntercambiados.insert(indexmaximo-1,lista[indexminimo])
        maxyMinIntercambiados.insert(indexminimo,lista[indexmaximo])
        return maxyMinIntercambiados
    return maxyMinIntercambiados

def regresarDatosMayoresaPromedio(lista):
    if len(lista)>0:
        promedio=sum(lista)/len(lista)
        elementosMayores=0
        for element in lista:
            if element>=promedio:
                elementosMayores+=1
        return elementosMayores
    else:
        return 0


def regresarPromedio(lista):
    if len(lista)>0:
        promedio=sum(lista)/len(lista)
        return promedio
    else:
        return 0


def regresarElementosMayoresalPromedio(lista):
    if len(lista)>0:
        promedio = sum(lista) / len(lista)
        mayoresalPromedio=[]
        for elemento in lista:
            if elemento>=promedio:
                mayoresalPromedio.append(elemento)
        return mayoresalPromedio
    else:
        return 0

def calcularMediayDesviacion(lista):
    if len(lista)>1:
        suma=0
        media= sum(lista) / len(lista)
        for element in lista:
            dif=(element-media)**2
            suma+=dif
        desviacion=(suma/(len(lista)-1))**(1/2)
        return media,desviacion
    return (0,0)






def main():
    print('''\nProblema #1 regresa una lista con los elementos pares de la lista original.
• La lista %s, regresa la lista de los elementos pares %s
• La lista %s, regresa la lista de los elementos pares %s
• La lista %s, regresa la lista de los elementos pares %s
• La lista %s, regresa la lista de los elementos pares %s
''' %(lista1,encontrarPares(lista1),lista2,encontrarPares(lista2),lista3,encontrarPares(lista3),lista5,encontrarPares(lista5)))
    print('''\nProblema #2 regresa una lista con los valores que son mayores a un elemento previo de la lista original.
• La lista %s, regresa la lista con los valores que son mayores a un elemento previo %s
• La lista %s, regresa la lista con los valores que son mayores a un elemento previo %s
• La lista %s, regresa la lista con los valores que son mayores a un elemento previo %s
• La lista %s, regresa la lista con los valores que son mayores a un elemento previo %s
''' % (lista1, regresarElementosMayores(lista1), lista2, regresarElementosMayores(lista2), lista3, regresarElementosMayores(lista3), lista5,regresarElementosMayores(lista5)))
    print('''\nProblema #3 regresa una lista con los elementos invertidos por pareja de la lista original (si la lista es de un número impar de elementos el último no cambia )
• La lista %s, regresa la lista de los elementos invertidos %s
• La lista %s, regresa la lista de los elementos invertidos %s
• La lista %s, regresa la lista de los elementos invertidos %s
• La lista %s, regresa la lista de los elementos invertidos %s
• La lista %s, regresa la lista de los elementos invertidos %s
''' % (lista7, intercambiarElementos(lista7), lista6, intercambiarElementos(lista6),lista2,intercambiarElementos(lista2), lista3, intercambiarElementos(lista3), lista5,intercambiarElementos(lista5)))
    print('''\nProblema #4 regresa una lista de los elementos máximo y mínimo invertidos de acuerdo a la lista original.
• La lista %s, regresa la lista de los elementos máximo y mínimo invertidos %s
• La lista %s, regresa la lista de los elementos máximo y mínimo invertidos %s
• La lista %s, regresa la lista de los elementos máximo y mínimo invertidos %s
• La lista %s, regresa la lista de los elementos máximo y mínimo invertidos %s
• La lista %s, regresa la lista de los elementos máximo y mínimo invertidos %s
''' % (lista7, cambiarValoresMaxyMin(lista7), lista6, cambiarValoresMaxyMin(lista6),lista2,cambiarValoresMaxyMin(lista2),lista3, cambiarValoresMaxyMin(lista3),lista8, cambiarValoresMaxyMin(lista8)))
    print('''\nProblema #5 regresa el número de elementos mayores o iguales al promedio de la lista original.
• La lista %s, regresa %s elementos que son mayores o iguales al promedio %.2f %s
• La lista %s, regresa %s elementos que son mayores o iguales al promedio %.2f %s 
• La lista %s, regresa %s elementos que son mayores o iguales al promedio %.2f %s
• La lista %s, regresa %s elementos que son mayores o iguales al promedio %.2f %s
• La lista %s, regresa %s elementos que son mayores o iguales al promedio %.2f %s
''' % (lista1, regresarDatosMayoresaPromedio(lista1),regresarPromedio(lista1), regresarElementosMayoresalPromedio(lista1), lista4, regresarDatosMayoresaPromedio(lista4),regresarPromedio(lista4), regresarElementosMayoresalPromedio(lista4), lista2, regresarDatosMayoresaPromedio(lista2),regresarPromedio(lista2), regresarElementosMayoresalPromedio(lista2),lista3,regresarDatosMayoresaPromedio(lista3),regresarPromedio(lista3),regresarElementosMayoresalPromedio(lista3),lista7, regresarDatosMayoresaPromedio(lista7),regresarPromedio(lista7), regresarElementosMayoresalPromedio(lista7)))
    m1, de1=calcularMediayDesviacion(lista1)
    m2, dE2=calcularMediayDesviacion(lista2)
    m3, dE3=calcularMediayDesviacion(lista3)
    m4, dE4=calcularMediayDesviacion(lista4)
    m5,dE5=calcularMediayDesviacion(lista9)
    print('''\nProblema #6 regresa una dupla con la media y la desviación estándar, de acuerdo a la lista original.
• La lista %s, regresa una dupla con la media y la desviación estándar (%.2f,%.6f)
• La lista %s, regresa una dupla con la media y la desviación estándar (%d,%d)
• La lista %s, regresa una dupla con la media y la desviación estándar (%d,%d)
• La lista %s, regresa una dupla con la media y la desviación estándar (%.2f,%.6f)
• La lista %s, regresa una dupla con la media y la desviación estándar (%.2f,%.6f)
''' % (lista1, m1,de1,lista2,m2,dE2, lista3, m3,dE3, lista4, m4,dE4,lista9, m5,dE5))

main()