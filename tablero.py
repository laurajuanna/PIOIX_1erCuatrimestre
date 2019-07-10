from tabulate import tabulate

jugadores = []
puntajeParcial = [['1'],['2'],['3'],['4'],['5'],['6'],['E'],['F'],['P'],['G'],['GD'],['']]

def ingresoCantidadJug ():#Esta función es para obtener y retornar la cantidad de jugadores ingresada por el usuario.
    cantidad = input("Por favor, ingrese la cantidad de jugadores: ")
    esValido = False
    while (esValido==False):# Lo que sigue sirve para validar errores de tipeo
        try:
            val = int(cantidad)
            esValido = True
        except ValueError:
            print("\n*** ERROR! Lo ingresado no fue recibido correctamente.")
            print("Por favor, ingrese una cantidad válida usando NÚMEROS.")
            cantidad = input("\nPor favor, ingrese la cantidad de jugadores: ")
    return int(cantidad)

def ingresoNombres (cantidad):#Esta función sirve para agregar los nombres de los jugadores a la lista Vacía de jugadores
    for cantidad in range(0, cantidad):
        jugadores.append(input("Por favor, ingrese el nombre del jugador: "))

def reanudarNombres (nombres): # Agrega una lista de nombres obtenida de la BD Guardada a la lista de nombres del tablero
    for m in range(0,len(nombres)):
        jugadores.append(nombres[m])

def insertarColumnas (cantidad):#Sirve para agregar X cantidad de "espacios" agregando un 0 por cada jugador en cada "Vagón" de la lista puntajeParcial
    for t in range (0,cantidad):#Por ejemplo si ponemos 3 en cantidad se va a agregar 1 cero por iteración en los 12 vagones (de 1-6, E,F,P,G,GD y el espacio del resultado final)
        for posiciones in range (0,12):#Estos son los doce "vagones"
            puntajeParcial[posiciones].append('')#acá agrega el valor 0 en el vagón X(cambia según la iteración)AL TERMINAR DE PROGRAMAR TOD HAY QUE CAMBIAR EL 0 por UN espacio vacio

def reanudarColumnas(cantidad,forTablero): # Con los datos obtenidos de la BD crea el tablero
    for c in range (0,cantidad):
        for pos in range(0,11):
            valores = (forTablero[c][pos])
            puntajeParcial[pos].append(valores)
        puntajeParcial[11].append('')

def sumaPuntajeFinal(cantidad,puntajeParcial):# Se debe agregar esta función solo al final, porque si los valores están vacíos no se pueden sumar
    for nume in range(1, cantidad+1):# Debe estar completo el ingreso de los 11 valores por jugador, lo que no tenga completo se debe agregar 0
        resultado = ((puntajeParcial[0][nume])+(puntajeParcial[1][nume])+(puntajeParcial[2][nume])+
                     (puntajeParcial[3][nume])+(puntajeParcial[4][nume])+(puntajeParcial[5][nume])+
                     (puntajeParcial[6][nume])+(puntajeParcial[7][nume])+(puntajeParcial[8][nume])+
                     (puntajeParcial[9][nume])+(puntajeParcial[10][nume]))
        puntajeParcial[11][nume] = (resultado)
    cadenaPuntaje =(" PUNTAJE FINAL ")
    print("\n"+(cadenaPuntaje.center(50,"=")+"\n"))
    mostrarPuntajeParcial()

def anotacion (nroJugador,categoria,puntos):# Esto es para anotar los puntos en el tablero
    if categoria == 1:
        puntajeParcial[0][nroJugador] = puntos
    elif categoria == 2:
        puntajeParcial[1][nroJugador] = puntos
    elif categoria == 3:
        puntajeParcial[2][nroJugador] = puntos
    elif categoria == 4:
        puntajeParcial[3][nroJugador] = puntos
    elif categoria == 5:
        puntajeParcial[4][nroJugador] = puntos
    elif categoria == 6:
        puntajeParcial[5][nroJugador] = puntos
    elif categoria == 'E':
        puntajeParcial[6][nroJugador] = puntos
    elif categoria == 'F':
        puntajeParcial[7][nroJugador] = puntos
    elif categoria == 'P':
        puntajeParcial[8][nroJugador] = puntos
    elif categoria == 'G':
        puntajeParcial[9][nroJugador] = puntos
    elif categoria == 'GD':
        puntajeParcial[10][nroJugador] = puntos

def mostrarPuntajeParcial():#Esto muestra el tablero con los resultados parciales
    print(tabulate(puntajeParcial, jugadores))


def puntajesFinales (jugadores, puntajeParcial): #Devuelve una lista con otras listas dentro que asocia en cada una un nombre de jugador y el puntaje que obtuvo al finalizar el juego.
    puntuacion = (puntajeParcial[11][1:])
    puntuacionDuplicada = puntuacion # Esta lista está duplicada para que, más adelante, no se reemplacen los puntos obtenidos en la lista original.
    nombrePuntos = []
    puntajeOrdenado = (sorted(puntuacion, reverse=True)) # Ordena los puntajes obtenidos de mayor a menor
    for nro in range(0,len(puntajeOrdenado)):
        punto = puntajeOrdenado[nro] # Asocia la variable "punto" a cada puntaje (desde el puntaje maximo al minimo) uno cada vez.
        if punto in puntuacionDuplicada: # Si el valor de "punto" se encuentra en la puntuacionDuplicada realiza las siguientes acciones
            orden = puntuacionDuplicada.index(punto) # Encuentra el número de indice donde está ubicada esa puntuación en la lista puntuacionDuplicada y la asocia a la variable "orden"
            del puntuacionDuplicada[orden] # Usando el numero de indice obtenido en la variable orden lo borra de la lista duplicada.
            puntuacionDuplicada.insert(orden,-1) #Luego lo agrega nuevamente en esa misma ubicación pero reemplazandolo por -1 (para evitar que no capte los numeros por repetición)
            nombrePuntos.insert(orden,[jugadores[orden],punto])# Agrega en la lista "ganadores" en el nro de órden indicado una tupla con el nombre del jugador y el puntaje que obtuvo.
    return nombrePuntos # Devuelve una lista con tuplas dentro que contienen nombre de jugador y puntaje obtenido.


def puestos(puntajeParcial): #devuelve el orden de puestos x puntaje
    puestos = []
    puntos = (puntajeParcial[11][1:])
    puntajeOrdenado = (sorted(puntos, reverse=True)) # Toma los puntos obtenidos y los ordena de mayor a menos
    for nro in puntajeOrdenado:
        if nro not in puestos: # Si no esta en la lista "puestos" (Vacia en un comienzo) agrega a la misma, si ya está lo ignora y no lo suma
            puestos.append(nro) # Lo que hace esta función es ignorar los puntajes repetidos para que haya un numero de puestos correspondientes a la puntuacion (no repetida) obtenida.
    return puestos # Devuelve la cantidad de puestos reales, sin repeticiones


def clasificados(puestos,puntajes): # Recibe cantidad de puestos y puntaje de cada jugador asociado a su nombre. Finalmente imprime el podio de ganadores por orden y detecta los empates.
    cadenasFinales = []
    for elemento in puntajes:
        nombrePuntos = elemento # Recibe cada elemento de la lista, mas abajo los separa en dos variables distintas de nombre y puntos
        nombre = nombrePuntos[0] # variable de nombre con el elemento 0
        puntos = nombrePuntos[1] # variable de puntos con el elemento 1
        if puntos in puestos:
            orden = puestos.index(puntos) # Si los puntos de la variable puntos estan en la lista de puestos devuelve el nro de indice dentro de la variable orden
            texto = ("En "+str(orden+1)+" puesto: "+nombre+" con "+str(puntos)+" puntos.") # Acá arma una cadena de texto con el nro de orden de puesto, el nombre del jugador y los puntos obtenidos.
        cadenasFinales.append(texto) # Agrega la cadena de la variable "texto" a la lista "cadenaFinales"
    resultado = (sorted(cadenasFinales)) # Crea una nueva lista con todas las cadenas finales ordenadas de menor a mayor (Puesto 1, puesto 2,etc) tomando como paramatro de orden el nro de puesto
    for cadena in resultado: # finalmente imprime cada elemento de la lista de resultados
        print(cadena)
