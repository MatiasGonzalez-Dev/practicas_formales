'''
1. genera un numero entre 1 y 100 (usa import random y random.randit(1,100)
2. pida al usuario que adivine, usando el bucle while que siga preguntando hasta que adivine
3. despues de cada intento, indique si el numero secreto es mas alto o bajo
4. al final muestre cuantos intentos uso.'''


import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es más alto.")
    elif intento > numero_secreto:
        print("El número secreto es más bajo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break