
# - Agregue el import random para que me obtener resultados aleatorios
# - Agregue el import matplotlib.pyolot para obtener una representacion 
# grafica de los resultados

import random
import matplotlib.pyplot as plt

# - Permite iniciar con 0 canicas en cada contenedor y agrega la cantidad 
# de contenedores requiridos por cada obstaculo
def simular_canicas(num_canicas, niveles):
    contenedores = [0] * (niveles + 1)  
    
# - Con el siguiente bucle permite que por cada canica se aplique otro bucle
# en el cual por cada nivel se elija la opcion de derecha o izquierda
    for i in range(num_canicas):
        nivel_actual = 0
        for i in range(niveles):
            direccion = random.choice(["izquierda", "derecha"])
            if direccion == "izquierda":
                nivel_actual += 1
        contenedores[nivel_actual] += 1  
        # Agrega la canica al contenedor correspondiente
    
    return contenedores

def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores)
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de canicas')
    plt.title('Distribución de canicas en contenedores')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
niveles_obstaculos = 12

# Simulación de las canicas y graficación del histograma
resultados_canicas = simular_canicas(num_canicas, niveles_obstaculos)
graficar_histograma(resultados_canicas)
