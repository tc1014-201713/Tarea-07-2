# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Tarea 2 sobre listas

def calcularPares(lista):
    '''
    Regresa una lista con los valores pares de la lista original.
    :param lista:
    :return: nueva
    '''
    nueva = []
    for dato in lista:
        if dato % 2 == 0:
            nueva.append(dato)
    return nueva

def calcularMayoresAPrevio(lista):
    '''
    Regresa una lista con los valores que son mayores a un elemento previo.
    :param lista:
    :return: nueva
    '''
    nueva = []
    if len(lista) > 0:
        previo = lista[0]
    for dato in lista:
        if dato > previo:
            nueva.append(dato)
        previo = dato
    return nueva

def intercambiarParejas(lista):
    '''
    Regresa una lista con cada pareja de datos intercambiados de la lista original.
    :param lista:
    :return: nueva
    '''
    nueva = []
    for i in range(len(lista)):
        if i % 2 == 0:
            nueva.insert(i+1,lista[i])
        elif i % 2 == 1:
            nueva.insert(i-1,lista[i])
    return nueva

def intercambiarMenorYMayor(lista):
    '''
    Regresa una lista con el valor menor y mayor intercambiados de la lista original.
    :param lista:
    :return:
    '''
    nueva = lista[::]
    if len(lista) > 0:
        menor_l = min(lista)
        mayor_l = max(lista)
        menor_n = min(nueva)
        mayor_n = max(nueva)
        i_menor_l = lista.index(menor_l)
        i_mayor_l = lista.index(mayor_l)
        nueva.remove(menor_n)
        nueva.remove(mayor_n)
        nueva.insert(i_menor_l,mayor_l)
        nueva.insert(i_mayor_l,menor_l)
    return nueva

def calcularMayoresOIgualesAPromedio(lista):
    '''
    Regresa una lista con los números mayores o iguales al promedio de la lista original.
    :param lista:
    :return: nueva
    '''
    nueva = []
    if len(lista) > 0:
        promedio = sum(lista)/len(lista)
        for dato in lista:
            if dato >= promedio:
                nueva.append(dato)
    return nueva

def calcularMediaYDesviacion(lista):
    '''
    Regresa una dupla con la media y la desviación estándar de la lista original.
    :param lista:
    :return: media, desviación estándar
    '''
    n = len(lista)
    if n == 0:
        media = 0
    else:
        media = sum(lista) / n
    lista_c_diferencia = []
    for x in lista:
        c_diferencia = (x - media)**2
        lista_c_diferencia.append(c_diferencia)
    des = sum(lista_c_diferencia) / (n-1)
    desviacion = des ** 0.5
    return (media,desviacion)

def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa",calcularPares([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista [5,7,3], regresa",calcularPares([5,7,3]))
    print("Con la lista [], regresa",calcularPares([]))
    print("----------------------------------------")
    print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo.")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa",calcularMayoresAPrevio([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista [5,4,3,2], regresa",calcularMayoresAPrevio([5,4,3,2]))
    print("Con la lista [], regresa",calcularMayoresAPrevio([]))
    print("----------------------------------------")
    print("Problema 3. Regresa una lista con cada pareja de datos intercambiados de la lista original.")
    print("Con la lista [1,2,3,2,4,60,5,8,3,22,44,55], regresa",intercambiarParejas([1,2,3,2,4,60,5,8,3,22,44,55]))
    print("Con la lista [1,2,3], regresa",intercambiarParejas([1,2,3]))
    print("Con la lista [], regresa",intercambiarParejas([]))
    print("----------------------------------------")
    print("Problema 4. Regresa una lista con el valor menor y mayor intercambiados de la lista original.")
    print("Con la lista [5,9,3,22,19,31,10,7], regresa",intercambiarMenorYMayor([5,9,3,22,19,31,10,7]))
    print("Con la lista [1,2,3], regresa",intercambiarMenorYMayor([1,2,3]))
    print("Con la lista [], regresa",intercambiarMenorYMayor([]))
    print("----------------------------------------")
    print("Problema 5. Regresa una lista con los números mayores o iguales al promedio de la lista original.")
    print("Con la lista [70, 80, 90] regresa",calcularMayoresOIgualesAPromedio([70, 80, 90]))
    print("Con la lista [95,21,73,24,15,69,71,80,49,100,85] regresa",calcularMayoresOIgualesAPromedio([95,21,73,24,15,69,71,80,49,100,85]))
    print("Con la lista [] regresa",calcularMayoresOIgualesAPromedio([]))
    print("----------------------------------------")
    print("Problema 6. Regresa una dupla con la media y la desviación estándar de la lista original.")
    print("Con la lista [1,2,3,4,5,6] regresa",calcularMediaYDesviacion([1,2,3,4,5,6]))
    print("Con la lista [95,21,73,24,15,69,71,80,49,100,85] regresa",calcularMediaYDesviacion([95,21,73,24,15,69,71,80,49,100,85]))
    print("Con la lista [] regresa",calcularMediaYDesviacion([]))

main()