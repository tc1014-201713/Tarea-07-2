#encoding: UTF-8
#Autor: Jose Antonio Vazquez Gabian
def devuelvePares(lista):
  nuevalista = []
  for i in range(0,len(lista)):
     if lista[i] % 2 == 0:
         nuevalista.append(lista[i])
  return nuevalista

def mayor(mayor):
     mayor = []
     for i in range(0, len(mayor) -1):
         if mayor[i] < mayor[i +1]:
             mayor.append(mayor[i +1])
     return mayor

def juntarintercambiar(lista):
     nuevalista = []
     for i in range(0, len(lista) -1, 2):
         nuevalista.append(lista[i +1])
         nuevalista.append(lista[i])
     if len(lista) % 2 != 0:
         nuevalista.append(lista[-1])
     return nuevalista

def cambiarlista(lista):
   nuevalista = []
   for i in range(0,len(lista)):
         if max(lista) == lista[i]:
           nuevalista.append(min(lista))
         elif min(lista) == lista[i]:
             nuevalista.append(max(lista))
         else:
            nuevalista.append(lista[i])
         return nuevalista

def calcularlista(lista):
     contador = 0
     for j in range(0,len(lista)):
         if lista[j] >= (sum(lista) / len(lista)):
             contador += 1
     return contador

def hacerDesviacion(lista):
    regreso = []
    mean = 0
    desviacion = 0
    if len(lista) > 2:
         for i in range(0,len(lista)):
            mean += lista[i]
         mean = mean / len(lista)
         regreso.append(mean)
         for i in range(0,len(lista)):
             desviacion += (lista[i] - mean) ** 2
         desviacion = (desviacion / (len(lista) -1)) ** (1/2)
         regreso.append(desviacion)
         return regreso
    else:
         return [0,0]

def menu():
    print("""
    1.- Regresar una lista con los valores pares.
    2.- Regresar una lista con los valores mayores al anterior.
    3.- Regresar una lista con los valores se intercabiados de dos en dos.
    4.- Regresar una lista con valores donde mayor y menor se intercambian.
    5.- Función que devuelve un número,el cual es la cantidad de elementos mayores al promedio de la lista.
    6.- Funcion que regresa una dupla, la cual devuelve la media y la desviación estandar.
    0.- salir
    """)
    respuesta = int(input("Elige una opcion: "))
    print("")
    return respuesta
def main():
     lista = [[], [1,2,3,2,4,60,5,8,3,22,44,55],[5,7,3], [5,4,3,2], [1,2,3], [7], [5,9,3,22,19,31,10,7], [70,80,90], [1,2,3,4,5,6], [95,21,73,24,15,69,71,80,49,100,85], [3]] # todas las listas para probar
     x = menu()
     while x != 0:
         if x == 1:
             for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], devuelvePares(lista[i])))
                 print("")
         elif x == 2:
             for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], mayor(lista[i])))
                 print("")
         elif x == 3:
            for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], juntarintercambiar(lista[i])))
                 print("")
         elif x == 4:
             for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], cambiarlista(lista[i])))
                 print("")
         elif x == 5:
             for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], calcularlista(lista[i])))
                 print("")
         elif x == 6:
            for i in range(0,len(lista)):
                 print("si recibe %s, regresa %s" % (lista[i], hacerDesviacion(lista[i])))
                 print("")
         else:
            print("Error, da un valor válido")
            print("")
         x = menu()
main()