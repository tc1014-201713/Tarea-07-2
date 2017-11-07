#encoding: utf-8
#coded by Jordan
#this programs tests many list on different cases

from math import sqrt

def exe1(list):
    newList = []
    for i in range(len(list)):
        if not list[i] % 2:
            newList.append(list[i])
    return newList

def exe2(list):
    newList = []
    for i in range(len(list)-1, 0, -1):
        if list[i] > list[i-1]:
            newList.append(list[i])
    newList.reverse()
    return newList

def exe3(list):
    newList = []
    if len(list) > 1:
        for i in range(0, len(list)-1, 2):
            newList.append(list[i+1])
            newList.append(list[i])
            if len(list) % 2:
                newList.append(list[len(list)-1])
    else:
        newList.append(list[0])
    return newList

def exe4(list):
    newList = []
    for i in range(len(list)):
        newList.append(list[i])
    minN = min(newList)
    maxN = max(newList)
    newList[newList.index(maxN)] = minN
    newList[newList.index(minN)] = maxN
    return newList

def exe5(list):
    newList = []
    count = 0
    prom = sum(list)/len(list)
    for i in range(len(list)):
        if list[i] >= prom:
            count += 1
            newList.append(list[i])
    return count, prom, newList

def exe6(list):
    mean = 0
    deviation = 0
    variation = 0
    if len(list) > 1:
        for i in range(len(list)):
            mean += list[i]
        mean /= len(list)
        for i in range(len(list)):
            variation += (list[i] - mean)**2
        deviation = sqrt(variation/(len(list)-1))
    return mean, deviation

def main():
    print("""Problema 1. Regresa una lista con los valores pares de la lista original. 
    Con la lista [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], regresa %s
    Con la lista [5, 7, 3], regresa %s
    Con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9], regresa %s
""" % (str(exe1([1,2,3,2,4,60,5,8,3,22,44,55])), str(exe1([5,7,3])), str(exe1([1,2,3,4,5,6,7,8,9]))))
    print("""Problema 2. Regresa una lista con los valores que son mayores a un elemento previo.
    Con la lista [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], regresa %s
    Con la lista [5, 4, 3, 2], regresa %s
    Con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9], regresa %s
""" % (str(exe2([1,2,3,2,4,60,5,8,3,22,44,55])), str(exe2([5,4,3,2])), str(exe2([1,2,3,4,5,6,7,8,9]))))
    print("""Problema 3. Regresa una lista con las posiciones de parejas intercambiadas.
    Con la lista [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], regresa %s
    Con la lista [1, 2, 3], regresa %s
    Con la lista [7], regresa %s
""" % (str(exe3([1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55])), str(exe3([1, 2, 3])), str(exe3([7]))))
    print("""Problema 4. Regresa una lista con las posiciones del mínimo y máximo intercambiadas.
    Con la lista [5, 9, 3, 22, 19, 31, 10, 7], regresa %s
    Con la lista [1, 2, 3], regresa %s
    Con la lista [7, 9], regresa %s
""" % (str(exe4([5, 9, 3, 22, 19, 31, 10, 7])), str(exe4([1, 2, 3])), str(exe4([7, 9]))))
    c1, p1, l1 = exe5([70, 80, 90])
    c2, p2, l2 = exe5([95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85])
    c3, p3, l3 = exe5([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("""Problema 5. Regresa el número de datos que son mayores o iguales al promedio de la lista, y la nueva lista con los valores.
    Con la lista [70, 80, 90], regresa %i. Porque el promedio es %.2f y hay %i valores mayores o iguales a %.2f %s
    Con la lista [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85], regresa %i. Porque el promedio es %.2f y hay %i valores mayores o iguales a %.2f %s
    Con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9], regresa %i. Porque el promedio es %.2f y hay %i valores mayores o iguales a %.2f %s
""" % (c1, p1, c1, p1, l1, c2, p2, c2, p2, l2, c3, p3, c3, p3, l3))
    m1, d1 = exe6([1, 2, 3, 4, 5, 6])
    m2, d2 = exe6([95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85])
    m3, d3 = exe6([])
    m4, d4 = exe6([3])
    print("""Problema 6. Regresa una dupla con la media y la desviación estandar.
    Con la lista [1, 2, 3, 4, 5, 6], regresa (%.2f, %.6f)
    Con la lista [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85], regresa (%.2f, %.4f)
    Con la lista [], regresa (%.2f, %.2f)
    Con la lista [3], regresa (%.2f, %.2f)
""" % (m1, d1, m2, d2, m3, d3, m4, d4))

main()