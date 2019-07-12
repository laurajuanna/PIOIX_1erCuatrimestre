from datetime import datetime
import sqlite3

base = sqlite3.connect('puntajes.db')
c = base.cursor()

# Sirve para ejecutar una consulta a la BD más adelante
def ejecutar_query(query):
   c.execute(query)
   base.commit()
   return c.fetchall()


def guardarJugadores(cantidad,jugadores):# Guarda los jugadores en la BD segun la cantidad indicada y los nombres de la lista jugadores
    for p in range(0,cantidad):
        nombre = jugadores[p]
        c.execute("INSERT INTO JUGADORES VALUES (?, ?)",
                  (None,nombre))
        base.commit()


def fechaActual(): # devuelve la fecha actual.
    dt = datetime.now()    # Fecha y hora actual
    laFecha = ("{}/{}/{}".format(dt.day, dt.month, dt.year))
    return laFecha


def horaActual(): #devuelve la hora actual
    dt = datetime.now()    # Fecha y hora actual
    laHora = ("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    return laHora


def nuevaPartida(nombrePartida):# Guarda el nombre de la partida en la BD junto a la fecha y hora actual
    laFecha = fechaActual()  # devuelve un str
    laHora = horaActual()  # devuelve un str
    c.execute("INSERT INTO PARTIDA VALUES (?, ?, ?, ?)",
              (None,nombrePartida,laFecha,laHora))# Se pone un valor None porque ese campo es autoincremental
    base.commit()


def ingresoApuntajes (jugadores,nombrePartida):# Ingresa a los jugadores en la tabla PUNTAJES junto a su respectivo ID de partida y jugador
    for t in range(len(jugadores)):
        jugador = (jugadores[t])
        query_part = '''SELECT ID_PARTIDA FROM PARTIDA WHERE PARTIDA.NOMBRE_PARTIDA = "{}" LIMIT 1'''.format(nombrePartida)
        query_jugador = '''SELECT ID_JUGADOR FROM JUGADORES WHERE JUGADORES.NOMBRE_JUGADOR = "{}" LIMIT 1'''.format(jugador)
        idPartida = (ejecutar_query(query_part)[0][0])
        idJugador = (ejecutar_query(query_jugador)[0][0])
        c.execute("INSERT INTO PUNTAJES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (None,idPartida,idJugador,None,None,None,None,None,None,None,None,None,None,None,None))#El primer valor None es autoincremental, los otros por default quedan Vacios
    base.commit()


def buscarIdPartida(nombrePartida): # Devuelve el ID de la partida a partir de un nombre de partida ingresado por el usuario
    sentencia = ("SELECT ID_PARTIDA FROM PARTIDA WHERE NOMBRE_PARTIDA = ?;")
    c.execute(sentencia,[nombrePartida])
    busquedaIdPartida = c.fetchall()
    idPartida = (busquedaIdPartida[0][0])
    base.commit()
    return idPartida

def buscarIdJugador(nombreJugador): # Devuelve el ID del jugador segun el nombre del jugador en la lista Jugadores
    sentencia = ("SELECT ID_JUGADOR FROM JUGADORES WHERE NOMBRE_JUGADOR = ?;")
    c.execute(sentencia,[nombreJugador])
    busquedaIdJugador = c.fetchall()
    idJugador = (busquedaIdJugador[0][0])
    base.commit()
    return idJugador


def buscarIdPuntaje(idPartida,idJugador): # Devuelve el ID del puntaje de la tabla puntajes segun el ID de partida y jugador
    sentencia = ("SELECT ID_PUNTAJE FROM PUNTAJES WHERE ID_PARTIDA = ? AND ID_JUGADOR = ?;")
    c.execute(sentencia,[idPartida,idJugador])
    busquedaIdPuntaje = c.fetchall()
    idPuntaje = (busquedaIdPuntaje[0][0])
    base.commit()
    return idPuntaje


def buscarGeneralaIngresada(idPuntaje):# Busca en la BD si la generala esta ingresada
    sentencia = ('SELECT "G" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
    c.execute(sentencia,[idPuntaje])
    busquedaGeneralaIng = c.fetchall()
    generalaIng = (busquedaGeneralaIng[0][0])
    base.commit()
    if generalaIng == None:# Si el campo generala está vacío devuelve True
        return True
    elif generalaIng == 0:# Si el campo tiene 0 (porque fue tachado) devuelve false
        return False
    elif generalaIng == 50:# Si la generala fue ingresada devuelve el puntaje obtenido (Sirve para detectar la GD)
        return generalaIng


def buscarNumIng(idPuntaje,valor):# Para buscar si un numero ya fue ingresado
    if valor == 1: #(Este if es igual a todos los de abajo pero cambian los valores según el numero ingresado)
        sentencia = ('SELECT "1" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia,[idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:# Si el campo está vacío devuelve True
            return True
        else:# Si está lleno devuelve False
            return False
    elif valor == 2:
        sentencia = ('SELECT "2" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia,[idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None :
            return True
        else :
            return False
    elif valor == 3:
        sentencia = ('SELECT "3" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:
            return True
        else:
            return False
    elif valor == 4:
        sentencia = ('SELECT "4" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:
            return True
        else:
            return False
    elif valor == 5:
        sentencia = ('SELECT "5" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:
            return True
        else:
            return False
    elif valor == 6:
        sentencia = ('SELECT "6" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:
            return True
        else:
            return False


def buscarCatIng(idPuntaje,categoria): # Esta función es igual a la anterior pero busca si las categorias especiales fueron ingresadas
    if categoria == 'E':
        sentencia = ('SELECT "E" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        catIng = busqueda[0][0]
        base.commit()
        if catIng == None:
            return True
        else:
            return False
    elif categoria == 'F':
        sentencia = ('SELECT "F" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        catIng = busqueda[0][0]
        base.commit()
        if catIng == None:
            return True
        else:
            return False
    elif categoria == 'P':
        sentencia = ('SELECT "P" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        catIng = busqueda[0][0]
        base.commit()
        if catIng == None:
            return True
        else:
            return False
    elif categoria == 'G':
        sentencia = ('SELECT "G" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        catIng = busqueda[0][0]
        base.commit()
        if catIng == None:
            return True
        else:
            return False
    elif categoria == 'GD':
        sentencia = ('SELECT "GD" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia, [idPuntaje])
        busqueda = c.fetchall()
        catIng = busqueda[0][0]
        base.commit()
        if catIng == None:
            return True
        else:
            return False


# Anota el Nro de turno jugado y los puntos obtenidos en la categoria correspondiente
# dentro de la tabla PUNTAJES. Habiendo obtenido esos datos previamente con otras funciones
def guardarPuntuacion(categoria,nroTurno,puntos,idPuntaje):
    if categoria == 1:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '1' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia,[nroTurno,puntos,idPuntaje])
    elif categoria == 2:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '2' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 3:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '3' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 4:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '4' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 5:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '5' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 6:
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, '6' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 'E':
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, 'E' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 'F':
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, 'F' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 'P':
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, 'P' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 'G':
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, 'G' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    elif categoria == 'GD':
        sentencia = ("UPDATE PUNTAJES SET TURNO = ?, 'GD' = ? WHERE ID_PUNTAJE = ?;")
        c.execute(sentencia, [nroTurno, puntos, idPuntaje])
    base.commit()

def buscarNombrePartida(): # Busca y devuelve todos los nombres de las partidas guardadas en la BD
    sentencia = ('SELECT NOMBRE_PARTIDA FROM PARTIDA;')
    c.execute(sentencia)
    busqueda = c.fetchall()
    return busqueda

def validarPartida(): # Sirve para ingresar un nombre nuevo de partida sin que éste coincida con algun nombre guardado en las partidas guardadas de la BD
    partidas = buscarNombrePartida() # invoca la funcion buscarNombrePartida y recibe la lista de partidas guardadas
    guardadas = []
    for m in partidas: # itera cada elemento y lo pasa a minusculas para evitar que no coincidan con la futura busqueda por errores de tipeo
        elemento = (m[0])
        elemento = elemento.lower()
        guardadas.append(elemento) # despues de pasar a minusculas agrega cada nombre en otra lista llamada "guardadas"
    esValido = False
    while esValido == False:
        ingreso = input("Ingrese nombre de partida: ")
        ingreso = ingreso.lower() # Pasa el nombre ingresado por el usuario a minusculas para que la búsqueda coincida con las de la lista "guardadas"
        if ingreso in guardadas:
            print("*** Error! Ese nombre ya está guardado en el sistema.") # Si encuentra coincidencia devuelve error y regresa al ciclo while
        else:
            ingreso = ingreso.capitalize()# Si el nombre ingresado no coincide con los anteriormente guardados en la BD pasa el ingreso a "tipo título" (Capitalize)
            esValido = True # Corta el ciclo while
    return ingreso # Devuelve el nombre ingresado por el uuario

def buscarPartidaGuardada():#Muestra las partidas guardadas, permite elegir cual reanudar y devuelve el ID_PARTIDA asociado a ella
    sentencia = ('SELECT * FROM PARTIDA')
    c.execute(sentencia)
    busqueda = c.fetchall()
    if not busqueda: # Si no hay nada guardado en la BD devuelve el siguiente error
        print("*** ERROR. No hay ninguna partida guardada hasta el momento.")
        print("Inténtelo nuevamente.\n")
        return False
    else: # Si encuentra algo en la BD devuelve los datos obtenidos de las partidas guardadas
        print(">>> ÉSTAS SON LAS PARTIDAS GUARDADAS")
        for cant in range(0, len(busqueda)):
            print("")
            print("> Nombre de partida:", (busqueda[cant][1]))
            print("Fecha de inicio de partida:", (busqueda[cant][2]))
            print("Hora de inicio de partida:", (busqueda[cant][3]))
        nombrePartida = input("\nIngrese el NOMBRE DE PARTIDA que desea reanudar: ") # Luego pide al usuario que elija cual quiere reanudar
        sentencia2 = ('SELECT ID_PARTIDA FROM PARTIDA WHERE NOMBRE_PARTIDA LIKE ?;') # Segun el nombre de partida dado encuentra el ID_PARTIDA asociado a ella
        c.execute(sentencia2, ["%{}%".format(nombrePartida)]) # Ejecuta la query anterior
        busqueda = c.fetchall() #devuelve el ID_PARTIDA obtenido
        if busqueda:
            idPartida = (busqueda[0][0])
            print("Los datos fueron ingresados Correctamente!")
            print("> Partida",nombrePartida,"reanudada con EXITO!")
            return idPartida # Si lo ingresado fue correcto devuelve el idPartida correspondiente
        elif ValueError: # Si hubo algun error de tipeo va a devolver False
            print("\n*** ERROR. Esa partida no existe. Inténtelo nuevamente.\n")
            resultado = False
            return resultado

# Devuelve una lista con los nombres de los jugadores asociados a una partida según un idPartida obtenido previamente
def buscarJugadoresGuardados(idPartida):
    sentencia = ("SELECT ID_JUGADOR FROM PUNTAJES WHERE ID_PARTIDA = ?;") # Selecciona todos los id_jugador asociados a un id_partida
    c.execute(sentencia,[idPartida])
    busqueda = c.fetchall()
    idAsociado = []
    nombres = []
    for can in range(0,len(busqueda)):
        idAsociado.append(busqueda[can][0]) # Agrega todos los id_jugador asociados a ese id_partida a una lista vacía (idAsociado)
    sentencia2 = ('SELECT NOMBRE_JUGADOR FROM JUGADORES WHERE ID_JUGADOR = ?;')
    for jug in range(0,len(idAsociado)):
        c.execute(sentencia2,[idAsociado[jug]]) # Busca el nombre_jugador asociado al id_jugador obtenido previamente
        jugador = c.fetchall() # obtiene el nombre
        nombres.append(jugador[0][0]) # lo suma a la lista vacía de nombres
    return nombres # retorna la lista de nombres de jugadores asociados al idPartida dado


def buscarPuntajeGuardado(idPartida): # busca todos los puntajes de todos los jugadores asociados a una misma partida según el idPartida dado
    sentencia = ('SELECT "1", "2", "3", "4", "5", "6", "E", "F", "P", "G", "GD" FROM PUNTAJES WHERE ID_PARTIDA = ?;')
    c.execute(sentencia,[idPartida])
    busqueda = c.fetchall()
    return busqueda # devuelve esa lista de puntajes de todos los jugadores asociados a una misma partida


# Busca todos los puntajes asociados a un jugador y devuelve las categorías disponibles para anotar/tachar
def buscarPuntajeJugador(idPuntaje):
    sentencia = ('SELECT "1", "2", "3", "4", "5", "6", "E", "F", "P", "G", "GD" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
    c.execute(sentencia,[idPuntaje])
    busqueda = ((c.fetchall())[0])
    categTotales = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G", "GD"]
    categDisponibles = []
    for m in range(0,len(busqueda)):
        puntos = busqueda[m]
        categoria = categTotales[m]
        if (type(puntos)) != int: # corrobora si lo ingresado NO es un INT (si está vacío el type sera None)
            categDisponibles.append(categoria) # Si es un valor type NONE agrega esa categoría a la lista de categorias disponibles
    disponibles = ""
    for i in categDisponibles:
        disponibles += str(i)+", " # Recorre la lista de categDisponibles y las suma a una variable que
    disponibles = disponibles[:-2] # convertirá esa lista en una variable asociada a una cadena de texto con cada categoría separada por comas
    return disponibles # Finalmente devuelve esa variable con las categorías disponibles


# recibe de parametro una lista de puntos asociados a la partida (busqueda) obtenidos de la bd con la funcion buscarPuntajeGuardado
# luego transforma esa lista de puntajes obtenida de la BD al formato necesario para crear el tablero
def formatoTablero(busqueda):
    forTablero = []
    for m in range(0,len(busqueda)):
        orden = []
        puntaje = busqueda[m]
        for t in range(0,len(puntaje)):
            valores = (puntaje[t])
            if valores == None:
                valores = ''
                orden.append(valores)
            else:
                orden.append(valores)
        forTablero.append(orden)
    return forTablero


def buscarTurnosGuardado(idPartida):# Devuelve los nros de orden de los turnos guardados
    sentencia = ('SELECT TURNO FROM PUNTAJES WHERE ID_PARTIDA = ?;')
    c.execute(sentencia,[idPartida])
    turnos = c.fetchall()
    turnosGuardados = []
    for m in range(0,len(turnos)):
        valor = turnos[m][0]
        if valor == None:
            turnosGuardados.append(0)
        else:
            turnosGuardados.append(valor)
    return turnosGuardados

def siguienteJug(turnosGuardados):# Devuelve qué nro de JUGADOR debe SEGUIR al REANUDAR una partida
    ordenJug = []
    turnoMax = max(turnosGuardados) # asocia a la variable el nro de turno máximo jugado
    for m in range (0,len(turnosGuardados)):
        valor = turnosGuardados[m] # recorre la lista de turnos guardados
        if turnoMax == valor: # compara cada valor de la lista con el nro de turno maximo
            ordenJug.append(0) # si recorre todos los valores y todos son iguales al turno máximó agrega un 0 a la lista ordenJug (porque comenzaría el jugador nro 0)
        elif valor < turnoMax:# si hay algún valor menor al valor del turno máximo agrega el nro de jugador a la lista de ordenJug
            ordenJug.append(m)
            break # luego corta el ciclo porque ya se sabe que debe arrancar el jugador con el valor menor de turno
    siguiente = (max(ordenJug)) # asocia esa variable al maximo porque la lista quedaría por ejemplo [0,0,2] y el máximo es el nro de jugador que le toca jugar
    return siguiente # devuelve el nro de jugador que debe seguir al reanudar la partida

def turnoSiguiente(turnosGuardados):# define y devuelve el nro de TURNO que se jugará al REANUDAR una partida
    maximo = (max(turnosGuardados))
    minimo = (min(turnosGuardados))
    if maximo == 0:# si el máximo es 0 significa que todavia no se jugó ningún turno
        turno = 1 # por lo tanto el nro de turno a jugar será el nro 1
    elif maximo == minimo: # Si todos los turnos son iguales devuelve el nro de turno máximo sumandole 1
        turno = (maximo+1) # ejemplo, si todos jugaron el turno nro 5 se devolverá el nro de turno 6
    else:
        turno = maximo # Si no se arranca x el 1 ni hay "empate" de turnos simplemente se arranca por el número de turno máximo
    return turno # devuelve el nro de turno que se jugará al reanudar la partida


# Esta funcion devuelve el id de los jugadores segun el id de partida asociado a su nombre
# se usará el resultado de ésta función para borrar a esos jugadores de la base de datos al elegir borrar una partida
def borrarJugadores(idPartida):
    sentencia = ('SELECT ID_JUGADOR FROM PUNTAJES WHERE ID_PARTIDA = ?;')
    c.execute(sentencia,[idPartida])
    busqueda = c.fetchall()
    return busqueda

# Esta función sirve para borrar los jugadores, puntajes y partidas asociados a un idPartida
# sólo en el caso de que los jugadores elijan borrar la partida
def borrarPartida(idPartida):
    busqueda = borrarJugadores(idPartida)
    sentencia = ('DELETE FROM PUNTAJES WHERE ID_PARTIDA = ?;')
    sentencia2 = ('DELETE FROM PARTIDA WHERE ID_PARTIDA = ?;')
    c.execute(sentencia,[idPartida])
    c.execute(sentencia2,[idPartida])
    for can in range(0,len(busqueda)):
        borrarId = (busqueda[can][0])
        sentencia2 = ('DELETE FROM JUGADORES WHERE ID_JUGADOR = ?;')
        c.execute(sentencia2,[borrarId])
    base.commit()


def cerrarBase():# Cierra la base de datos
    c.close()
    base.close()
