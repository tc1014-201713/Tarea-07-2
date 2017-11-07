# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696
# Segunda tarea de listas


def juntarPares(lista1):
    listaConPares = []
    if lista1 != []:
        leng = len(lista1)
        for i in range(leng):
            if lista1[i] % 2 == 0:
                listaConPares.append(lista1[i])
        final = listaConPares
        return final

    else:
        final = "Lista vacía"
        return final

def crearListaElementosMayores(lista1):
    leng = len(lista1)
    listaElementos = []
    if lista1 != []:
        for i in range(1, leng, 1):
            if lista1[i] > lista1[i - 1]:
                listaElementos.append(lista1[i])
        return listaElementos
    else:
        return "lista vacía"

def crearListaConElementosAlReves(lista1):
    listaReves=[]
    if lista1 != []:
        leng = len(lista1)
        if leng % 2 != 0:
            leng = len(lista1) - 1
            for i in range(1, leng, 2):
                listaReves.append(lista1[i])
                listaReves.append(lista1[i - 1])
            listaReves.append(lista1[leng])
            return listaReves

        else:
            for i in range(1, leng, 2):
                listaReves.append(lista1[i])
                listaReves.append(lista1[i - 1])
            return listaReves
    else:
        return "Lista vacía"


def cambiarMaxyMin(lista1):
    reassembledList=[]
    if lista1 != []:
        maxilist = max(lista1)
        minilist = min(lista1)
        leng = len(lista1)
        for i in range(leng):
            reassembledList.append(lista1[i])
            if lista1[i] == maxilist:
                spotMax = i
            elif lista1[i] == minilist:
                spotMin = i
        reassembledList.insert(spotMin, maxilist)
        reassembledList.pop(spotMin + 1)
        reassembledList.insert(spotMax, minilist)
        reassembledList.pop(spotMax + 1)
        return reassembledList

    else:
        return "Lista vacía"

def calcularPromedios(lista1):
    listaMayores=[]
    if lista1 != []:
        promedio = sum(lista1) // len(lista1)
        counterMayores = 0
        for i in range(len(lista1)):
            if lista1[i] >= promedio:
                counterMayores += 1
        return counterMayores
    else:
        return "lista Vacía"

def calcularMeanYDesv(lista1):
    if lista1 != [] and lista1 !=[3]:
        mean = float(sum(lista1) / len(lista1))
        desviacion = 0
        for i in range(len(lista1)):
            desviacion = (lista1[i] - mean) ** 2 + desviacion
        desviacion2 = (desviacion / (len(lista1) - 1)) ** 0.5
        return (("%.2f, %.6f")% (mean, desviacion2))
    else:
        return (0, 0)


def main():
    listaPares1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("Con", listaPares1, "regresa", juntarPares(listaPares1))
    listaPares2 = [5,7,3]
    print("Con", listaPares2, "regresa", juntarPares(listaPares2))
    listaElementos1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("con", listaElementos1, "regresa", crearListaElementosMayores(listaElementos1))
    listaElementos2 = [5,4,3,2]
    print("con", listaElementos2, "regresa", crearListaElementosMayores(listaElementos2))
    listaReves1 =[1,2,3,2,4,60,5,8,3,22,44,55]
    listaReves2 =[1,2,3]
    listaReves3 = [7]
    print("Si recibe", listaReves1, "regresa", crearListaConElementosAlReves(listaReves1))
    print("Si recibe", listaReves2, "regresa", crearListaConElementosAlReves(listaReves2))
    print("Si recibe", listaReves3, "regresa", crearListaConElementosAlReves(listaReves3))
    listaMinMax1 = [5,9,3,22,19,31,10,7]
    listaMinMax2 = [1,2,3]
    print("Si recibe", listaMinMax1, "regresa", cambiarMaxyMin(listaMinMax1))
    print("Si recibe", listaMinMax2, "regresa", cambiarMaxyMin(listaMinMax2))
    listaMayores1 = [70, 80, 90]
    listaMayores2 = [95,21,73,24,15,69,71,80,49,100,85]
    print("Si recibe", listaMayores1, "regresa", calcularPromedios(listaMayores1))
    print("Si recibe", listaMayores2, "regresa", calcularPromedios(listaMayores2))
    listaDesv1 = [1,2,3,4,5,6]
    listaDesv2 = [95,21,73,24,15,69,71,80,49,100,85]
    listaDesv3 = []
    listaDesv4 = [3]
    print("Si recibe", listaDesv1, "regresa", calcularMeanYDesv(listaDesv1))
    print("Si recibe", listaDesv2, "regresa", calcularMeanYDesv(listaDesv2))
    print("Si recibe", listaDesv3, "regresa", calcularMeanYDesv(listaDesv3))
    print("Si recibe", listaDesv4, "regresa", calcularMeanYDesv(listaDesv4))


main()