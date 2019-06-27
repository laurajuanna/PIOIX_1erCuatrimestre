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

def reanudarNombres (nombres):
    for m in range(0,len(nombres)):
        jugadores.append(nombres[m])

def insertarColumnas (cantidad):#Sirve para agregar X cantidad de "espacios" agregando un 0 por cada jugador en cada "Vagón" de la lista puntajeParcial
    for t in range (0,cantidad):#Por ejemplo si ponemos 3 en cantidad se va a agregar 1 cero por iteración en los 12 vagones (de 1-6, E,F,P,G,GD y el espacio del resultado final)
        for posiciones in range (0,12):#Estos son los doce "vagones"
            puntajeParcial[posiciones].append('')#acá agrega el valor 0 en el vagón X(cambia según la iteración)AL TERMINAR DE PROGRAMAR TOD HAY QUE CAMBIAR EL 0 por UN espacio vacio

def reanudarColumnas(cantidad,forTablero):
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

def mostrarGanador (puntajeParcial,cantidad,jugadores):#Muestra que jugador ganó y con cuantos púntos
    listaPuntos = (puntajeParcial[11])
    soloPuntos = (puntajeParcial[11][1:])
    puntajeOrdenado = (sorted(soloPuntos,reverse=True))
    cadenaResultados = (" RESULTADOS FINALES ")
    print("\n" + (cadenaResultados.center(50, "*") + "\n"))
    for i in range(0,len(puntajeOrdenado)):
        ganador = (puntajeOrdenado[i])
        if ganador in listaPuntos:
            ordenGanadores = listaPuntos.index(ganador)
            print("En ", i + 1, "puesto: ", (str(jugadores[ordenGanadores - 1])), "con ", ganador, "puntos")
