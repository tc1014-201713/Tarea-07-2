#encoodong:UTF-8
#Autor: Rodrigo Rivera Salinas
#Descripcion: Programa listas

def problemaUno():
    lista=[1,2,3,2,4,60,5,8,3,22,44,55]
    lista2=[5,7,3]
    listaM=[]
    listaN=[]
    for a in lista:
        list=a%2
        if list==0:
            listaN.append(a)
    print(listaN)
    for b in lista2:
        listq=a%2
        if listq==0:
         listaM.append(a)
    print(listaM)
def problemaDos():
    lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2 = [5, 4, 3, 2]
    listaUno = []
    listaDos = []
    for a in range(0, len(lista)):
        x = lista[a]
        if a != 0:
            if x > lista[a - 1]:
                listaDos.append(x)
    print(listaDos)
    for b in range(0, len(lista2)):
        x = lista2[b]
        if b != 0:
            if x > lista2[b - 1]:
                listaUno.append(x)
    print((listaUno))
def problemaCuatro():
    lista = [5, 9, 3, 22, 19, 31, 10, 7]
    maxn = max(lista)
    minn = min(lista)
    posicionMax = lista.index(maxn)
    posicionMin = lista.index(minn)
    lista.pop(posicionMax)
    lista.pop(posicionMin)
    lista.insert(posicionMax, minn)
    lista.insert(posicionMin, maxn)
    print(lista)
    lista2 = [1, 2, 3]
    maxn1 = max(lista2)
    minn2 = min(lista2)
    posicionMax1 = lista2.index(maxn1)
    posicionMin2 = lista2.index(minn2)
    lista2.pop(posicionMax1)
    lista2.pop(posicionMin2)
    lista2.insert(posicionMax1, minn2)
    lista2.insert(posicionMin2, maxn1)
    print(lista2)
def problemaCinco():
    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista2 = [70, 80, 90]
    promedio2 = sum(lista2) / len(lista2)
    promedio = sum(lista) / len(lista)
    listaNew = []
    listaNew2 = []
    for a in lista:
        if a >= promedio:
            listaNew.append(a)
    print("hay ", len(listaNew), "numeros mayores al ", promedio)
    for b in lista2:
        if b >= promedio2:
            listaNew2.append(b)
    print("hay", len(listaNew2), "numeros mayores al ", promedio2)

def problemaSeis():
    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista2 = [1, 2, 3, 4, 5, 6]
    if len(lista) != 0 and len(lista) != 1:
        listaVacia = []
        promedio = sum(lista) / len(lista)
        for a in range(len(lista)):
            binomio = (lista[a] - promedio) ** 2
            listaVacia.append((binomio) / (len(lista) - 1))
        desciacionE = (sum(listaVacia)) ** .5
        print(promedio, desciacionE)
    if len(lista2) != 0 and len(lista2) != 1:
        listaVacia2 = []
        promedio2 = sum(lista2) / len(lista2)
        for a in range(len(lista2)):
            binomio2 = (lista2[a] - promedio2) ** 2
            listaVacia2.append((binomio2) / (len(lista2) - 1))
        desciacionEs = (sum(listaVacia2)) ** .5
        print(promedio2, desciacionEs)

def main():
    problemaUno()
    problemaDos()
    problemaCuatro()
    problemaCinco()
    problemaSeis()
main()
