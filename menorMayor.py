#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Hacer una funcion que tome como entrada una lista y regrese los valores mayores y menores intercambiados.
def calcularMayorYMenor(lista):
    if len(lista) >= 1:
        Mm =lista [:]
        M = max(lista)
        m = min(lista)
        intercambioM = Mm.index(M)
        intercambiom = Mm.index(m)
        Mm.remove(M)
        Mm.remove(m)
        Mm.insert(intercambiom, M)
        Mm.insert(intercambioM, m)
    else:
        Mm = []
    return (Mm)

def main():
    lista1 = [5, 9, 3, 22, 19, 31, 10, 7]
    lista2 = [1, 2, 3]
    print("Dada la lista", lista1, "la lista con el mayor y menor intercambiados es:", calcularMayorYMenor(lista1))
    print("Dada la lista:", lista2,"la lista con el mayor y menor intercambiados es:", calcularMayorYMenor(lista2))


main()