#encoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Ejercicos con listas de la tarea 7_2


#LISTAS PARA LA FUNCION DE SELECCIONAR PARES.
listapares1 = [1,2,3,2,4,60,5,8,3,22,44,55]
listapares2 = [5, 7, 3]
listapares3 = []

#LISTAS PARA LA FUNCION DE SELECCIONAR EL MAYOR.
listaMayores1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
listaMayores2 = [5, 4, 3, 2]
listaMayores3 = []

#LISTAS PARA LA FUNCION DE INVERTIR PAREJAS DE DATOS.
listaInvertir1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
listaInvertir2 = [1, 2, 3]
listaInvertir3 = []

#LISTAS PARA LA FUNCION DE INTERCAMBIAR MAYOR POR MENOR.
listaIntercambiar1 = [5, 9, 3, 22, 19, 31, 10, 7]
listaIntercambiar2 = [1,2,3]
listaIntercambiar3 = []

#LISTAS PARA LA FUNCION DE SELECCIONAR SOLO LOS IGUALES O MAYORES AL PRMEDIO.
listaPromedio1 = [70, 80, 90]
listaPromedio2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
listaPromedio3 = []

#LISTAS PARA LA FUNCION DE CALCULAR LA MEDIA Y LA DESVIACION.
listaDesviacion1 = [1, 2, 3, 4, 5, 6]
listaDesviacion2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
listaDesviacion3 = []



def selesccionarPares(lista): #De la lista dada, selecciona y devuelve sólo los pares.
    datospares = [] #Lista nueva para los datos pares.
    if len(lista) > 0: #Sólo se realiza si la lista contiene algún dato.
        for dato in lista: #Para recorrer todos los indices dentro de la lista.
            if dato % 2 == 0: #Si el residuo de la division del dato entre dos es cero, ese dato es par.
                datospares.append(dato) #Se agregan los datos que cumplan la condicion a la nueva lista
        return datospares
    else: #Se realiza si la lista no contiene ningún dato
        datospares = lista
        return datospares #Se regresa la lista en blanco

def esMayor(lista):
    mayores = [] #Nueva lista para los datos mayores que el anterior
    if len(lista) > 0: #Sólo se realiza si la lista contiene algún dato.
        for par in range(0, len(lista)-1): #Para recorrer los indices dentro de la lista.
            if lista[par] < lista[par+1]: #Se evalua si el dato es más pequeño que el siguiente.
                mayores.append(lista[par+1]) #Se agrega el dato mayor a la nueva lista.
        return mayores
    else: #Se realiza si la lista no contiene ningún dato
        mayores = lista
        return mayores #Se regresa la lista en blanco

def invertir(lista):
    inversos = []#Nueva lista para los datos ya invertidos.
    if len(lista) > 0:
        if len(lista)%2 != 0: #Se realiza si el numero de datos es par.
            for inverso in range(1, len(lista) - 1,2): #Para recorrer los indices dentro de la lista de dos en dos.
                inversos.append(lista[inverso]) #Agregar el segundo dato en primera posición.
                inversos.append(lista[inverso-1])#Agregar el primer dato en segunda posición.
            inversos.append(lista[-1])
            return inversos
        else:#Se realiza si el numero de datos es impar.
            for inverso in range(1, len(lista), 2):
                inversos.append(lista[inverso])
                inversos.append(lista[inverso - 1])
            return inversos
    else: #Se realiza si la lista no contiene ningún dato
        inversos = lista
        return inversos #Se regresa la lista en blanco

def invertirMayorMenor(lista):
    if len(lista) > 0: #Sólo se realiza si la lista contiene algún dato.
        mayor = max(lista) #Ubica el mayor.
        menor = min(lista) #Ubica el menor.
        indice_mayor = lista.index(mayor) #Da el indice del mayor.
        indice_menor = lista.index(menor)#Da el indice del menor.
        lista.insert(indice_mayor,menor) #Se inserta el número menor en el índice del mayor.
        lista.remove(mayor)#Se remueve el mayor de esa posición.
        lista.insert(indice_menor, mayor) #Se inserta el número mayor en el índice del menor.
        lista.remove(menor)#Se remueve el menor de esa posición.
        return lista
    else: #Se realiza si la lista no contiene ningún dato.
        return lista #Se regresa la lista en blanco.

def esMayorIgualPromedio(lista):
    nuevalista = [] ##Nueva lista para los datos mayores o iguales al promedio.
    if len(lista) > 0:#Sólo se realiza si la lista contiene algún dato.
        promedio = sum(lista) / len(lista) #Se divide la suma de todos los datos entre la cantidad de los mismos.
        for dato in lista: #Para recorrer todos los indices dentro de la lista.
            if dato >= promedio: #Se evalua si el dato es mayor o igual al promedio.
                nuevalista.append(dato) #Si cumple la condición se agrega a la lista.
        return nuevalista
    else: #Se realiza si la lista no contiene ningún dato.
        nuevalista = lista
        return nuevalista #Se regresa la lista en blanco

def calcularDesviacionyMedia(lista):
    if len(lista) > 0:#Sólo se realiza si la lista contiene algún dato.
        mean = sum(lista) / len(lista) #Se divide la suma de todos los datos entre la cantidad de los mismos.
        lista_desviacion = [] #Nueva lista para datos evaluados al cuadrado.
        for dato in lista: #Para recorrer todos los indices dentro de la lista.
            datos_desviacion = (dato - mean)**2 #Se calcula los componentes del numerador.
            lista_desviacion.append(datos_desviacion) #Se agregan a la lista antes creada.
        desviación = ((sum(lista_desviacion) / (len(lista) -1 ))** 0.5) #Se divide la suman los datos creados entre la cantidad menos uno y la raíz de eso.
        return (mean,'%.4f' % desviación)
    else:#Se realiza si la lista no contiene ningún dato.
        mean = 0
        desviación = 0
        return (mean, desviación)

def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista",listapares1, ", regresa", selesccionarPares(listapares1))
    print("Con la lista", listapares2, ", regresa", selesccionarPares(listapares2))
    print("Con la lista", listapares3, ", regresa", selesccionarPares(listapares3),'\n')

    print("Problema 2. Regresa una lista con los valores que son mayores al elemento previo.")
    print("Con la lista", listaMayores1, ", regresa",esMayor(listaMayores1))
    print("Con la lista", listaMayores2, ", regresa", esMayor(listapares2))
    print("Con la lista", listaMayores3, ", regresa", esMayor(listaMayores3),'\n')

    print("Problema 3. Regresa una lista con cada pareja de datos intercambiados de la lista original.")
    print("Con la lista", listaInvertir1, ", regresa",invertir(listaInvertir1))
    print("Con la lista", listaInvertir2, ", regresa", invertir(listaInvertir2))
    print("Con la lista", listaInvertir3, ", regresa", invertir(listaInvertir3), '\n')

    print("Problema 4. Regresa una lista con el valor menor y mayor intercambiados de la lista original.")
    print("Con la lista", listaIntercambiar1, ", regresa", invertirMayorMenor(listaIntercambiar1))
    print("Con la lista", listaIntercambiar2, ", regresa", invertirMayorMenor(listaIntercambiar2))
    print("Con la lista", listaIntercambiar3, ", regresa", invertirMayorMenor(listaIntercambiar3), '\n')

    print("Problema 5. Regresa una lista con los números mayores o iguales al promedio de la lista original.")
    print("Con la lista", listaPromedio1, ", regresa",esMayorIgualPromedio(listaPromedio1))
    print("Con la lista",listaPromedio2, ", regresa",esMayorIgualPromedio(listaPromedio2))
    print("Con la lista", listaPromedio3, ", regresa", esMayorIgualPromedio(listaPromedio3), '\n')

    print("Problema 6. Regresa una dupla con la media y la desviación estándar de la lista original.")
    print("Con la lista", listaDesviacion1, ", regresa",calcularDesviacionyMedia(listaDesviacion1))
    print("Con la lista", listaDesviacion2, ", regresa",calcularDesviacionyMedia(listaDesviacion2))
    print("Con la lista", listaDesviacion3, ", regresa", calcularDesviacionyMedia(listaDesviacion3))

main()