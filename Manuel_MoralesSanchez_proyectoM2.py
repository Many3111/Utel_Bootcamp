# Primera actividad Longitud de una frase

#  Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta 
# debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:

#  Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe
# imprimir un mensaje que indique que la palabra es correcta

#  Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta
# letras. Solo tiene N letras (siendo N el número de letras de la palabra)

#  Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. 
# Tiene N letras ((siendo N el número de letras de la palabra))

print("Para la primera actividad comprobare si los datos ingresados son correctos.\n")

while True:
    
    Palabra = input("Favor de ingresar una palabra de 8 letras: ")

    if Palabra.isalpha() == True:  
        if len(Palabra) < 4:
            print("Lo siento, hacen falta letras. Solo tiene",len(Palabra),"letras. Intente de nuevo\n")
        elif len(Palabra) > 8:
            print("Lo lamento sobraron letras. La palabra ingresada tiene",len(Palabra),"letras. Intente de nuevo\n")
        else:
            print("La cantidad de letras ingresadas es correcta. Muchas gracias por participar en mi\
 primera activadad del proyecto M2\n\n") 
            break
    else:
        print("Lo siento, la informacion ingresada no es correcta, favor de ingresar unicamente letras")


# Segunda actividad:

# Crear un programa que en base a 2 números de entrada, coordenadas,
# identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa
# debe verificar que ninguna coordenada sea 0.

print("Para la siguiente actividad debere de ubicar en que cuadrante de un sistema cartesiano,\
 se encontran los valores ingresados:\n")

while True:
    while True:
        try:
            ValorX = int(input('Ingrese el valor del eje X: '))
            ValorY = int(input('Ingrese el valor del eje Y: '))
        
            if ValorX > 0 and ValorY > 0:
                print("La coordenada ingresada se encuentra en el cuadrante 1")
                break
            elif ValorX < 0 and ValorY > 0:
                print("La coordenada ingresada se encuentra en el cuadrante 2")
                break
            elif ValorX > 0 and ValorY < 0:
                print("La coordenada ingresada se encuentra en el cuadrante 4")
                break
            elif ValorX < 0 and ValorY < 0:
                print("La coordenada ingresada se encuentra en el cuadrante 3")
                break
            elif ValorX == 0:
                print("No se puede determinar un cuandrante si el valor ingresado es 0. Favor de intentar de nuevo")
            elif ValorY == 0:
                print("No se puede determinar un cuandrante si el valor ingresado es 0. Favor de intentar de nuevo")
        except ValueError:
            print("El dato ingresado debe ser un valor numerico. Favor de intentar de nuevo")
        
    resultado = input('¿Desea ingresar nuevos datos? (si/no): ')
    if  resultado == 'si' or resultado == 's' or resultado == 'Si' or resultado == 'SI':
        print()
    else:
        break

print("\nMuchas gracias por participar en mi segunda actividad del poyecto M2.\n\n¡Que pasen un excelente dia!")