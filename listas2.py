#Encoding: UTF-8
#Autor Aaron Villanueva


def crearListaConPares(listaOriginal):
  listaPares=[]
  for i in listaOriginal:
    if i%2==0:
      listaPares.append(i)
  return(listaPares)
      
def crearListaMayores(listaOriginal):
  listaMayores=[]
  anterior=0
  for i in listaOriginal:
    if i > anterior:
      listaMayores.append(i)
    anterior=i
  return(listaMayores)

def intercambiarPares(listaOriginal):    
    

    
def definirNumerosMayoresAlPromedio(listaOriginal):
  lenOriginal=len(listaOriginal)
  promedio= sum(listaOriginal) / lenOriginal
  listaFinal=[]
  contador=0
  for j in listaOriginal:
    if j=>promedio:
      contador+=1
      listaFinal.append(j)
  return(contador, promedio,listaFinal)
      
def cambiarPosicionMinMax(listaOriginal):
  valormin=min(listaOriginal)
  valormax=max(listaOriginal)
  posicionmin=listaOriginal.index(valormin)
  print(posicionmin)
  posicionmax=listaOriginal.index(valormax)
  print(posicionmax)
  listaIntercambiada=listaOriginal[:]
  listaIntercambiada.remove(valormax)
  listaIntercambiada.insert(posicionmin,valormax)
  listaIntercambiada.remove(valormin)
  listaIntercambiada.insert(posicionmax,valormin)
  return(listaIntercambiada)
  
  
  
    
def calcularMediaYDesviacionEstandar(listaOriginal):
  lenOriginal=len(listaOriginal)
  media=sum(listaOriginal) / lenOriginal
    
    
def main():

main()
    
