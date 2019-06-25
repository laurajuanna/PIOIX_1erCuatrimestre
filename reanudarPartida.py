import tiro
import tablero
import funcionesbd
import sys

def continuarPartida(idPartida):
    print("Desea continuar la partida?")
    print("Ingrese:\n- 1 para continuar la partida."
          "\n- 2 para guardar la partida y continuar más tarde."
          "\n- 3 para abandonar la partida y cerrar el programa.")
    ref_anotacion = {"1": 1, "2": 2, "3": 3}
    opcionContinuar = input("\nIngrese la opción deseada: ")
    while opcionContinuar not in ref_anotacion:
        print("\nERROR. Lo ingresado no fue recibido correctamente. Por favor, ingrese una opción válida.")
        opcionContinuar = input("\nPor favor, ingrese la opción deseada: ")
    opcionContinuar = int(opcionContinuar)
    if opcionContinuar == 2:
        funcionesbd.cerrarBase()
        print("La partida ha sido guardada CORRECTAMENTE!")
        print("Muchas gracias por jugar! Vuelva pronto!")
        sys.exit()
    elif opcionContinuar == 3:
        funcionesbd.borrarPartida(idPartida)
        print("Muchas gracias por jugar! Vuelva pronto!")
        sys.exit()
    elif opcionContinuar == 1:
        return True


def nuevaPartida():
    jugadores = tablero.jugadores  # asigna la variable jugadores a la lista jugadores tablero.py
    puntajeParcial = tablero.puntajeParcial  # asigna la variable puntajeParcial a la lista puntajeParcial de tablero.py
    cantidad = tablero.ingresoCantidadJug()  # llama a la función para preguntar y guarda el valor de la cantidad de jugadores
    tablero.ingresoNombres(
        cantidad)  # llama a la funcion para agregar los nomgres a la lista de jugadores y sumarlos al tablero
    tablero.insertarColumnas(cantidad)  # suma espacios vacios a la lista del tablero segun la cantidad de jugadores
    nombrePartida = input("Ingrese el nombre de la partida: ")
    funcionesbd.guardarJugadores(cantidad, jugadores)  # Guarda los datos en la base de datos
    funcionesbd.nuevaPartida(nombrePartida)  #
    funcionesbd.ingresoApuntajes(jugadores, nombrePartida)
    idPartida = funcionesbd.buscarIdPartida(nombrePartida)
    print('\nLos datos fueron ingresados Correctamente! -'
          ' La partida fue guardada con el Nombre: "', nombrePartida, '" bajo el Nro de ID: ', idPartida)
    for turno in range(0,2):
        nroTurno = (turno + 1)
        print("\n* Turno número", str(turno + 1) + " *\n")
        for a in range(0, cantidad):
            nombreJugador = (jugadores[a])
            idJugador = funcionesbd.buscarIdJugador(nombreJugador)
            idPuntaje = funcionesbd.buscarIdPuntaje(idPartida, idJugador)
            print(">>> Debe tirar el jugador Número", (a + 1), ":", (jugadores[a]), "<<<")
            desglosar = tiro.programa_principal(idPuntaje)
            puntos = desglosar[0]  # recibe el elemento 1 guardado en la tupla que equivale a los puntos obtenidos
            categoria = desglosar[1]  # lo mismo que la anterior, recibe la categoria obtenida
            tablero.anotacion(a+1,categoria,puntos)
            funcionesbd.guardarPuntuacion(categoria, nroTurno, puntos, idPuntaje)
            tiro.dados.clear() # luego de anotar borra los datos de la lista de dados para que el prox jugador arranque de cero
            tiro.contadorTiradas =1  # regresa el valor del contador de tiradas a 1 para que el prox jugador arranque de cero
            print("")
            continuar = continuarPartida(idPartida)
            if continuar == True:
                pass
            print("")
        print("* Resultados Finales del Turno Nro",(turno+1),"*\n")  # Imprime los resultados parciales al finalizar el turno
        tablero.mostrarPuntajeParcial()
    tablero.sumaPuntajeFinal(cantidad,puntajeParcial)
    tablero.mostrarGanador(puntajeParcial, cantidad, jugadores)
    funcionesbd.cerrarBase()

#def reanudarPartida():

def iniciarPrograma():
    print("*BIENVENIDO A LA GENERALA.*")
    print("Desea iniciar una partida nueva?\nIngrese:\n- 1 para iniciar una nueva partida.\n- 2 para reanudar una partida guardada.")
    ref_anotacion = {"1": 1, "2": 2}
    opcionPartida = input("\nIngrese la opción deseada: ")
    while opcionPartida not in ref_anotacion:
        print("\nERROR. Lo ingresado no fue recibido correctamente.\nPor favor, ingrese una opción válida usando NÚMEROS.")
        print("- 1 para iniciar una nueva partida.\n- 2 para reanudar una partida guardada.")
        opcionPartida = input("\nPor favor, ingrese la opción deseada: ")
    opcionPartida = int(opcionPartida)
    if opcionPartida == 1:
        print("\nUsted a iniciado una NUEVA PARTIDA.\n")
        nuevaPartida()
    elif opcionPartida == 2:
        print("\nUsted a REANUDADO una partida.\n")
        #reanudarPartida()
        return opcionPartida

iniciarPrograma()
