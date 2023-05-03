#Grupo: Estefany Clara, Gonzalo Paz y Juan Pérez

"""2 jugadores, juan tira 2 dados, si sale algun 4 el tiene la opción de de elegir entre tirar de nuevo o quedarse con el puntaje obtenido hasta el momento, dicho puntaje solo equivale al dado distinto de 4.

Estrategia de Juan
si Juan obtiene 0 puntos en la primera tirada, tira de nuevo y ese es su puntaje
si juan obtiene x puntos con 1<=x<=6
	si x => 4 juan no tira de nuevo.
	si x = 3 juan tira de nuevo el dado distinto de 4
1- hallar la probabilidad de que juan saque k puntos.
2- cual es la prob. de que juan tenga 0 puntos en el primer lanzamiento, sabiendo que juan obtuvo 5 puntos en el juego?  (probabilidad condicional)"""

import msvcrt
import random

def tirar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    return dado1, dado2

def tirar_dado():
    dado = random.randint(1,6)
    return dado
    
jugador1 = "Juan"
jugador2 = "María"
victorias_j1 = 0
victorias_j2 = 0
empates = 0
tabla = "\t {} \t\t|\t {}\n".format(jugador1, jugador2)
tabla += "Dado 1  Dado 2  Puntaje |Dado 1  Dado 2  Puntaje |Ganador\n"
jugadas = ""
contador = 0

def jugar():
    global tabla
    global contador
    global jugadas
    jugada = ""
    resumen = ""
    
    puntos_j1 = 0
    #juega el jugador1

    dado1, dado2 = tirar_dados()
    jugada += "Juan tiro los dados y salio: {} {}\n".format(dado1, dado2)
    if dado1 != 4 and dado2 != 4:
        dado1, dado2 = tirar_dados()
        jugada += "Juan tiro los dados y salio: {} {}\n".format(dado1, dado2)
        if dado1 == 4 and dado2 == 4:
            puntos_j1 += 4  
            resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
        elif dado1 == 4 and dado2 != 4:
            puntos_j1 += dado2
            resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
        elif dado1 != 4 and dado2 == 4:
            puntos_j1 += dado1
            resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
        else:
            resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    elif dado1 == 4 and dado2 >= 4:
        puntos_j1 += dado2
        resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    elif dado1 >= 4 and dado2 == 4:
        puntos_j1 += dado1
        resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    elif dado1 == 4 and dado2 < 4:
        dado2 = tirar_dado()
        jugada += "Juan tiro el dado y salio: {}\n".format(dado2)
        puntos_j1 += dado2
        resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    elif dado1 < 4 and dado2 == 4:
        dado1 = tirar_dado()
        jugada += "Juan tiro el dado y salio: {}\n".format(dado1)
        puntos_j1 += dado1
        resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    else:
        resumen += "{}\t{}\t{}\t|".format(dado1, dado2, puntos_j1)
    jugada += "Juan obtuvo: {} puntos\n".format(puntos_j1)
    
    #juega el jugador2
    puntos_j2 = 0
    dado1, dado2 = tirar_dados()
    jugada += "María tiro los dados y salio: {} {}\n".format(dado1, dado2)
    if dado1 != 4 and dado2 != 4:
        #tira de nuevo
        dado1, dado2 = tirar_dados()
        jugada += "María tiro los dados y salio: {} {}\n".format(dado1, dado2)
        if dado1 == 4 and dado2 == 4:
            puntos_j2 += 4   
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado1 == 4 and dado2 != 4:
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado1 != 4 and dado2 == 4:
            puntos_j2 += dado1
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        else:
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
    elif dado1 == 4 and dado2 != 4:
        if dado2 > puntos_j1:
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado2 == puntos_j1 and dado2 <= 3:
            dado2 = tirar_dado()
            jugada += "María tiro el dado y salio: {}\n".format(dado2)
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado2 == puntos_j1 and dado2 > 3:
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        else:
            dado2 = tirar_dado()
            jugada += "María tiro el dado y salio: {}\n".format(dado2)
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
    elif dado1 != 4 and dado2 == 4:
        if dado1 > puntos_j1:
            puntos_j2 += dado1
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado1 == puntos_j1 and dado1 <= 3:
            dado1 = tirar_dado()
            jugada += "María tiro el dado y salio: {}\n".format(dado1)
            puntos_j2 += dado1
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif dado1 == puntos_j1 and dado1 > 3:
            puntos_j2 += dado1
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        else:
            dado1 = tirar_dado()
            jugada += "María tiro el dado y salio: {}\n".format(dado1)
            puntos_j2 += dado1
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
    elif dado1 == 4 and dado2 == 4:
        if puntos_j1 < 4:
            puntos_j2 += 4
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
        elif puntos_j1 >= 4:
            dado2 = tirar_dado()
            jugada += "María tiro el dado y salio: {}\n".format(dado2)
            puntos_j2 += dado2
            resumen += "{}\t {}\t {}\t |".format(dado1, dado2, puntos_j2)
    jugada += "María obtuvo: {} puntos\n".format(puntos_j2)
    
    #comparar puntajes
    if puntos_j1 > puntos_j2:
        jugada += "Juan gana la ronda\n\n"
        global victorias_j1
        victorias_j1 += 1
        resumen += "{}\n".format(jugador1)
    elif puntos_j1 < puntos_j2:
        jugada += "María gana la ronda\n\n"
        global victorias_j2
        victorias_j2 += 1
        resumen += "{}\n".format(jugador2)
    else:
        jugada += "El resultado es Empate\n\n"
        #print("Empate")
        global empates
        empates += 1
        resumen += "Empate\n"
    
    while contador < 10:
        jugadas += jugada
        tabla += resumen
        break    
    contador += 1

"""La función mostrar_jugadas() recibe un parametro booleano que indica si se debe mostrar o no las jugadas realizadas"""
def mostrar_jugadas(mostrar):

    if mostrar == "S":
        print("-----------------------------------------------------------------------")
        print("Resumen de las jugadas")
        print(jugadas)
        print("-----------------------------------------------------------------------")
    elif mostrar == "N":
        print("")
    else:
        print("Opción incorrecta. POR FAVOR INTENTE DE NUEVO")
        ver_jug = input("Desea mostrar las jugadas realizadas? (S/N): ").upper()
        mostrar_jugadas(ver_jug)

"""La función mostrar_resumen() recibe un parametro booleano que indica si se debe mostrar o no el resumen de las jugadas realizadas"""
def mostrar_resumen(mostrar):
    if mostrar == "S":
        print("-----------------------------------------------------------------------")
        print("Tabla de resultados de las jugadas")
        print(tabla)
        print("-----------------------------------------------------------------------")
    elif mostrar == "N":
        print("")
    else:
        print("Opción incorrecta. POR FAVOR INTENTE DE NUEVO")
        ver_tab = input("Desea mostrar la tabla de resumen de las jugadas realizadas? (S/N): ").upper()
        mostrar_resumen(ver_tab)

def main(veces):
    print("-----------------------------------------------------------------------")
    print("Comienza el juego")
    for i in range(veces):
        jugar()
    print(jugador1," tiene: ", victorias_j1, "victorias")
    print(jugador2," tiene: ", victorias_j2, "victorias")
    print("Hay ", empates, "empates")
    print("-----------------------------------------------------------------------")
    """El sistema indica si se desea mostrar las jugadas realizadas"""
    ver_jug = input("Desea mostrar 10 de las jugadas realizadas? (S/N): ").upper()
    mostrar_jugadas(ver_jug)
    """El sistema indica si se desea mostrar el resumen de las jugadas realizadas"""
    ver_tab= input("Desea mostrar la tabla de resumen con 10 jugadas realizadas? (S/N): ").upper()
    mostrar_resumen(ver_tab)
    print("-----------------------------------------------------------------------")
    print("{}\t |{}\t | Empates".format(jugador1, jugador2))
    print("{}\t |{}\t | {}".format(victorias_j1, victorias_j2, empates))
    print("{}%\t |{}%\t | {}%".format(round((victorias_j1*100/veces),1), round((victorias_j2*100/veces),1), round((empates*100/veces),1)))
    print("-----------------------------------------------------------------------")
    print("Fin del juego")
    print("Presione cualquier tecla para salir")
    while True:
        if msvcrt.kbhit():
            break

def main_auto(veces):
    print("-----------------------------------------------------------------------")
    print("Se realizaran {:,.0f} tiradas".format(veces).replace(",", "@").replace(".", ",").replace("@", "."))
    for i in range(veces):
        jugar()
    print(jugador1," tiene: ", victorias_j1, "victorias")
    print(jugador2," tiene: ", victorias_j2, "victorias")
    print("Hay ", empates, "empates")
    print("-----------------------------------------------------------------------")
    print("{}\t |{}\t | Empates".format(jugador1, jugador2))
    print("{}\t |{}\t | {}".format(victorias_j1, victorias_j2, empates))
    print("{}%\t |{}%\t | {}%".format(round((victorias_j1*100/veces),1), round((victorias_j2*100/veces),1), round((empates*100/veces),1)))
    print("-----------------------------------------------------------------------")

def tiradas():
    try :
        veces = int(input("Ingrese la cantidad de veces que desea jugar: "))
    except ValueError:
        print("Por favor ingrese un número entero")
        veces = tiradas()
    return veces

def tipo_juegos():
    try :
        tipo_juego = input("Ingrese el tipo de juego: Manual (M) o Automático (A): ").upper()
        if tipo_juego == "M" or tipo_juego == "A":
            pass
        else:
            print("Por favor ingrese un caracter correcto (M o A)")
            tipo_juego = tipo_juegos()
    except ValueError:
        print("Por favor ingrese un caracter correcto (M o A)")
        tipo_juego = tipo_juegos()
    return tipo_juego
       
modo = tipo_juegos()
if modo == "M":
    veces = tiradas()
    main(veces)
elif modo == "A":
    main_auto(1000)
    main_auto(10000)
    main_auto(100000)
    print("Fin de la simulación de 1000, 10000 y 100000 tiradas")
    print("Presione cualquier tecla para salir")
    while True:
        if msvcrt.kbhit():
            break
