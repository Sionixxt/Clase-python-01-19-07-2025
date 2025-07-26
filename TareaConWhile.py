while True:
    menu=int(input("(1)Saludo Personalizado, (2)Valor Absoluto, (3)Calculadora, (4)Promedio o (5)Salir: "))

    if menu==1:
        nombre=input("Ingrese su nombre: ")
        print("Un placer conocerte", nombre)
    elif menu==2:
        num=int(input("Ingrese un numero: "))
        if num>=0:
            absoluto=num
        else:
            absoluto=num*-1
        print(f"El valor absoluto {num} es {absoluto}")
    elif menu==3:
        opcion=int(input("(1)Suma, (2)Resta, (3)Multiplicacion, (4)Division o (5)Salir:  "))
        
        if opcion==5:
            print("Gracias por usar la calculadora")
            break
        elif opcion==1 or opcion==2 or opcion==3 or opcion==4:
            num1=float(input("Introduca el primero numero: "))
            num2=float(input("Introduzca el segundo numero: "))
            if opcion==1:
                print(f"La suma de {num1} + {num2} es {num1+num2}")
            elif opcion==2:
                print(f"La resta de {num1} - {num2} es {num1-num2}")
            elif opcion==3:
                print(f"La multiplicacion de {num1} * {num2} es {num1*num2}")
            elif opcion==4:
                if num2==0:
                    print("Division por cero no se puede realizar.")
                else:
                    print(f"La division de {num1} / {num2} es {num1/num2}")
    elif menu==4:
        nombre=input("Ingrese su nombre: ")
        nota1=float(input("Introduzca la priemra nota: "))
        nota2=float(input("Introduzca la segunda nota: "))
        nota3=float(input("Introduzca la tercera nota: "))
        
        if nota1>20 or nota2>20 or nota3>20 or nota1<0 or nota2<0 or nota3<0:
            print("No se puede evaluar con notas mayores a 20 o menores a 0")
        else:
            promedio=(nota1+nota2+nota3)/3
            if promedio>12:
                state="Aprobado"
            else:
                state="Reprobado"
            print(f"El estudiante {nombre} tiene un promedio de {promedio} y esta {state}")
    else:
        print("Gracias por utilizar el programa, Hasta luego.")
        break