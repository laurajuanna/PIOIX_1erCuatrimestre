import random
import categorias
import tablero
import funcionesbd
import funGenerales

opcionElegida = ""
dados = []
contadorTiradas = 1

# Esta función es la tirada random de X cantidad de dados
# se la invoca para la primer tirada de 5 dados
# también puede volver a invocarse para volver a tirar los 5 dados
# o para tirar nuevamente una cantidad x de dados elegidos
def tirar_dados(dados):
    for i in range(5):
        dados.append(random.randint(1,6))
    return dados

# Ésta función le explica al usuario cómo proceder,
# pide que elija el procedimiento a seguir y devuelve esa elección
def elegirProcedimiento(idPuntaje):
    disponibles = funcionesbd.buscarPuntajeJugador(idPuntaje)
    print("\n--- Usted puede anotarse éstas categorías:\n--> "+disponibles)
    print("\nDesea tirar otra vez? Presione:\n- P para ver los resultados parciales.\n- V para volver a tirar todos los dados."
          "\n- E para elegir qué dados tirar.\n- T para terminar y quedarse con la tirada obtenida.\n")
    procedElegido = input("Por favor, ingrese su elección: ")
    global opcionElegida
    opcionElegida = procedElegido.upper()
    return procedElegido.upper()

# Ésta función vuelve a tirar los 5 dados nuevamente:
# primero le suma 1 al contador de tiradas,
# después imprime qué número de tirada es y avisa que "va a obtener los siguientes dados"
# luego pide que se borren los valores en la lista de dados obtenida anteriormente
# y por ultimo, invoca la tirada random, tira los dados y devuelve la nueva lista de dados obtenidos
def tirarTodoNuevo():
    global contadorTiradas
    contadorTiradas = contadorTiradas + 1
    print("\n*** La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
    dados.clear()
    return tirar_dados(dados)

# Ésta función simplemente imprime y devuelve la lista de dados con las que
# el usuario eligió quedarse tras haber decidido terminar su turno
# o tras haber agotado las 3 tiradas posibles.
def aceptarTirada():
    print("\n*** Turno finalizado. Se ha quedado con los siguientes dados:")
    return dados

# Ésta función HACE DEMASIADAS COSAS y claramente hay que SIMPLIFICARLA
# entre sus muchas funciones hace lo siguiente:
# primero invoca las funciones de categorias y devuelve true si hay alguna categoria especial
# luego analizando el contador de tiradas define si la categoria obtenida es servida o armada
# si obtuvo alguna jugada especial da la opción de elegir quedarse o no con esa categoria especial,
# anotarse puntos de la categoria números o tachar una categoria.
# si el jugador obtiene una categoría que ya tiene anotada lo avisa y da la opcion de anotar numero o tachar
# devuelve el puntaje correspondiente a lo que haya elegido
# si el jugador no obtuvo ninguna jugada especial
# podra elegir anotarse puntos de la categoria numeros o tachar una categoria.
# finalmente RETORNA una TUPLA con los (puntos,categoria) obtenidos
# tambien tiene las validaciones correspondientes en caso de errores de tipeo
def definiciones(dados,idPuntaje):
    categorias.EsGenerala(dados)
    categorias.esEscalera(dados)
    categorias.esFull(dados)
    categorias.EsPoker(dados)
    global contadorTiradas
    global categoria
    global puntos
    if contadorTiradas == 1 and categorias.EsGenerala(dados) == True and funcionesbd.buscarGeneralaIngresada(idPuntaje) == True:
        print("\n*** OBTUVISTE GENERALA SERVIDA! ***")
        print("\n*** Felicitaciones, ganaste el juego! ***")
        print("\nDeseas iniciar una nueva partida?")
        esValido = False
        while esValido == False:
            print("\nPresione:\n- 1 para iniciar una NUEVA PARTIDA.\n- 2 para CERRAR el programa.\n")
            continuar = int(input("Ingrese la opción elegida: "))
            if continuar == 1:
                funGenerales.iniciarPrograma()
                esValido = True
            elif continuar == 2:
                print("\nMuchas gracias por jugar! Vuelva pronto!")
                funGenerales.cerrarPartida()
            else:
                print(">>> ERROR! Ingresaste una opción inválida.")
    elif contadorTiradas == 1 and categorias.esEscalera(dados)==True:
        categoria = "E"
        catIng = funcionesbd.buscarCatIng(idPuntaje,categoria)
        print("Obtuvo una ESCALERA servida: ",dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste la ESCALERA servida Correctamente!")
                puntos = 25
                categoria = "E"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas == 1 and categorias.esFull(dados)==True:
        categoria = "F"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo FULL servido: ", dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste el FULL servido Correctamente!")
                puntos = 35
                categoria = "F"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas == 1 and categorias.EsPoker(dados)==True:
        categoria = "P"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo POKER servido: ", dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste el POKER servido Correctamente!")
                puntos = 45
                categoria = "P"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas > 1 and categorias.EsGenerala(dados)==True:
        categoria = "G"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo GENERALA: ", dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste la GENERALA Correctamente!")
                puntos = 50
                categoria = "G"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas > 1 and categorias.EsGenerala(dados) == True and funcionesbd.buscarGeneralaIngresada(idPuntaje) == 50:
        categoria = "GD" # Si el contadorTiradas es 1 (es servida) la generala es True y la Generala YA FUE OBTENIDA se detecta la GD
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo GENERALA DOBLE: ", dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste la GENERALA DOBLE Correctamente!")
                puntos = 60
                categoria = "GD"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas > 1 and categorias.esEscalera(dados)==True:
        categoria = "E"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo ESCALERA: ", dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste la ESCALERA Correctamente!")
                puntos = 20
                categoria = "E"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas > 1 and categorias.esFull(dados)==True:
        categoria = "F"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo FULL: ",dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste el FULL Correctamente!")
                puntos = 30
                categoria = "F"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    elif contadorTiradas > 1 and categorias.EsPoker(dados)==True:
        categoria = "P"
        catIng = funcionesbd.buscarCatIng(idPuntaje, categoria)
        print("Obtuvo POKER: ",dados)
        if catIng == True:
            siNo = pregunta_QueAnotar()
            siNo = siNo.upper()
            if siNo == "S":
                print("Anotaste el POKER Correctamente!")
                puntos = 40
                categoria = "P"
            elif siNo == "N":
                anotar_NadaEspecial(idPuntaje)
        elif catIng == False:
            print("\n... Usted ya tiene esa categoría anotada!")
            anotar_NadaEspecial(idPuntaje)
    else:
        print("\n*** No obtuvo ninguna jugada especial.")
        anotar_NadaEspecial(idPuntaje)
    tuplaPuntosCategoria = (puntos,categoria)
    return tuplaPuntosCategoria


# Esta funcion se la invoca en la función anterior para anotar
# los puntos correspondientes cuando no se obtiene ninguna categoría especial
# o cuando el jugador decide anotarse numeros o tachar
# categorías a pesar te haber obtenido una categoría especial.
def anotar_NadaEspecial(idPuntaje):
    global categoria
    global puntos
    ref_anotacion = {"N": "n", "T": "t"}
    print("\nPresione:\n- N para anotar un número.\n- T para tachar alguna categoría especial.")
    anotar = input("\nIngrese su elección: ")
    anotar = anotar.upper()
    while anotar not in ref_anotacion:
        print("\n*** ERROR. Ingrese una opción válida.")
        print("\nPresione:\n- N para anotar un número.\n- T para tachar alguna categoría.\n")
        anotar = input("\nIngrese su elección: ")
        anotar = anotar.upper()
    if anotar == "T":
        print("\nEstos son los resultados parciales:\n")
        tablero.mostrarPuntajeParcial()
        opciones=("\nIngrese categoria a tachar. Presione:\n- Números del 1 al 6.\n- E para anotar ESCALERA.\n"
              "- F para anotar FULL.\n- P para anotar POKER.\n- G para anotar GENERALA.\n- GD para anotar GENERALA DOBLE.\n")
        print(opciones)
        ref_tachar = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "E": "E", "e": "E", "F": "F", "f": "F", "P": "P",
                      "p": "P", "G": "G", "g": "G", "GD": "GD", "gd": "GD"}
        categoria = str(input("\nIngrese su elección: "))
        categoria = ref_tachar.get(categoria)
        numIng = False
        catIng = False
        if type(categoria) == int or type(categoria) == str:
            while type(categoria) == int and numIng == False:
                valor = categoria
                numIng = funcionesbd.buscarNumIng(idPuntaje, valor)
                if numIng == True :
                    categoria = valor
                    puntos = 0
                else :
                    print("*** ERROR. La categoría ingresada ya fue obtenida anteriormente.")
                    print(opciones)
                    opcion = str(input("\nIngrese su elección: "))
                    valor = ref_tachar.get(opcion)
                    categoria = valor
            while type(categoria) == str and catIng == False:
                catIng = funcionesbd.buscarCatIng(idPuntaje,categoria)
                if catIng == True :
                    puntos = 0
                else :
                    print("*** ERROR. La categoría ingresada ya fue obtenida anteriormente.")
                    print(opciones)
                    opcion = str(input("\nIngrese su elección: "))
                    categoria = ref_tachar.get(opcion)
        puntos = 0
        print("Tachaste la categoria Correctamente!")
    elif anotar == "N":
        ref_numeros = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}
        valor = (input("\nIngrese el valor del dado que se anotará (Usando números del 1 al 6): "))
        while valor not in ref_numeros:
            print("\n*** ERROR. Esa opción no es correcta. Ingrese números del 1 al 6.\n")
            valor = input("Ingrese el valor del dado que se anotará: ")
        valor = int(valor)
        numIng = funcionesbd.buscarNumIng(idPuntaje, valor)
        if numIng == False:
            while numIng == False:
                print("Usted ya se ha anotado ese número. Intente nuevamente.")
                valor = input("Ingrese el valor del dado que se anotará: ")
                valor = int(valor)
                nroIngresado = funcionesbd.buscarNumIng(idPuntaje, valor)
                numIng = nroIngresado
        puntos = categorias.SalidaDeNumero(dados, valor)
        print("El número fue anotado Correctamente!")
        categoria = valor

# Ésta función pregunta al usuario si desea anotar o no la categoría especial obtenida.
# en el caso de que el usuario se equivoque al escribir hay una validacion dentro del while
# termina RETORNANDO el valor de la elección (siNo) que será tomado en las funciones anteriores
# para tomarlo en las condiciones (IF) y realizar una acción.
def pregunta_QueAnotar():
    ref_SiNo = {"S":"S","s":"S","N":"N","n":"N"}
    print("\nDesea anotar la categoría especial obtenida? Presione:"
          "\n- S para anotar la categoría obtenida."
          "\n- N para anotar dados o tachar categorías.")
    siNo = (input("\nIngrese su elección: "))
    while siNo not in ref_SiNo:
        print("\n*** ERROR. Esa opción no es correcta. Ingrese S o N.")
        siNo = (input("\nIngrese su elección: "))
    return siNo

# Ésta función es para elegir uno o varios dados de una lista de dados previa
# para que luego esa cantidad x de dados sea tirada nuevamente y obtenga un nuevo valor.
# Para eso se invoca a la función random sólo para cambiar los valores de los dados elegidos,
# luego se le suma 1 al contador de tiradas,
# se imprime qué número de tirada es y avisa que "va a obtener los siguientes dados"
# y finalmente devuelve el valor de la nueva tirada con los valores de los 5 dados.
def modificarDados():
    dadosAtirar = input("\nIngrese los dados a cambiar separados por coma (por Nro. De Órden del 1-6): ")
    lista_dados_cambiados = dadosAtirar.split(",")
    esValido = False
    while esValido == False:
        try:
            for i in lista_dados_cambiados:
                dados[(int(i)) - 1] = random.randint(1, 6)
                esValido = True
        except ValueError:
            print("\n*** ERROR!! Lo ingresado no es válido.")
            print("Ingrese el NÚMERO de Órden del dado (Ejemplo: 1) o VARIOS separados por coma (Ejemplo: 1,2,3)")
            dadosAtirar = input("\nIngrese los dados a cambiar separados por comas: ")
            lista_dados_cambiados = dadosAtirar.split(",")
        except IndexError:
            print("\n*** ERROR!! Lo ingresado no es válido.")
            print("Ingrese el NÚMERO de Órden del dado (Ejemplo: 1) o VARIOS separados por coma (Ejemplo: 1,2,3)")
            dadosAtirar = input("\nIngrese los dados a cambiar separados por comas: ")
            lista_dados_cambiados = dadosAtirar.split(",")
    global contadorTiradas
    contadorTiradas = contadorTiradas + 1
    print("\n*** La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
    return dados

# La siguiente función contiene a todas las funciones y opciones principales del programa TIRO
# Después de haber obtenido los dados en cada tirada esta función RECIBE lo ingresado por el usuario
# en la funcion elegirProcedimiento y acata la tarea a realizar invocando a otras funciones.
# esas funciones estan contenidas en la lista diccionario del comienzo (ref_opciones)
# Estan contenidas en ese diccionario para poder realizar la validacion si el usuario
# comete un error al escribir.
# Termina RETORNANDO la lista de dados obtenida al aceptar anotar la tirada invocando
# a la función (definiciones(dados)) para definir qué puntuación anotará el tablero
def programa_principal(idPuntaje):
    ref_opciones = {"T": aceptarTirada, "V": tirarTodoNuevo, "E": modificarDados, "P": '' }
    print("\n*** La tirada número",contadorTiradas,"obtuvo los siguientes dados:\n",tirar_dados(dados))
    while contadorTiradas != 3 and elegirProcedimiento(idPuntaje) != "T":
        if opcionElegida == "P":
            print("\n* Estos son los resultados parciales *\n")
            tablero.mostrarPuntajeParcial()
        elif opcionElegida in ref_opciones and opcionElegida != "P":
            print(ref_opciones[opcionElegida]())
        else:
            print("\n*** ERROR. Esa opción no es correcta. Por favor ingrese una opción válida.")
    return definiciones(dados,idPuntaje)
