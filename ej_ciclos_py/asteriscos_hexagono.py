#dibujar hexagono con asteriscos
a = int(input("Lado: "))

# Parte superior del hexágono
for i in range(a):
    print(" " * (a - i - 1) + "*" * (2 * i + 1))

# Parte inferior del hexágono
for i in range(a - 2, -1, -1):
    print(" " * (a - i - 1) + "*" * (2 * i + 1))