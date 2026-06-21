print("Piensa un número del 1 al 100")

minimo = 1
maximo = 100

while True:
    intento = (minimo + maximo) // 2

    respuesta = input(f"¿Tu número es {intento}? (mayor/menor/correcto): ")

    if respuesta == "correcto":
        print("¡He adivinado tu número!")
        break

    elif respuesta == "mayor":
        minimo = intento + 1

    elif respuesta == "menor":
        maximo = intento - 1
      
