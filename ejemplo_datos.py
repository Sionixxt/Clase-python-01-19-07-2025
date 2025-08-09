
from Estudiantes.Calculadora import Calculadora as calc
from Estudiantes.estudiante import Estudiante as Un

while True:
    try:
        menu = int(input(" (1)Estudiante, (2)Calculadora o (3)Salir: "))
    except ValueError:
        print("Por favor, ingrese una opción válida.")
        continue
    if menu == 1:
        while True:
            opcion=int(input("(1)Agregar Estudiante, (2)Eliminar, (3)Buscar, (4)Listar, (5)Modificar, (6)Salir: "))
            if opcion == 1:
                nombre = input("Ingrese el nombre del estudiante: ")
                apellido = input("Introduzca el apellido del estudiante: ")
                FechaNacimiento = input("Introduzca la fecha de nacimiento dd/mm/yy: ")
                cedula = input("Introduzca la cédula: ")
                grupo = input("Introduce tu grupo: ")
                nota = []
                for i in range(3):
                    nota.append(float(input(f"Introduzca la nota {i+1} del estudiante: ")))
                estudiante = Un(nombre, apellido, cedula, FechaNacimiento, grupo, nota)
                estudiante.AgregarEstudiante()
                print("Estudiante agregado con éxito.")
                break
            elif opcion==2:
                cedula = input("Introduzca la cédula del estudiante a eliminar: ")
                Un.EliminarEstudiante(cedula)
            elif opcion==3:
                cedula = input("Introduzca la cédula del estudiante a buscar: ")
                Un.BuscarEstudiante(cedula)
            elif opcion==4:
                Un.Listar()
            else:
                break
            nombre = input("Introduzca el nombre del estudiante: ")
            apellido = input("Introduzca el apellido del estudiante: ")
            FechaNacimiento = input("Introduzca la fecha de nacimiento dd/mm/yy: ")
            cedula = input("Introduzca la cédula: ")
            grupo = input("Introduce tu grupo: ")
            nota = []
            for i in range(3):
                nota.append(float(input(f"Introduzca la nota {i+1} del estudiante: ")))
            est1 = Un(nombre, apellido, cedula, FechaNacimiento, grupo, nota)
            est1.mostrar_info()

            try:
                respuesta = int(input("¿Desea procesar otro estudiante? (1)Sí o (2)No: "))
                if respuesta != 1:
                    break
            except ValueError:
                print("Entrada inválida. Regresando al menú principal.")
                break
    elif menu == 2:
        while True:
            try:
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                calc1 = calc(n1, n2)

                print("\nSeleccione la operación:")
                print("1. Sumar")
                print("2. Restar")
                print("3. Multiplicar")
                print("4. Dividir")
                opcion = input("Opción (1-4): ")

                if opcion == "1":
                    print(f"Resultado: {calc1.sumar()}")
                elif opcion == "2":
                    print(f"Resultado: {calc1.restar()}")
                elif opcion == "3":
                    print(f"Resultado: {calc1.multiplicar()}")
                elif opcion == "4":
                    print(f"Resultado: {calc1.dividir()}")
                else:
                    print("Opción inválida.")

                continuar = int(input("\n¿Desea realizar otra operación? (1)Sí o (2)No: "))
                if continuar != 1:
                    break
            except ValueError:
                print("Por favor, ingrese números válidos.")

    elif menu == 3:
        print("Saliendo del programa. Hasta luego")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

