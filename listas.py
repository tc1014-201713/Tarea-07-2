#Encoding: UTF-8
#Autor: Juan Sebastián Lozano Derbez
#Listas 2

def hacerprob1(listauno):
    pares = []
    for numero in (listauno):
        if numero % 2 == 0:
            pares.append(numero)
    return pares


def hacerprob2(listauno):
    lista = []

    counter1 = 0
    counter2 = 1

    while counter2 <= len(lista):
        if listauno[counter2] > listauno[counter1]:
            lista.append(listauno[counter2])
            counter1 += 1
            counter2 += 1

    return lista

def hacerprob5(listauno):
    vacioluegolleno = []

    if len(listauno) == 0:
        return vacioluegolleno

    promedio = sum(listauno) / len(listauno)

    for numero in listauno:
        if numero >= promedio:
            vacioluegolleno.append(numero)

    return vacioluegolleno

def hacerprob4(listauno):
    idk = []

    if len(listauno) > 1:

        for i in range(0, len(listauno) - 1, 2):
            idk.append(listauno[i + 1])
            idk.append(listauno[i])

            if len(listauno) % 2:
                idk.append(listauno[len(listauno) - 1])

    else:
        idk.append(listauno[0])

    return idk


def hacerprob3(listauno):
    vacioluegolleno = []

    if len(listauno) == 0:
        return vacioluegolleno

    vacioluegolleno = listauno[::1]

    mayor = max(vacioluegolleno)
    menor = min(vacioluegolleno)

    ceroparamayor = 0
    ceroparamenor = 0

    for x in range(len(vacioluegolleno)):
        if vacioluegolleno[x] == mayor:
            ceroparamayor = x
        if vacioluegolleno[x] == menor:
            ceroparamenor = x

    medio = vacioluegolleno[ceroparamayor]

    vacioluegolleno[ceroparamayor] = vacioluegolleno[ceroparamenor]
    vacioluegolleno[ceroparamenor] = medio

    return vacioluegolleno

def hacerprob6(listauno):
    media = 0
    desv = 0
    desvest = 0

    if len(listauno) > 1:
        for i in range(len(listauno)):
            media += listauno[i]

        media /= len(listauno)

        for i in range(len(listauno)):
            desvest += (listauno[i] - media) ** 2

        desv = (desvest / (len(listauno) - 1)) ** 1 / 2

    return (media, desv)


def main():
    listauno = [1,2,3,2,4,60,5,8,3,22,44,55]

    print("1) Función que recibe como parámetro una lista de números enteros y regresa UNA NUEVA lista con los valores pares de la lista original.")
    print("Con la lista", listauno,"la solucion es: ", hacerprob1(listauno))
    print("Con la lista", [5,7,3], "la solucion es: ", hacerprob1([5,7,3]))
    print("Con la lista", [], "la solucion es: ", hacerprob1([]))
    print("")



    print("2) Función que recibe como parámetro una lista y regresa una nueva lista, con los valores que son mayores a un elemento previo.")
    print("Con la lista", listauno, "la solucion es: ", hacerprob2(listauno))
    print("Con la lista", [5,4,3,2], "la solucion es: ", hacerprob2([5,4,3,2]))
    print("Con la lista", [], "la solucion es: ", hacerprob1([]))
    print("")

    print("3) Función que recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiados. Si el número de datos es impar, el último elemento no cambia.")
    print("Con la lista", listauno, "la solucion es: ", hacerprob3(listauno))
    print("Con la lista", [1,2,3], "la solucion es: ", hacerprob3([1,2,3]))
    print("Con la lista", [], "la solucion es: ", hacerprob3([]))
    print("")

    print("4) Función que recibe una lista de valores y regresa una nueva lista con el valor menor y mayor intercambiados. Suponga que los valores son únicos.")
    print(hacerprob4(listauno))
    print("Con la lista", [1, 2, 3], "la solucion es: ", hacerprob4([1, 2, 3]))
    print("Con la lista", [], "la solucion es: ", hacerprob3([]))
    print("")

    print("5) Función que recibe una lista de valores y regresa el número de datos que son mayores o iguales al promedio de todos los valores de la lista.")
    print(hacerprob5(listauno))
    print("Con la lista", [1, 2, 3], "la solucion es: ", hacerprob5([1, 2, 3]))
    print("Con la lista", [], "la solucion es: ", hacerprob5([]))
    print("")


    print("6) Función que recibe una lista de números y regresa una dupla con la media y la desviación estándar.")
    print(hacerprob6(listauno))
    print("Con la lista", [1, 2, 3], "la solucion es: ", hacerprob6([1, 2, 3]))
    print("Con la lista", [], "la solucion es: ", hacerprob6([]))
    print("")


main()



