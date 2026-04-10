# Ejercicio 5 - La arena del Gladiador

vidaGladiador = 100
vidaOponente = 100
pocionesCura = 3
ataquePesado = 15
turnoGladiador = True
banderaInicio = 0
banderaJuego = 0

while banderaInicio == 0:
    nombreGladiador = input("Ingresa el nombre tuyo Gladiador: ")

    while nombreGladiador.isalpha() and banderaJuego == 0:
            if vidaGladiador > 0 and vidaOponente > 0:
                #print("Ejecuto el juego")
                if turnoGladiador:
                    opcionMenu = input(f"Tienes {vidaGladiador} puntos de vida, tu oponente tiene {vidaOponente} puntos de vida y cuentan con {pocionesCura} pociones para curarse. Pelea eligiendo las siguientes opciones e ingresando el número: 1. Ataque pesado, 2. Ráfaga Veloz, 3. Curar ")
                    while opcionMenu.isdigit():
                        if opcionMenu == "1":
                            if vidaOponente > 20:
                                vidaOponente = vidaOponente - ataquePesado
                                print(f"¡Atacaste al enemigo por {ataquePesado} puntos de daño!")
                                turnoGladiador = False
                                break
                            else:
                                golpeCritico = ataquePesado * 1.5
                                vidaOponente = vidaOponente - golpeCritico
                                print(f"¡Atacaste al enemigo por {golpeCritico} puntos de daño!")
                                turnoGladiador = False
                                break
                        elif opcionMenu == "2":
                            print("Ráfaga Veloz")
                            for i in range (3):
                                vidaOponente -= 5
                                print("¡Golpe conectado por 5 de daño!")
                                turnoGladiador = False
                            break
                        elif opcionMenu == "3":
                            print("Cura")
                            if pocionesCura > 0:
                                vidaGladiador += 30
                                pocionesCura -= 1
                                print("¡Te curaste 30 puntos de vida!")
                                break
                            else:
                                print("¡No te quedan pociones!")
                                turnoGladiador = False
                            break
                    #banderaJuego += 1
                    #banderaInicio += 1
                else:
                    vidaGladiador -= 12
                    turnoGladiador = True
                    print("¡El enemigo te atacó por 12 puntos de daño!")
            elif vidaOponente <= 0:
                print("¡Has ganado el juego!")
                banderaJuego += 1
                banderaInicio += 1
            elif vidaGladiador <= 0:
                print("¡Has perdido!")
                banderaJuego += 1
                banderaInicio += 1

    if nombreGladiador.isalpha() == False:
        print("Error solo se permiten letras, vuelve a intentar")
        

