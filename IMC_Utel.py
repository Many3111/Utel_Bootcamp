# Como calcular IMC
   
def imc(estatura, peso):
    return peso / estatura**2

while True:
    while True:
        try:
            peso = float(input('Escriba su peso en (Kg): '))
            estatura = float(input('Escriba su estatura (m): '))
        
            Indice = imc(estatura, peso)

            if Indice <= 1:
                print('El IMC calculado es inusual. Por favor, vuelva a ingresar sus datos.')
            else:
                break 
        except ValueError:
            print('Se ingresó un valor incorrecto, por favor, ingrese un valor numérico válido en kilos(Kg) y metros(m).')


    if Indice <= 24.9 and Indice >= 18.5:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC se encuentra normal')
    elif Indice <= 29.9 and Indice >= 25:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC es: {}'.format(Indice))
        print('Su IMC indica que tiene ligero sobrepeso')
    elif Indice <= 34.9 and Indice >= 30:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC es: {}'.format(Indice))
        print('Su IMC indica que sufre de obesidad grado 1')
    elif Indice <= 39.9 and Indice >= 35:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC es: {}'.format(Indice))
        print('Su IMC indica que sufre de obesidad grado 2')
    elif Indice >= 40:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC es: {}'.format(Indice))
        print('Su IMC indica que sufre de obesidad grado 3')
    elif Indice <=24.8 and Indice >=2:
        print('Peso (Kg): {}'.format(peso))
        print('Altura (m): {}'.format(estatura))
        print('Su IMC es: {}'.format(Indice))
        print('La cantidad indicada de su IMC esta por debajo de los niveles recommendados, se recomienda consultar a su medico')
    else:
        print()

    resultado = input('¿Desea ingresar nuevos datos? (si/no): ')
    if  resultado != 'si':
        break

print('¡Gracias por su tiempo!')