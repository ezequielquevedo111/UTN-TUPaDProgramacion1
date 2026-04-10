#Ejercicio 2 — “Acceso al Campus y Menú Seguro”#
#Objetivo: Login con intentos + menú de acciones con validación estricta.#
#Requisitos
#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#o clave correcta: "python123"
#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; deben
#coincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir
#5. Validación del menú:
#o Debe ser número (.isdigit())
#o Debe estar entre 1 y 4

user = "alumno"
password = "python123"
bandera = 0
userTest = ""
userPassword = ""

while bandera < 3:
    userTest = input("Ingrese su nombre de usuario:")
    userPassword = input("Ingrese su contraseña:")
    menu = 1
    if userTest == user and userPassword == password:
        while menu > 0 and menu < 4:
            print("1. Ver estado de inscripción, 2. Cambiar de clave, 3. Mostrar mensaje motivacional, 4. Salir")
            menu = int(input("Seleccione su opción"))
            if menu == 1:
                print("Estas inscripto")
            elif menu == 2:
                nPassword = input("Ingrese la nueva contraseña de 6 caracteres: ")
                validPass = len(nPassword)
                if validPass == 6:
                    print(f"Nueva clave: {nPassword}")
                    print("Clave cambiada")
                else:
                    print("Contraseña incorrecta pruebe más tarde nuevamente")
            elif menu == 3:
                print("Cada paso te ayuda a lograr eso que deseas")
            elif menu == 4:
                bandera = 3
            else:
                print("Has ingresado una opción invalida, por favor ingresa nuevamente un digito entre 1 y 4.")
    else:
        bandera += 1
        if bandera < 3:
            print("Has ingresado el usuario y/o contraseña incorrecta")
        else:
            print("Cuenta bloqueada")