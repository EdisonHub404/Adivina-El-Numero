# Proyecto: Adivina el Número
# Autor: Edison Osmany
# El computador intenta adivinar el número pensado por el usuario

print("Bienvenido al juego Adivina el Número")
print("Piensa un número entre 1 y 100.")

# Límites iniciales
minimo = 1
maximo = 100

# Contador de intentos
intentos = 0

# Bucle principal del juego
while True:

    # El computador calcula un intento
    intento = (minimo + maximo) // 2
    intentos += 1

    print(f"\n¿Tu número es {intento}?")

    respuesta = input(
        "Escribe: mayor, menor o correcto: "
    ).lower()

    # Si el computador acierta
    if respuesta == "correcto":
        print(f"\n¡He adivinado tu número en {intentos} intentos!")
        break

    # Si el número del usuario es mayor
    elif respuesta == "mayor":
        minimo = intento + 1

    # Si el número del usuario es menor
    elif respuesta == "menor":
        maximo = intento - 1

    # Si el usuario escribe algo incorrecto
    else:
        print("Respuesta no válida. Intenta nuevamente.")
