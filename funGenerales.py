import tiro
import tablero
import funcionesbd
import sys

def cerrarPartida(): # Cierra el programa. Se invoca sólo si al ganar con generala servida se elige la opcion salir.
    sys.exit()

# Esta es la versión extendida que pregunta si se desea continuar la partida
# Se puede Continuar la partida, Guardar y salir o Borrar la partida y salir.
# Tdo con sus respectivas validaciones y confirmaciones (en el caso de borrar la partida)
def continuarPartida(idPartida):
    print("Ingrese:\n- 1 para CONTINUAR la partida."
          "\n- 2 para GUARDAR la partida y SALIR."
          "\n- 3 para BORRAR la partida y SALIR.")
    ref_anotacion = {"1": 1, "2": 2, "3": 3}
    opcionContinuar = input("\nIngrese la opción deseada: ")
    while opcionContinuar not in ref_anotacion: # esta es la validacion para un ingreso erróneo
        print("\n*** ERROR! Lo ingresado no fue recibido correctamente. Por favor, ingrese una opción válida.")
        opcionContinuar = input("\nPor favor, ingrese la opción deseada: ")
    opcionContinuar = int(opcionContinuar)
    if opcionContinuar == 2: # Cierra la Base de Datos, cierra el juego y sale del programa
        funcionesbd.cerrarBase()
        print("La partida ha sido guardada CORRECTAMENTE!")
        print("Muchas gracias por jugar! Vuelva pronto!")
        sys.exit()
    elif opcionContinuar == 3: # pide la confirmacion para borrar la partida que ha jugado
        ref_borrar = {"1": "1", "2": "2"}
        print("\nPor favor, confirme su eleccion.")
        borrar = input("Presione -> 1 para BORRAR y SALIR\nPresione -> 2 para VOLVER ATRÁS: ")
        while borrar not in ref_borrar: # validacion para un ingreso erróneo
            print("\n*** ERROR! Lo ingresado no fue recibido correctamente. Por favor, ingrese una opción válida.")
            borrar = input("\nPresione -> 1 para BORRAR y SALIR\nPresione -> 2 para VOLVER ATRÁS: ")
        if borrar == "1": # borra la partida y sale del programa
            funcionesbd.borrarPartida(idPartida)
            print("Muchas gracias por jugar! Vuelva pronto!")
            sys.exit()
        elif borrar == "2": # vuelve a preguntar si desea continuar la partida
            preguntaCorta(idPartida)
    elif opcionContinuar == 1:
        return True

# Función para continuar la partida en forma "ágil" presionando ENTER.
def preguntaCorta(idPartida):
    print("Presione -> ENTER para CONTINUAR la partida.")
    opcion = input("Presione -> 1 para GUARDAR y SALIR: ")
    if opcion == "1": # esta opción lleva a otra función que amplía las opciones a guardar y salir, o borrar y salir.
        print("")
        continuarPartida(idPartida)
    else: # esta opcion hace que la partida continúe
        print("")
        return True


# Esta es la función principal para iniciar una partida nueva
def nuevaPartida():
    jugadores = tablero.jugadores  # asigna la variable jugadores a la lista jugadores tablero.py
    puntajeParcial = tablero.puntajeParcial  # asigna la variable puntajeParcial a la lista puntajeParcial de tablero.py
    cantidad = tablero.ingresoCantidadJug()  # llama a la función para preguntar y guarda el valor de la cantidad de jugadores
    tablero.ingresoNombres(cantidad)  # llama a la funcion para agregar los nombres a la lista de jugadores y sumarlos al tablero
    tablero.insertarColumnas(cantidad)  # suma espacios vacios a la lista del tablero segun la cantidad de jugadores
    nombrePartida = input("Ingrese el nombre de la partida: ")
    funcionesbd.guardarJugadores(cantidad, jugadores)  # Inserta nombres en la tabla Jugadores de la BASE DE DATOS
    funcionesbd.nuevaPartida(nombrePartida)  # Inserta el nombre de partida, fecha y hora en la tabla Partida de la BD
    funcionesbd.ingresoApuntajes(jugadores, nombrePartida) # Inserta los anteriores datos en la tabla Puntajes de la BD
    idPartida = funcionesbd.buscarIdPartida(nombrePartida) # Busca el ID_PARTIDA asociado a la nueva partida en la BD
    print('\n> Los datos fueron ingresados Correctamente!\n>La partida fue guardada con el Nombre>',nombrePartida)
    for turno in range(0,12): # Crea un ciclo de 11 Turnos
        nroTurno = (turno + 1) # Variable asociada al nro de turno que se jugará
        print("\n------------------------ * TURNO NÚMERO ",str(turno+1), " * ------------------------\n")
        for a in range(0, cantidad): # Crea un ciclo que se repetirá según la cantidad de jugadores
            nombreJugador = (jugadores[a]) # Variable asociada al nombre del jugador que jugará
            idJugador = funcionesbd.buscarIdJugador(nombreJugador) # Devuelve el ID_JUGADOR asociado al jugador en la BD
            idPuntaje = funcionesbd.buscarIdPuntaje(idPartida, idJugador) # Devuelve el ID_PUNTAJE asociado al jugador en la BD
            print("------------>>> Debe tirar el jugador Número", (a + 1), ":", (jugadores[a]), "<<<------------")
            desglosar = tiro.programa_principal(idPuntaje) # Realiza la tirada y devuelve una tupla con los puntos y la categoria obtenidos
            puntos = desglosar[0]  # recibe el elemento 1 guardado en la tupla que equivale a los puntos obtenidos
            categoria = desglosar[1]  # recibe el elemento 2 de la tupla que equivale a la categoria obtenida
            tablero.anotacion(a+1,categoria,puntos) # anota los puntos en el tablero del python
            funcionesbd.guardarPuntuacion(categoria, nroTurno, puntos, idPuntaje) # guarda tdo lo obtenido x el jugador en la BD
            tiro.dados.clear() # luego de anotar borra los datos de la lista de dados para que el prox jugador arranque de cero
            tiro.contadorTiradas =1  # regresa el valor del contador de tiradas a 1 para que el prox jugador arranque de cero
            print("")
            continuar = preguntaCorta(idPartida) # Pregunta si desea continuar la partida o guardar y salir.
            if continuar == True:
                pass
        print("") # Se sale del ciclo de jugadores
        print("* Resultados Finales del Turno Nro",(turno+1),"*\n")
        tablero.mostrarPuntajeParcial() # al finalizar el turno muestra el tablero con los puntajes parciales
    tablero.sumaPuntajeFinal(cantidad,puntajeParcial) # al finalizar los 11 turnos suma todos los puntos obtenidos
    cadenaResultados = (" RESULTADOS FINALES ")
    print("\n" + (cadenaResultados.center(50, "*") + "\n"))
    puestos = tablero.puestos(tablero.puntajeParcial)
    puntajes = tablero.ganador(jugadores, tablero.puntajeParcial)
    tablero.clasificados(puestos, puntajes)
    print("\n Partida finalizada. Muchas gracias por jugar!")
    funcionesbd.cerrarBase()# Cierra la BD


# Esta función reanuda una partida guardada
def ejecutarReanudar(idPartida):
    nombres = funcionesbd.buscarJugadoresGuardados(idPartida) # busca en la BD los nombres de jugadores asoc al ID_PARTIDA y los guarda en la variable.
    tablero.reanudarNombres(nombres) # agrega esos nombres a la lista de nombres del tablero
    jugadores = tablero.jugadores # devuelve esa lista
    cantidad = len(jugadores) # guarda la cantidad de jugadores asociados a la partida
    busqueda = funcionesbd.buscarPuntajeGuardado(idPartida) # busca en la bd los puntajes asociados al ID_PARTIDA
    forTablero = funcionesbd.formatoTablero(busqueda) # transforma esa lista de puntos al formato necesario para crear el tablero
    tablero.reanudarColumnas(cantidad,forTablero) # crea el tablero
    print("\n------------ * ESTOS SON LOS RESULTADOS PARCIALES * ------------\n")
    tablero.mostrarPuntajeParcial() # Muestra el tablero de resultados parciales guardados
    listaTurnos = funcionesbd.buscarTurnosGuardado(idPartida) # define los nros de turnos guardados
    siguienteJug = funcionesbd.siguienteJug(listaTurnos) # define cuál es el jugador que debe continuar jugando
    siguienteTurno = funcionesbd.turnoSiguiente(listaTurnos) # define que nro de turno sigue a continuacion
    for turno in range (siguienteTurno,12): # Crea un ciclo que comienza con el nro de turno siguiente al guardado y termina en 11
        nroTurno = (turno) # Tdo lo que sigue a continuacion es igual a la funcion de nueva partida
        print("\n------------------------ * TURNO NÚMERO ", str(turno)," * ------------------------\n")
        for a in range(siguienteJug,cantidad): # Excepto este ciclo, que comienza con el nro de jugador siguiente al guardado
            nombreJugador = (jugadores[a])
            idJugador = funcionesbd.buscarIdJugador(nombreJugador)
            idPuntaje = funcionesbd.buscarIdPuntaje(idPartida,idJugador)
            print("------------>>> Debe tirar el jugador Número", (a + 1), ":", (jugadores[a]), "<<<------------")
            desglosar = tiro.programa_principal(idPuntaje)
            puntos = desglosar[0]
            categoria = desglosar[1]
            tablero.anotacion(a+1,categoria,puntos)
            funcionesbd.guardarPuntuacion(categoria,nroTurno,puntos,idPuntaje)
            tiro.dados.clear()
            tiro.contadorTiradas = 1
            print("")
            continuar = preguntaCorta(idPartida)
            if continuar == True:
                pass
        siguienteJug = 0 # Cambia el rango del ciclo de nro de jugadores a cero para que arranque desde el 1er jugador
        print("")
        print("------------ * Resultados Finales del Turno Nro", (turno), "* ------------\n")
        tablero.mostrarPuntajeParcial()
    tablero.sumaPuntajeFinal(cantidad,tablero.puntajeParcial)
    cadenaResultados = (" RESULTADOS FINALES ")
    print("\n" + (cadenaResultados.center(50, "*") + "\n"))
    puestos = tablero.puestos(tablero.puntajeParcial)
    puntajes = tablero.ganador(jugadores, tablero.puntajeParcial)
    tablero.clasificados(puestos,puntajes)
    print("\n Partida finalizada. Muchas gracias por jugar!")
    funcionesbd.cerrarBase()


def reanudarPartida(): #Muestra las partidas guardadas y permite elegir cual reanudar
    resultado = funcionesbd.buscarPartidaGuardada()
    if resultado == False: # Si no hay ninguna guardada devuelve ERROR y comienza el programa otra vez
        iniciarPrograma()
    else: # Si eligio correctamente una partida asociara el idPartida a ella y la reanudara exitosamente
        idPartida = resultado
        ejecutarReanudar(idPartida)


# Esta es la fun principal que llama a tdo el programa
def iniciarPrograma():
    print(">>> BIENVENIDO A LA GENERALA! <<<")
    print("Desea iniciar una partida nueva?\nIngrese:\n- 1 para iniciar una NUEVA partida.\n- 2 para REANUDAR una partida guardada.")
    print("- 3 para CERRAR el programa.")
    ref_anotacion = {"1": 1, "2": 2, "3": 3}
    opcionPartida = input("\nIngrese la opción deseada: ")
    while opcionPartida not in ref_anotacion: # Esta es la validacion para un ingreso erróneo
        print("\n*** ERROR! Lo ingresado no fue recibido correctamente.\nPor favor, ingrese una opción válida usando NÚMEROS.")
        print("- 1 para iniciar una nueva partida.\n- 2 para reanudar una partida guardada.")
        opcionPartida = input("\nPor favor, ingrese la opción deseada: ")
    opcionPartida = int(opcionPartida)
    if opcionPartida == 1: # Acá invoca a la funcion de iniciar una partida nueva
        print("\nUsted a iniciado una NUEVA PARTIDA.\n")
        nuevaPartida()
    elif opcionPartida == 2: # Acá invoca a la función de reanudar una partida guardada
        print("")
        reanudarPartida()
    elif opcionPartida == 3: # Esta opción te hace cerrar el programa y salir del juego
        print("Muchas gracias por jugar! Vuelva Pronto!")
        sys.exit()
