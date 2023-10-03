# como calcular IMC

def imc(estatura, peso):
    return peso / estatura**2

peso = float(input('Escriba su peso en (Kg): '))
estatura = float(input('Escriba su estatura (m): '))


Indice = imc(estatura, peso)


print('Su IMC es: {}'.format(Indice))


