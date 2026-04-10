#Ejercicio 4 - Escape Room - la Bóveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contadorCerradura = 0
bandera = 0

nombreAgente = input("Ingrese el nombre del agente seleccionado: ")

while nombreAgente.isalpha() and tiempo > 3:
    opcionMenu = input("Ingrese el número para indicar la opción deseada del menú: 1. Forzar cerradura, 2.Hackear panel, 3.Descansar.")
    if cerraduras_abiertas != 3:
        while opcionMenu.isdigit() and alarma != True or bandera == 0:
            if energia > 0 or tiempo > 0 or cerraduras_abiertas < 3:
                
                if opcionMenu  == "1":
                    print("Forzar cerradura")
                    contadorCerradura += 1;
                    print(contadorCerradura)
                    if contadorCerradura == 3:
                        print("Has intentado más de 3 veces, la cerradura se ha bloqueado. Fin del juego.")
                        alarma = True
                        tiempo = 0
                        break
                    elif energia > 40:
                        print("Cerradura forzada")
                        energia -= 20
                        tiempo -= 2
                        cerraduras_abiertas += 1
                        #bandera = 1
                        break
                    elif energia < 40:
                        print("Existe riesgo de la alarma")
                        validarEnergia = input("Ingrese un número del 1 al 3")
                        print(validarEnergia)
                        
                        if validarEnergia.isdigit() and validarEnergia == "3":
                            alarma = True
                            nombreAgente = ""
                            print("Alarma activada, cerradura bloqueada. Fin del juego")
                            break
                
                elif opcionMenu  == "2":
                    print("Hackear panel")
                    x = 0
                    energia -= 10
                    tiempo -= 3
                    for x in range(4):
                        print(f"El codigo parcial es: {codigo_parcial}")
                        codigo_parcial += "A"
                        print(f"El codigo parcial actual es: {codigo_parcial}")
                        bandera = 1
                    if len(codigo_parcial) == 8 and cerraduras_abiertas <= 2:
                        print("Has abierto una cerradura")
                        cerraduras_abiertas += 1
                    break
                elif opcionMenu  == "3":
                    print("Descansar")
                    if energia <= 85 and alarma == False:
                        print("Felicidades has regenerado +15 de energia y te restamos -1 tiempo")
                        tiempo -=1
                        energia += 15
                        break
                    elif energia <= 85 and alarma == True:
                        print("Felicidades has regenerado +10 de energía y te restamos -1 tiempo")
                        tiempo -=1
                        energia += 10
                        break
                    else:
                        print("Tienes demasiada energía, no puedes descansar en este momento intenta más tarde")
                        break
                break
            else:
                alarma = True
                nombreAgente = ""
                print("Fin del juego.")
    elif cerraduras_abiertas == 3:
            print("Has ganado el juego.")
            tiempo = 0


