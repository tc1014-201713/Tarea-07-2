#encoding:UTF-8
#Angel Roberto Pesado Bartolo A01374942
#Manejo de listas, segunda tarea.

def encontrarNumerosPares(lista):#función que encuentra los numeros pares dentro de una lista
    numerosPares=[]
    for par in lista:
        if par%2==0:
            numerosPares.append(par)
    return numerosPares

def encontrarParametroMayor(lista):#función que encuentra el numero mayor al elemento previo de la lista.
    listaMayores=[]

    for posición in range(0,len(lista)-1):
        if lista[posición] < lista[posición+1]:
            listaMayores.append(lista[posición+1])
    return listaMayores

def calcularPromedio(lista): #función que calcula cuantos numeros son más grandes o iguales al promedio de la lista.
    promedio=sum(lista)/len(lista)
    num=0
    for i in lista:
        if i >=promedio:
            num+=1
    return num

def calularPromedioDesviacion(lista):#función que calcula el promedio y la desviación estandar de la lista.
    promedio=sum(lista)/len(lista)
    suma1=0
    lista1=[]
    lista2=[]
    for i in lista:
        suma=(i-promedio)**2
        suma1=suma+suma1
        variancia=suma1/(len(lista)-1)
        desviacion=(variancia)**.5
    lista2.append(desviacion)
    lista1.append(promedio)
    lista3 = lista1 + lista2
    return lista3

def intercambiarNumeros(lista):#función que intercambia de posición los datos de cada pareja de la lista.
    desplazamiento = []
    for i in range(0, len(lista)-1,2):
        desplazamiento.append(lista[i+1])
        desplazamiento.append(lista[i])
    if len(lista) % 2 != 0:
        desplazamiento.append(lista[-1])
    return desplazamiento

def intercambiarNumerosMayoresYMenores(lista):#función que intercambia de posición los numeros mayores y menores de la lista
    if len(lista) >= 1:
        lugar = lista[:]
        lugarmayor = lugar.index(max(lista))
        lugarmenor = lugar.index(min(lista))
        lugar.remove(max(lista))
        lugar.remove(min(lista))
        lugar.insert(lugarmenor, max(lista))
        lugar.insert(lugarmayor, min(lista))
    else:
        lugar = []
    return (lugar)


def main():
    salirMenu = True
    while salirMenu:  # mientras el menu sea seleccionable hará lo siguiente
        print("Tarea 07.2.Listas\nAngel Roberto Pesado Bartolo A01374942\n1.-Problema1 Regresa una lista con los valores pares de la lista original.\n2.-Problema2 Regresa una lista con los valores que son mayores a un elemento previo.\n3.-Problema3 Regresa una lista con los valores intercambiados de cada parejas de datos.\n4.-Problema4 Regresa una lista con los con el valor menor y mayor intercambiados.\n5.-Problema5 Regresa una lista con los valores que son iguales o mayores al promedio de la lista.\n6.-Problema6 Regresa una lista con los la media y la desviación estandar de la lista.\n7.-Salir")
        desicion = int(input("¿Qué deseas realizar?: "))  # Pedimos al usuario que desea hacer
        if desicion <= 0 or desicion > 7:  # indicamos que si la desicion del usuario es menor a 0 o mayor a 7 indique que está en error y eliga de nuevo
            print("ERROR, teclea un numero del 1 al 7\n")
        elif desicion == 1:  # si la decisión es 1
            print("\nProblema1 Regresa una lista con los valores pares de la lista original.")#imprime este letrero
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            print("La lista es la siguiente",lista,"dentro de ella los numeros pares son: ",encontrarNumerosPares(lista))#llamamos a la función e imprimimos el resultado
            lista = [5, 7, 3]
            print("La lista es la siguiente", lista, "dentro de ella los numeros pares son: ", encontrarNumerosPares(lista),"\n")# ejecuta la función
        elif desicion == 2:  # si la desición es 2
            print("\nProblema2 Regresa una lista con los valores que son mayores a un elemento previo.")#imprime este letrero
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            print("La lista es la siguiente", lista, "dentro de ella los numeros mayores son: ", encontrarParametroMayor(lista))#llamamos a la función e imprimimos el resultado
            lista = [5, 4, 3,2]
            print("La lista es la siguiente", lista, "dentro de ella los numeros mayores son : ",encontrarParametroMayor(lista), "\n")# ejecuta la función
        elif desicion == 3:  # si la desición es 3
            print("\n3.-Problema3 Regresa una lista con los valores intercambiados de cada parejas de datos.")#imprime este letrero
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            print("La lista es la siguiente", lista, "invirtiendo los numeros de posición: ", intercambiarNumeros(lista))#llamamos a la función e imprimimos el resultado
            lista = [1, 2, 3]
            print("La lista es la siguiente", lista, "invirtiendo los numeros de posición: ", intercambiarNumeros(lista))#llamamos a la función e imprimimos el resultado
            lista = [7]
            print("La lista es la siguiente", lista, "invirtiendo los numeros de posición: ",intercambiarNumeros(lista), "\n")# ejecuta la función
        elif desicion == 4:  # si la desición es 4
            print("\nProblema4 Regresa una lista con los con el valor menor y mayor intercambiados.")#imprime este letrero
            lista = [5, 9, 3, 22, 19, 31, 10, 7]
            print("La lista es la siguiente", lista, "dentro de ella se cambian los numeros mayores y menores así: ", intercambiarNumerosMayoresYMenores(lista))#llamamos a la función e imprimimos el resultado
            lista = [1,2,3]
            print("La lista es la siguiente", lista, "dentro de ella se cambian los numeros mayores y menores así : ",intercambiarNumerosMayoresYMenores(lista), "\n")# ejecuta la función
        elif desicion == 5:  # si la desición es 5
            print("\nProblema5 Regresa una lista con los valores que son iguales o mayores al promedio de la lista.")#imprime este letrero
            lista = [70, 80, 90]
            print("La lista es la siguiente", lista, "los numeros que son mayores al promedio son: ",calcularPromedio(lista))#llamamos a la función e imprimimos el resultado
            lista = [95,21,73,24,15,69,71,80,49,100,85]
            print("La lista es la siguiente", lista, "los numeros que son mayores al promedio son : ",calcularPromedio(lista), "\n")# ejecuta la función
        elif desicion == 6:  # si la desición es 6
            print("\nProblema6 Regresa una lista con los la media y la desviación estandar de la lista.")#imprime este letrero
            lista=[1,2,3,4,5,6]
            print("La lista es la siguiente", lista, "la desiación estandar de la lista es: ",calularPromedioDesviacion(lista))#llamamos a la función e imprimimos el resultado
            lista = [95,21,73,24,15,69,71,80,49,100,85]
            print("La lista es la siguiente", lista, "la desviación estandar de la lista es : ",calularPromedioDesviacion(lista), "\n")# ejecuta la función
        elif desicion == 7:  # si la desición es 7
            return print("Gracias por usar este programa, regresa pronto")  # imprime este anuncio
main()
