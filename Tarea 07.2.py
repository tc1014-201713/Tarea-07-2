#encoding: UTF-8
#Ernesto Ibhar Guevara Gómez
#A01746121
# El porgrama prueba distintos ejercicios en base a problemas relacionados con listas.
#Definimos listas de prueba (constantes)

# Ejercicio 1
LISTA_1 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA_2 = [5,7,3]
LISTA_3 =[5]
LISTA_4 = []

#Ejercicio 2
LISTA_5 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA_6 = [5,4,3,2]
LISTA_7 = [8]
LISTA_8 = []

# Ejercicio 3
LISTA_9 = [1,2,3,2,4,60,5,8,3,22,44,55]
LISTA_10 = [1,2,3]
LISTA_11 = [7]
LISTA_12 = []

# Ejercicio 4
LISTA_13 = [5,9,3,22,19,31,10,7]
LISTA_14 = [1,2,3]
LISTA_15 = [3]
LISTA_16 = []

# Ejercicio 5
LISTA_17 = [70, 80, 90]
LISTA_18 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA_19 = [2]
LISTA_20 = []

# Ejercicio 6
LISTA_21 = [1,2,3,4,5,6]
LISTA_22 = [95,21,73,24,15,69,71,80,49,100,85]
LISTA_23 = [3]
LISTA_24 = []


#Funcion para realizar el primer ejercicio
def enlistarPares(lista):
    nueva_Lista = []
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            nueva_Lista.append(lista[i])
    return nueva_Lista

#Funcion para realizar el segundo ejercicio
def calcularMayoresAPrevio(lista):
    nueva_Lista2 = []
    for i in range (0,len(lista) -1):
        if lista[i] < lista[i+1]:
            nueva_Lista2.append(lista[i+1])
    return nueva_Lista2

#Funcion para realizar el tercer ejercicio
def emparejarIntercambiados(lista):
    nuevalista=[]
    for i in range(0,len(lista)-1,2):
        nuevalista.append(lista[i+1])
        nuevalista.append(lista[i])
    if len(lista)%2!=0:
        nuevalista.append(lista[-1])
    return nuevalista
#Funcion para realizar el cuarto ejercicio
def intercambiarMayoresYMenores(lista):
    nuevalista=lista[:]
    if len(lista)<=1:
        nuevalista=lista[:]
    else:
        mayor=lista.index(max(lista))
        menor=lista.index(min(lista))
        nuevalista.remove(min(lista))
        nuevalista.remove(max(lista))
        nuevalista.insert(mayor-1,min(lista))
        nuevalista.insert(menor,max(lista))
    return nuevalista

#Funcion para realizar el quinto ejercicio
def calcularMayoresIguales(lista):
    nueva_Lista5 = []
    promedio = sum(lista) / len(lista)
    for i in range(0, len(lista)):
        if lista[i] >= promedio:
            nueva_Lista5.append(lista[i])
    return nueva_Lista5

def calcularMedia(lista):
    nuevalista=[]
    if len(lista)>0:
        promedio=sum(lista)/len(lista)
        for i in range (0,len(lista)):
            if lista[i]>=promedio:
                nuevalista.append(lista[i])
    else:
        nuevalista=[]
    return nuevalista
#Funcion que realiza el sexto ejercicio
def regresarDuplas(lista):
    nuevalista=[]
    suma=0
    if len(lista)>1:
        promedio=sum(lista)/len(lista)
        for i in lista:
            suma+=(i-promedio)**2
        desviacion=suma/(len(lista)-1)
        desviacionRaiz=desviacion**.5
        nuevalista.append(promedio)
        nuevalista.append(desviacionRaiz)
    else:
        nuevalista=[0,0]
    return nuevalista

def main():
    print("Si recibe",LISTA_9,", regresa",enlistarPares(LISTA_9))#Ejemplo Ejercicio 1
    print("Si recibe",LISTA_5,", regresa",calcularMayoresAPrevio(LISTA_5))#Ejemplo Ejercicio 2
    print("Si recibe",LISTA_9,", regresa",emparejarIntercambiados(LISTA_9))#Ejemplo Ejercicio 3
    print("Si recibe",LISTA_13,", regresa",intercambiarMayoresYMenores(LISTA_13))#Ejemplo Ejercicio 4
    print("Si recibe",LISTA_18,", regresa",calcularMayoresIguales(LISTA_18))#Ejemplo Ejercicio 5
    print("Si recibe",LISTA_18,", regresa",regresarDuplas(LISTA_18))#Ejemplo Ejercicio 6

main()