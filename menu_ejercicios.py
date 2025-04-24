#Solucion de ejercicios praticos de python

#=======================================================================================

while True:
    try:
        print("""Bienvenido al menu de ejercios riwi seleciona una opcion para continuar
        ===================================================================
        1. Ingresar datos por consola
        2. Tipos de datos en python 
        3. Operadores en python
        4. operadores relacionales
        5. operadores logicos
        6. salir""")

        opcion = int(input("\n"))
        if opcion == 1:
            
            # 1.1
            nombre,edad = input("Ingresa tu nombre y tu edad separados por coma(,): ").split(",")
            print(f"hola {nombre} tienes {edad} años")

            # 1.2

            comida,color = input("Ingresa tu comida favorita y tu color favorito separados por coma(,): ").split(",")
            print(f"tu comida favorita es {comida} y tu color favorito es el {color} ")

            # 1.3

            numero = int(input("Ingresa un numero: "))
            print("doble de el numero:", numero * 2, "triple del numero:", numero * 3)

  
        elif opcion == 2:

            # 2.1

            buli = True
            entero = 9
            flotante = 8.6
            cadena = ""

            # 2.2

            textonum = str(input("Ingresa un valor: "))
            valor = int(textonum)
            print(valor + 5)

            # 2.3

            textonum2 = str(input("\nIngresa otro valor: "))
            valor2 = float(textonum2)
            print(valor2 * 2 ,"\n")

            #2.4

            def es_numero(cadena):
                try:
                    float(cadena)
                    return True
                except ValueError:
                    return False
                
            print(es_numero("123"))
            print(es_numero("45.67"))
            print(es_numero("abc"))

        elif opcion == 3:

            # 3.1

            base = float(input("Ingrese el valor de la base: "))
            altura = float(input("Ingrese el valor de la altura: "))
            print("area del rectangulo: ", base * altura) 

            # 3.2

            precio = float(input("\nIngrese un precio: "))
            desc = float(input("Ingrese un descuento: "))
            valdesc = precio * desc/100
            print("Precio final despues del descuento: ", precio - valdesc)

            # 3.3

            num1 = int(input("\nIngrese el valor del numero 1: "))
            num2 = int(input("Ingrese el valor del numero 2: "))
            print("Residuo de la division: ",num1 % num2)

            # 3.4


        elif opcion == 4:
            # 4.1

            num3 = int(input("Ingrese el valor del numero 1: "))
            num4 = int(input("Ingrese el valor del numero 2: "))
            if num3 > num4:     
                print(num3,"es mayor que",num4)
            elif num4 > num3:
                print(num4,"es mayor que ",num3)
            elif num4 == num3:
                print(num3, "y", num4,"son iguales ")

            # 4.2

            edad = int(input("\ningrese su edad: "))
            if edad < 18:
                print("Eres menor de edad tienes ",edad,"años ")
            if edad >= 18:
                print("Eres mayor de edad tienes ",edad,"años ")
                 
            # 4.3

            mensj1 = str(input("\nIngrese el mensaje numero 1: ").lower())
            mensj2 = str(input("Ingrese el mensaje numero 2: ").lower())
            if mensj1 == mensj2:
                print("el mensaje es igual")
            else:
                print("El mensaje es diferente")

        elif opcion == 5:

            # 5.1
         
            edad2 = int(input("porfavor ingrese su edad: "))
            licencia = str(input("Tienes licencia ? (S-N)").upper())
            if edad2 >= 18 and licencia == "S":
                print("Puedes Conducir")
            else: 
                print("No puedes conducir")

            # 5.2

            exp = int(input("\nIngrese sus meses de experiencia: "))
            titulU = str(input("Tienes titulo universitario ? (S-N) ").upper())
            if exp >= 6 and titulU == "S":
                print("Puedes aplicar a la oferta de trabajo")
            else:
                print("No puedes aplicar a la oferta de trabajo")

            # 5.3

            num5 = int(input("\nIngrese el valor de el numero: "))
            if num5 >= 10 and num5 <= 50:
                print("Tu numero esta en un rango de 10 - 50")
            else:
                print("Tu numero no esta en un rango de 10 - 50")

        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("¡Error ingrese una opcion correcta del 1 al 6!")
    
    
    except ValueError:
        print("¡Error ingrese una opcion correcta del 1 al 6!")