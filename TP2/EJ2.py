import numpy as np

import math

#%matplotlib inline


# funcion objetivo
def funcion_objetivo(x, y, a, b):
    
    return (x - a)**2 + (y + b)**2


def PSO(a, b, num_particulas, dim, limite_inf, limite_sup):

    # inicializacion
    particulas = np.random.uniform(limite_inf, limite_sup, (num_particulas, dim))  # posiciones iniciales de las particulas

    velocidades = np.zeros((num_particulas, dim))  # inicializacion de la matriz de velocidades en cero

    # inicializacion de pbest y gbest
    pbest = particulas.copy()  # mejores posiciones personales iniciales

    fitness_pbest = np.empty(num_particulas)  # mejores fitness personales iniciales
    for i in range(num_particulas):
        fitness_pbest[i] = funcion_objetivo(particulas[i][0], particulas[i][1], a, b)

    # cambiando por np.argmin y por np.min creo que tenemos un problema de minimización
    gbest = pbest[np.argmin(fitness_pbest)]  # mejor posicion global inicial
    fitness_gbest = np.min(fitness_pbest)  # fitness global inicial


    # aplicamos el algoritmo
    # busqueda
    for iteracion in range(cantidad_iteraciones):
        for i in range(num_particulas):  # iteracion sobre cada partícula
            r1, r2 = np.random.rand(), np.random.rand()  # generacion dos numeros aleatorios

            # actualizacion de la velocidad de la particula en cada dimension
            for d in range(dim):
                velocidades[i][d] = (w * velocidades[i][d] + c1 * r1 * (pbest[i][d] - particulas[i][d]) + c2 * r2 * (gbest[d] - particulas[i][d]))

            for d in range(dim):
                particulas[i][d] = particulas[i][d] + velocidades[i][d]  # cctualizacion de la posicion de la particula en cada dimension

                # mantenimiento de las partículas dentro de los limites
                particulas[i][d] = np.clip(particulas[i][d], limite_inf, limite_sup)

            fitness = funcion_objetivo(particulas[i][0], particulas[i][1], a, b)  # Evaluacion de la funcion objetivo para la nueva posicion

            # actualizacion el mejor personal
            if fitness < fitness_pbest[i]:
                fitness_pbest[i] = fitness  # actualizacion del mejor fitness personal
                pbest[i] = particulas[i].copy()  # actualizacion de la mejor posicion personal

                # actualizacion del mejor global
                if fitness < fitness_gbest:
                    fitness_gbest = fitness  # actualizacion del mejor fitness global
                    gbest = particulas[i].copy()  # actualizacion de la mejor posicion global

        # imprimir el mejor global en cada iteracion
        print(f"Iteración {iteracion + 1}: Mejor posición global {gbest}, Valor {fitness_gbest}")

    return gbest, fitness_gbest


# parametros
num_particulas = 20  # numero de particulas
dim = 2  # dimensiones
cantidad_iteraciones = 10  # maximo numero de iteraciones
c1 = 2  # componente cognitivo
c2 = 2  # componente social
w = 0  # factor de inercia
limite_inf = -100 # limite inferior de busqueda
limite_sup = 100 # limite superior de busqueda


flag = True
while(flag):

    flag = str(input("Quieres continuar usando el programa (Si) o dejar de usar el programa (No): "))

    if flag == 'No':
        print("El programa se cerrará")
        break
    elif flag =='Si':
        a = float(input("Por favor, ingresa el valor de a: "))
        print("Ingresaste el número:", a)
        b = float(input("Por favor, ingresa el valor de b: "))
        print("Ingresaste el número:", b)

        if a < -50 and a > 50:
            print("Valor de a es incorrecto, el rango debe ser entre -50 y 50")

        if b < -50 and b > 50:
            print("Valor de b es incorrecto, el rango debe ser entre -50 y 50")

        # resultado
        gbest, fitness_gbest = PSO(a, b, num_particulas, dim, limite_inf, limite_sup)

        solucion_optima = gbest  # mejor posicion global final
        valor_optimo = fitness_gbest  # mejor fitness global final

        print(f"a={a} y b={b}")
        print("Valor optimo:", valor_optimo)
        print("La solucion optima ocurre en [x, y] = ", solucion_optima)

    else:
        print("Ingresa un valor correcto: Si o No")
