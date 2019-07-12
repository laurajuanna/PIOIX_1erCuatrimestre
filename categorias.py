from collections import Counter # Utilizado para el Poker

# segun los dados obtenidos y un valor de dado pedido al usuario anteriormente
# recorre la lista de dados para averiguar cuantas veces está ese dado repetido
# finalmente imprime una cadena con esa información y retorna los puntos obtenidos
# al multiplicar el valor del dado x la cantidad de veces que se ha repetido
def SalidaDeNumero(dados,valor):
  cantidad_de_repeticiones=0
  for i in dados:
      if i==valor:
          cantidad_de_repeticiones+=1
  multiplicacion = (valor*cantidad_de_repeticiones)
  print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces. Obtuvo",multiplicacion,"puntos.")
  return multiplicacion

# La I toma el primer valor del dado hasta el último
# Luego pregunta valor por valor la cantidad de veces que está repetido
# Si el valor i esta 5 veces dentro de la jugada es GENERALA y retorna True
# De lo contrario retorna False
def EsGenerala(dados):
   for i in range (0,len(dados)):
      if dados.count(dados[i])==5:
          return True
      else:
          return False

# Para encontrar el poker se debe importar el modulo Counter
def EsPoker(dados):
   cuenta = Counter(dados) # cuenta cuantas repeticiones hay de cada valor
   cuentaRepeticiones = (cuenta.most_common(1)) # genera una lista mostrando qué valor es el mas repetido y cuántas veces se repitió
   maxRepeticion = cuentaRepeticiones[0][1] # muestra el número de veces que se repitió el valor mas repetido
   if maxRepeticion == 4:# si el valor mas repetido se repitió cuatro veces devuelve True, sino False.
       return True
   else:
       return False

# La i toma el primer valor de jugada hasta el ultimo,
# pregunta valor por valor la cantidad de veces que está repetido
# si el valor i esta 3 veces dentro de la jugada, me retorna True
# si hay otro valor que está 2 veces me retorna True.
# Si ambos se cumplen retorna True, de lo contrario retorna False.
def esFull(dados):
    hay_tres=False
    hay_dos=False
    for i in range (0,len(dados)):
        if dados.count(dados[i])==3:
            hay_tres=True
        if dados.count(dados[i])==2:
           hay_dos=True
    return hay_tres and hay_dos

# La función establece las dos posibles escaleras que existen dentro del juego.
# Luego ordena la jugada, si es igual a alguna de las dos escaleras retorna true.
def esEscalera(dados):
    esc1=[1,2,3,4,5]
    esc2=[2,3,4,5,6]
    if sorted(dados)==esc1 or sorted(dados)==esc2:
        return True
    else:
        return False
