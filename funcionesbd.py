from datetime import datetime

import sqlite3

base = sqlite3.connect('puntajes.db')
c = base.cursor()

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
              (None,nombrePartida,laFecha,laHora))
    base.commit()

def ingresoApuntajes (jugadores,nombrePartida):# Ingresa a los jugadores en la tabla PUNTAJES junto a su respectivo ID de partida y jugador
    for t in range(len(jugadores)):
        jugador = (jugadores[t])
        query_part = '''SELECT ID_PARTIDA FROM PARTIDA WHERE PARTIDA.NOMBRE_PARTIDA = "{}" LIMIT 1'''.format(nombrePartida)
        query_jugador = '''SELECT ID_JUGADOR FROM JUGADORES WHERE JUGADORES.NOMBRE_JUGADOR = "{}" LIMIT 1'''.format(jugador)
        idPartida = (ejecutar_query(query_part)[0][0])
        idJugador = (ejecutar_query(query_jugador)[0][0])
        c.execute("INSERT INTO PUNTAJES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (None,idPartida,idJugador,None,None,None,None,None,None,None,None,None,None,None,None))
    base.commit()

def buscarIdPartida(nombrePartida): # Devuelve el ID de la partida a partir del nombre de partida ingresado
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

def buscarIdPuntaje(idPartida,idJugador): # Devuelve el ID de la tabla puntajes segun el ID de partida y jugador(AMBAS DEBEN SER TRUE)
    sentencia = ("SELECT ID_PUNTAJE FROM PUNTAJES WHERE ID_PARTIDA = ? AND ID_JUGADOR = ?;")
    c.execute(sentencia,[idPartida,idJugador])
    busquedaIdPuntaje = c.fetchall()
    idPuntaje = (busquedaIdPuntaje[0][0])
    base.commit()
    return idPuntaje

def buscarGeneralaIngresada(idPuntaje):#Busca si la generala esta ingresada
    sentencia = ('SELECT "G" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
    c.execute(sentencia,[idPuntaje])
    busquedaGeneralaIng = c.fetchall()
    generalaIng = (busquedaGeneralaIng[0][0])
    base.commit()
    if generalaIng == None:
        return False
    elif generalaIng == 0:
        return False
    elif generalaIng == 50:
        return generalaIng

def buscarNumIng(idPuntaje,valor):# Para buscar si un numero ya fue ingresado
    if valor == 1:
        sentencia = ('SELECT "1" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
        c.execute(sentencia,[idPuntaje])
        busqueda = c.fetchall()
        numIng = busqueda[0][0]
        base.commit()
        if numIng == None:
            return True
        else:
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

#def buscaPuntajes(idPuntaje):#Busca puntaje ingresado FALTA PROGRAMAR
 #   sentencia = ('SELECT "4" FROM PUNTAJES WHERE ID_PUNTAJE = ?;')
  #  c.execute(sentencia, [idPuntaje])
   # busqueda = c.fetchall()
    #return busqueda

def buscarCatIng(idPuntaje,categoria): # Para buscar si una cat ya fue ingresada
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


def guardarPuntuacion(categoria,nroTurno,puntos,idPuntaje):#Anota el Nro de turno y Puntos en la tabla PUNTAJES
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

def buscarPartidaGuardada():
    sentencia = ('SELECT * FROM PARTIDA')
    c.execute(sentencia)
    busqueda = c.fetchall()
    print(">>> ÉSTAS SON LAS PARTIDAS GUARDADAS")
    for cant in range(0,len(busqueda)):
        print("")
        print("> Nombre de partida:",(busqueda[cant][1]))
        print("Fecha de inicio de partida:",(busqueda[cant][2]))
        print("Hora de inicio de partida:",(busqueda[cant][3]))
    nombrePartida = input("\nIngrese el NOMBRE DE PARTIDA que desea reanudar: ")
    sentencia2 = ('SELECT ID_PARTIDA FROM PARTIDA WHERE NOMBRE_PARTIDA LIKE ?;')
    c.execute(sentencia2,["%{}%".format(nombrePartida)])
    busqueda = c.fetchall()
    idPartida = (busqueda[0][0])
    return idPartida

def borrarJugadores(idPartida):
    sentencia = ('SELECT ID_JUGADOR FROM PUNTAJES WHERE ID_PARTIDA = ?;')
    c.execute(sentencia,[idPartida])
    busqueda = c.fetchall()
    return busqueda

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
    print("Partida borrada.")

buscarPartidaGuardada()

'''
idPartida = 2
sentencia = ('SELECT * FROM PUNTAJES WHERE ID_PARTIDA = ?;')
c.execute(sentencia,[idPartida])
aca = c.fetchall()
print(type(aca[0]))
print(aca[0])
cantidad = len(aca)
print("el contenido de la tupla es:",len(aca[0]))

for i in range(0,cantidad):
    for m in range(4,15):
        print('Jugador Nro',(i+1),'Puntaje: ',[m],aca[i][m])
        print(type(aca[i][m]))
# -------------- HASTA ACA ES LO DEL SELECT QE PROBE ULTIMO

idPuntaje = 6
valor = 5
numIng = buscarNumIng(idPuntaje,valor)
if numIng == False:
    while numIng == False:
        print("Usted ya se ha anotado ese número. Intente nuevamente.")
        valor = input("Ingrese el valor del dado que se anotará: ")
        numIng = buscarNumIng(idPuntaje, valor)
print("anotado!")'''

def cerrarBase():# Cierra la base de datos
    c.close()
    base.close()
