#Oscar Zuñiga Lara
#A01654827

#Listas ejercicio 1/////////////////////////////////
lista11 = [1,2,3,2,4,60,5,8,3,22,44,55]
lista12 = [5,7,3]
#Listas ejercicio 2/////////////////////////////////
lista21 = [1,2,3,2,4,60,5,8,3,22,44,55]
lista22 = [5,4,3,2]
#Listas ejercicio 3 ////////////////////////////////
lista31 = [1,2,3,2,4,60,5,8,3,22,44,55]
lista32 = [1,2,3]
lista33 = [7]
#Listas ejercicio 4 ////////////////////////////////
lista41 = [5,9,3,22,19,31,10,7]
lista42 = [1,2,3]
#Listas ejercicio 5 ////////////////////////////////
lista51 = [70,	80,	90]
lista52 = [95,21,73,24,15,69,71,80,49,100,85]
#Listas ejercicio 5 ////////////////////////////////
lista61 = [1,2,3,4,5,6]
lista62 = [95,21,73,24,15,69,71,80,49,100,85]
lista63 = []
lista64 = [3]




def ejercicio1(listao):
    lista1 = []
    aaa = len(listao)
    for a in range(0,aaa):
        o = listao[a]
        if o // 2 == o / 2 :
            lista1.append(o)

    print("Tu lista original es: ",listao, "La lista sin numeros impares es: ",lista1)


def ejercicio2(listao):
    lista2 = []
    aaa = len(listao)
    for a in range(0, aaa):
        o = listao[a - 1]
        u = listao[a]
        if u > o:
            lista2.append(u)
    print("Si recibe: ",listao, "Regresa: ",lista2)


def ejercicio3(listao):
    lista3 =[]
    aaa = len(listao)
    for a in range(0,aaa-1,2):
        if aaa // 2 == aaa / 2:
            lista3.append(listao[a + 1])
            lista3.append(listao[a])
    print("Si recibe: ",listao, "Regresa: ",lista3)


def ejercicio4(listao):
    lista4 = []
    aaa = len(listao)
    for a in range(0,aaa):
        if listao[a] == max(listao):
            o = listao[a]
            b = a
        if listao[a] == min(listao):
            u = listao[a]
            c = a
    for a in range(0,aaa):
        if a != b and a != c:
            lista4.append(listao[a])
        elif a == b:
            lista4.append(listao[c])
        elif a == c:
            lista4.append(listao[b])
    print("Si recibe: ",listao, "Regresa: ",lista4)

def ejercicio5(listao):
    c = 0
    d = 0
    lista5 = []
    aaa = len(listao)
    for a in range(0,aaa):
        b = listao[a]
        c = c + b
    prom = c / aaa
    for a in range(0,aaa):
        if prom <= listao[a]:
            d += 1
    print("Si recibe : " , listao, "Regresa" , d)

def ejercicio6(listao):
    mean = 0
    d = 0
    lista6 = 0
    aaa = len(listao)
    if len(listao) > 1:
        for a in range(0,aaa):
            mean += listao[a]
        mean = mean / aaa
        for a in range(0,aaa):
            d += (listao[a] - mean)**2
        lista6 = (d/(aaa-1))**.5
    print("Si recibe: " , listao, "regresa: ", "(" ,mean,",", lista6 ,")")


def main():
    ejercicio1(lista11)
    ejercicio1(lista12)

    print("Ejercicio 2, recibe	como	parámetro	una	lista	y regresa	una	nueva	lista,	con	los	valores	que	son	mayores	a	un	elemento	previo.	")
    ejercicio2(lista21)
    ejercicio2(lista22)

    print("Ejercicio 3, recibe	una	lista	de	valores	y	regresa	una	nueva	lista	con	cada	pareja	de	datos	intercambiados.")
    ejercicio3(lista31)
    ejercicio3(lista32)
    ejercicio3(lista33)

    print("Ejercicio 4, recibe	una	lista	de	valores	y	regresa	una	nueva	lista	con	el	valor	menor	y	mayor	intercambiados. ")
    ejercicio4(lista41)
    ejercicio4(lista42)

    print("Ejercicio 5, recibe	una	lista	de	valores	y	regresa	el	número	de	datos	que	son	mayores	o	iguales	al	promedio	de	todos	los	valores	de	la	lista.	")
    ejercicio5(lista51)
    ejercicio5(lista52)

    print("Ejercicio 6, calcula media y desviacion estandard")
    ejercicio6(lista61)
    ejercicio6(lista62)
    ejercicio6(lista63)
    ejercicio6(lista64)


main()