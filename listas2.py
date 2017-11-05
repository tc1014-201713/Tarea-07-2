#Encoding UTF-8
#Autor: Anaid Fernanda Labat González, A01746289


def encontrarPares(lista): #regresa los elementos pares de la lista
    pares=[]
    for par in lista:
        if par%2==0: #para que el número sea par,el residuo de la division entre 2 es igual a 0
            pares.append(par)
    return pares

def mayor(lista): #regresa los valores mayores a un elemento previo
    maximos = []
    for maximo in range(0, len(lista) -1):
        if lista[maximo] < lista[maximo+1]:
            maximos.append(lista[maximo +1])
    return maximos

def intercambiar(lista): #intercambia una pareja de datos
    alreves = []
    i = 0 #número impar de datos
    p = 1 #número par de datos
    if len(lista) % 2 == 0:
        for inter in range(len(lista) // 2):
            alreves.append(lista[p])
            alreves.append(lista[i])
            i = i + 2
            p = p + 2
    else:
        for inter in range(len(lista) // 2):
            alreves.append(lista[p])
            alreves.append(lista[i])
            i = i + 2
            p = p + 2
        alreves.append(lista[-1]) # si la lista tiene una cantidad de datos impar evita que su último dato sufra cambios
    return alreves

def intercambiarMm(lista): #intercambia el número menor y el mayor
    maymen = [] #
    for mm  in range(0,len(lista)):
        if max(lista) == lista[mm]:
            maymen.append(min(lista))
        elif min(lista) == lista[mm]:
            maymen.append(max(lista))
        else:
            maymen.append(lista[mm])
    return maymen

def promedio(lista): # indica cuántos números en la lista son mayores o iguales al promedio
    igualom = 0
    for dato in range(0,len(lista)):
        if lista[dato] >= (sum(lista) / len(lista)):
            igualom += 1
    return igualom

def duplaMedia(lista): #regresa una dupla con la media y la desviación estándar
    if lista == [3] or lista == []: # si recibe una lista vacía o con 3 regresa (0,0)
        return 0,0
    else:
        media = sum(lista)/len(lista)
        sumatoria = 0
        for dato in lista:
            sumatoria = sumatoria + (dato - media)**2
        desviacion = (sumatoria/(len(lista)-1))**0.5
        return media, desviacion

def main():
    print("Problema 1. Regresa una lista con valores pares de la lista original")
    a=[1,2,3,22,4,60,5,18,53,82,50,30]
    print("Al recibir la lista:",a,"regresa:",encontrarPares(a))
    b=[5,15,9]
    print("Al recibir la lista:",b,"regresa:",encontrarPares(b))
    print("Problema 2. Regresa una lista con los valores que son mayores a un elemento previo")
    c=[5,8,6,9,10,5,14,18,2,8]
    print("Al recibir la lista:", c, "regresa:", mayor(c))
    d=[5,3,1]
    print("Al recibir la lista", d, "regresa", mayor(d))
    print("Problema 3. Regresa una lista con cada pareja de datos intercambiados ")
    e=[5,8,6,5,2,1,45,4]
    print("Al recibir la lista:", e, "regresa:", intercambiar(e))
    f=[8]
    print("Al recibir la lista:", f, "regresa:", intercambiar(f))
    g=[1,2,3,2,4,60,5,8,3,22,44,55,8]
    print("Al ingresar la lista:", g,"Regresa:", intercambiar(g))
    print("Problema 4. Regresa una lista con el valor menor y el mayor intercambiados ")
    h=[5,9,3,22,19,31,10,7]
    print("Al recibir la lista:", h, "regresa:", intercambiarMm(h))
    print("Problema 5. Regresa una lista con el número de datos que son mayores o iguales al promedio de todos los valores de la lista")
    i=[5,8,40]
    prom=sum(i)//len(i)
    print("Al recibir la lista:", i, "regresa:", promedio(i),",porque es el número de datos que son mayores o iguales al promedio que es:",prom)
    j=[5,60,40,2,5,1]
    prom1=sum(j)//len(j)
    print("Al recibir la lista:",j, "regresa:", promedio(j),",porque es el número de datos que son mayores o iguales al promedio que es:", prom1)
    print("Problema 6. Regresa una dupla con la media y la desviación estándar")
    k=[]
    print("Al recibir la lista:", k, "regresa:", duplaMedia(k) )
    l=[3]
    print("Al recibir la lista:", l, "regresa:", duplaMedia(l))
    m=[95,21,73,24,15,69,71,80,49,100,85]
    print("Al recibir la lista:", m, "regresa: ",duplaMedia(m))
main()