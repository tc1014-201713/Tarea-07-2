#encoding: UTF-8
#Autor: Luis Miguel Baqueiro
#Tarea lsitas 2

def regresaPares(lista): # primer ejercicio
    nuevalista = [] # genera la lista para regresar
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0: # localiza los valores pares
            nuevalista.append(lista[i]) # los agrega
    return nuevalista # regresa la lista

def mayor(lista): # segundo ejercicio
    nuevalista = [] # genera la lista para regresar
    for i in range(0, len(lista) -1):
        if lista[i] < lista[i +1]: # calcula si es mayor que el anterior
            nuevalista.append(lista[i +1]) # lo agrega
    return nuevalista # regresa la lista

def intercambiar(lista): # tercer ejercicio
    nuevalista = [] # crea la lista para regresar
    for i in range(0, len(lista) -1, 2): # busca el valor
        nuevalista.append(lista[i +1]) # agrega el 2°
        nuevalista.append(lista[i]) # agrega el 1°
    if len(lista) % 2 != 0: # comprueba si es inpar la lista
        nuevalista.append(lista[-1]) # agrega el úlitmo valor
    return nuevalista # regresa la lista

def intercambiarm(lista): # cuarto ejercicio
    nuevalista = [] # crea la lista para regresar
    for i in range(0,len(lista)): # busca un valor
        if max(lista) == lista[i]: # si es maximo
            nuevalista.append(min(lista)) # agrega minimo
        elif min(lista) == lista[i]: # si es minimo
            nuevalista.append(max(lista)) # agrega maximo
        else: # si no es nada
            nuevalista.append(lista[i]) # agrega el valor
    return nuevalista # regresa la lista

def promedio(lista): # quinto ejercicio
    contador = 0 # crea el contador
    for i in range(0,len(lista)): # buasca el valor
        if lista[i] >= (sum(lista) / len(lista)): # ve si el valor es mayor al promedio
            contador += 1 # le suma 1
    return contador # regresa la cantidad de valores mayores al promedio

def mediaYDesviacion(lista): # sexto ejercicio
    regreso = [] # crea una lista con el promedio ( mean) y la desviacion (deviation)
    mean = 0 # promedio
    deviation = 0 # desviación
    if len(lista) > 2: # si la lista tiene mas de 2 valores
        for i in range(0,len(lista)): # busca un valor
            mean += lista[i] # se lo suma al promedio
        mean = mean / len(lista) # la suma de todos los valores sobre la cantidad de valores
        regreso.append(mean) # agrega ese valor a la lista
        for i in range(0,len(lista)): # busca un valor
            deviation += (lista[i] - mean) ** 2 # lo suma a la desviacion y le resta el promedio y lo eleva al cuadrado
        deviation = (deviation / (len(lista) -1)) ** (1/2) # la suma de todos los valores menos el promedio al cuadrado entre la cantidad de los valores -1 todo eso su raiz
        regreso.append(deviation) # agrega la desviacion a lo que se regresa
        return regreso # regresa el resultado
    else: # si no tiene mas de dos valores
        return [0,0] # no se puede sacar nada :P

def menu(): # crea el menu
    print("""0.- salir
1.- Probar la función que devuelve una lista cullos valores sean pares.
2.- Probar la función que devuelve una lista cullos valores sean mayores al anterior.
3.- Probar la función que devuelve una lista cullos valores se intercabian de dos en dos
4.- Probar la función que devuelve una lista cullos valores mayor y menor se intercambian
5.- Probar la función que devuelve una número, este es la cantidad de elementos mayores al promedio de la lista
6.- Probar la función que devuelve una dupla, la cual devuelve la media y la desviación estandar
""")
    respuesta = int(input("Que desea hacer? "))
    print("")
    return respuesta


def main():
    lista = [[], [1,2,3,2,4,60,5,8,3,22,44,55],[5,7,3], [5,4,3,2], [1,2,3], [7], [5,9,3,22,19,31,10,7], [70,80,90], [1,2,3,4,5,6], [95,21,73,24,15,69,71,80,49,100,85], [3]] # todas las listas para probar
    m = menu() # pregunta que quieres hacer
    while m != 0: # ciclo para salir
# los for dentro de esto son para probar todos los valores de la lista
        if m == 1:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], regresaPares(lista[i])))
                print("")
        elif m == 2:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], mayor(lista[i])))
                print("")
        elif m == 3:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], intercambiar(lista[i])))
                print("")
        elif m == 4:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], intercambiarm(lista[i])))
                print("")
        elif m == 5:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], promedio(lista[i])))
                print("")
        elif m == 6:
            for i in range(0,len(lista)):
                print("si recibe %s, regresa %s" % (lista[i], mediaYDesviacion(lista[i])))
            print("")
        else: # si no es un valor valido
            print("Usa un valor válido")
            print("")
        m = menu() # cerrar el ciclo

main()