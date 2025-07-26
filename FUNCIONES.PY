def saludar(name):
    return print("Un placer conocerte", name)

def valor_absoluto(num):
    return print(f"El valor absoluto de {num} es {abs(num)}")

def calculadora():
    while True:
        opcion=int(input("(1)Suma, (2)Resta, (3)Multiplicacion, (4)Division o (5)Salir:  "))
        if opcion==5:
            print("Gracias por usar la calculadora")
            break
        if opcion==1 or opcion==2 or opcion==3 or opcion==4:
                num1=float(input("Introduca el primero numero: "))
                num2=float(input("Introduzca el segundo numero: "))
                if opcion==1:
                    return print(f"La suma de {num1} + {num2} es {num1+num2}")
                elif opcion==2:
                    return print(f"La resta de {num1} - {num2} es {num1-num2}")
                elif opcion==3:
                    return print(f"La multiplicacion de {num1} * {num2} es {num1*num2}")
                elif opcion==4:
                    if num2==0:
                        return print("Division por cero no se puede realizar.")
                    else:
                        return print(f"La division de {num1} / {num2} es {num1/num2}")
        
def estudiante():
    nombre=input("Ingrese su nombre: ")
    sum=0
    for i in range(3):
        nota=float(input(f"Introduzca la nota {i+1}: "))
        if nota>20 or nota<0 :
            print("No se puede evaluar con notas mayores a 20 o menores a 0")
        else:
            sum+=nota
            promedio=sum/3
            if promedio>12:
                state="Aprobado"
            else:
                state="Reprobado"
    return print(f"El estudiante {nombre} tiene un promedio de {promedio} y esta {state}")

def menu():
    print("Bienvenido al programa")
    while True: 
        
        menu=int(input("(1)Saludo Personalizado, (2)Valor Absoluto, (3)Calculadora, (4)Promedio o (5)Salir: "))

        if menu==1:
            nombre=input("Introuzca su nombre: ")
            saludar(nombre)
        elif menu==2:
            numero=int(input("Introduzca el numnero: "))
            valor_absoluto(numero)
        elif menu==3:
            calculadora()
        elif menu==4:
            estudiante()
        else:
            print("Gracias por usar el programa")
            break
menu()