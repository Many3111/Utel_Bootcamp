# Como calcular IMC

def imc(estatura, peso):
    return peso / estatura**2

peso = float(input('Escriba su peso en (Kg): '))
estatura = float(input('Escriba su estatura (m): '))


Indice = imc(estatura, peso)

if Indice <= 1 and Indice >= 0:
    print('Hubo un error en los datos ingresados favor de reingresar los datos en base a kg(peso) y m(altura)')
elif Indice <= 24.9 and Indice >= 18.5:
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
elif Indice >= 40:
    print('Peso (Kg): {}'.format(peso))
    print('Altura (m): {}'.format(estatura))
    print('Su IMC es: {}'.format(Indice))
    print('Su IMC indica que sufre de obesidad grado 1')
elif Indice <=24.8 and Indice >=2:
    print('Peso (Kg): {}'.format(peso))
    print('Altura (m): {}'.format(estatura))
    print('Su IMC es: {}'.format(Indice))
    print('La cantidad indicada de su IMC esta por debajo de los niveles recommendados, se recomienda consultar a su medico')
else:
    print('Peso (Kg): {}'.format(peso))
    print('Altura (m): {}'.format(estatura))
    print('Su IMC es: {}'.format(Indice))
    print('Por favor de usar unicamente digitos para llenar su solicitud')


