#"Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”"
#Contexto
#Hay 2 días de atención: Lunes y Martes.
#Cada día tiene cupos fijos:
#• Lunes: 4 turnos
#• Martes: 3 turnos
#Reglas
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#1. Reservar turno
#2. Cancelar turno (por nombre)
#3. Ver agenda del día
#4. Ver resumen general
#5. Cerrar sistema
#3. Reservar:
#o Elegir día (1=Lunes, 2=Martes).
#o Pedir nombre del paciente (solo letras).
#o Verificar que no esté repetido en ese día (comparando con las variables
#ya cargadas).
#o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#4. Cancelar:
#o Elegir día.
#o Pedir nombre del paciente (solo letras).
#o Si existe, cancelar y dejar el espacio vacío ("")
#5. Ver agenda del día:
#o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
#está vacío.
#6. Resumen general:
#o Turnos ocupados y disponibles por día.
#o Día con más turnos (o empate).

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

counterL = 0
counterM = 0
bandera = 1
ticket = ""
operatorName = input("Ingrese el nombre del operador por favor: ")
validOperatorName = operatorName.isalpha()
selectedDay = ""
agenda = ""

if validOperatorName:
    while bandera:
        #print("Me ejecuto")
        print("1. Reservar turno, 2. Cancelar turno, 3. Ver agenda del día, 4.Ver resumen general")
        #bandera = 0
        menu = input("Seleccione su opción ingresando valores númericos de 1  al 5: ")
        validMenu = menu.isdigit()
        
        if validMenu:
            if menu == "1": 
                print("Reservar turno")
                selectedDay = input("Ingrese 1 si desea un turno para el Lunes o 2 para el día martes: ")
                validDay = selectedDay.isdigit()
                #print(validDay)
                if validDay:
                    if selectedDay == "1":
                        print("Ha seleccionado el día lunes")
                        pacientName = input("Ingrese el nombre del paciente: ")
                        validPacient = pacientName.isalpha()
                        if validPacient:
                            print(f"El nombre del paciente es:{pacientName}")
                            if lunes1 == "":
                                lunes1 = pacientName
                                agenda += "Lunes 1: " + pacientName
                                counterL += 1
                            elif lunes2 == "":
                                lunes2 = pacientName
                                agenda += "Lunes 2: " + pacientName
                                counterL += 1
                            elif lunes3 == "":
                                lunes3 = pacientName
                                agenda += "Lunes 3: " + pacientName
                                counterL += 1
                            elif lunes4 == "":
                                lunes4 = pacientName
                                agenda += "Lunes 4: " + pacientName
                                counterL += 1
                            else:
                                print("No hay turnos disponibles para este día")
                        else:
                            print("Error, ingrese el nombre nuevamente")
                    elif selectedDay == "2":
                        print("Ha seleccionado el día Martes")
                        pacientName = input("Ingrese el nombre del paciente: ")
                        validPacient = pacientName.isalpha()
                        if validPacient:
                            print(f"El nombre del paciente es:{pacientName}")
                            if martes1 == "":
                                martes1 = pacientName
                                agenda += "Martes 1: " + pacientName
                                counterM += 1
                            elif martes2 == "":
                                martes2 = pacientName
                                agenda += "Martes 2: " + pacientName
                                counterM += 1
                            elif martes3 == "":
                                martes3 = pacientName
                                agenda += "Martes 3: " + pacientName
                                counterM += 1
                            else:
                                print("No hay turnos disponibles para este día")
                        else:
                            print("Error, ingrese el nombre nuevamente")
                else:
                    print("Ha ingresado un día incorrecto, intente nuevamente")
            elif menu == "2": 
                print("Cancelar turno")
                cancelDay = input("Ingrese el día que desea cancelar su turno agendado, indicando si es lunes con 1 o martes con 2:")
                validDay = cancelDay.isdigit()
                if validDay:
                    if cancelDay == "1":
                        pacientName = input("Ingrese el nombre del paciente: ")
                        validPacient = pacientName.isalpha()
                        if validPacient:
                            if pacientName == lunes1:
                                lunes1 = ""
                                counterL -= 1
                                print("Turno eliminado")
                            elif pacientName == lunes2:
                                lunes2 = ""
                                counterL -= 1
                                print("Turno eliminado")
                            elif pacientName == lunes3:
                                lunes3 = ""
                                counterL -= 1
                                print("Turno eliminado")
                            elif pacientName == lunes4:
                                lunes4 = ""
                                counterL -= 1
                                print("Turno eliminado")
                            else:
                                print("El paciente ingresado no presenta turnos agendados")
                    elif cancelDay == "2":
                        pacientName = input("Ingrese el nombre del paciente: ")
                        validPacient = pacientName.isalpha()
                        if validPacient:
                            if pacientName == martes1:
                                martes1 = ""
                                counterM -= 1
                                print("Turno eliminado")
                            elif pacientName == martes2:
                                martes2 = ""
                                counterM -= 1
                                print("Turno eliminado")
                            elif pacientName == martes3:
                                martes3 = ""
                                counterM -= 1
                                print("Turno eliminado")
                            else:
                                print("El paciente ingresado no presenta turnos agendados")
            elif menu == "3":
                print("Ver agenda del día")  
                if agenda:
                    print(f"Los turnos son: {agenda}")
                else:
                    print("Hay turnos disponibles")
            elif menu == "4": 
                print("Ver resumen general")
                if lunes1 == "":
                    lunes1 = "Dia libre"
                elif lunes2 == "":
                    lunes2 = "Dia libre";
                elif lunes3 == "":
                    lunes3 = "Dia libre";
                elif lunes3 == "":
                    lunes3 = "Dia libre";
                elif lunes4 == "":
                    lunes4 = "Dia libre";
                elif martes1 == "":
                    martes1 = "Dia libre";
                elif martes2 == "":
                    martes2 = "Dia libre";
                elif martes3 == "":
                    lunes3 = "Dia libre";
                agenda = f"Turnos: lunes 1: {lunes1}, lunes 2: {lunes2}, lunes 3:  {lunes3}, lunes 4:  {lunes4}, martes 1: {martes1}, martes: 2 {martes2}, martes 3: {martes3} "
                print(f"Resumen - {agenda}, cantidad de turnos Lunes: {counterL} y cantidad de turnes Martes {counterM}")

                

            else:
                print("Has elegido una opción incorrecta intenta nuevamente")
        else:
            print("Has elegido una opción incorrecta intenta nuevamente")

else:
    bandera = 0
    print("Usuario ingresado incorrecto, intente nuevamante")