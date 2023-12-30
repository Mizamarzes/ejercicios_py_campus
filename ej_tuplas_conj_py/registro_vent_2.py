list_sales = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
    ("ProductoD", 10, 320),
]

def calcular_agregados(ventas):
    agregados = {}
    
    for producto, cantidad, ingreso in ventas:
        if producto not in agregados:
            agregados[producto] = {"cantidad": 0, "ingreso": 0}
        
        agregados[producto]["cantidad"] += cantidad
        agregados[producto]["ingreso"] += ingreso

    return agregados

def imprimir_resultados(agregados):
    for producto, valores in agregados.items():
        print(f"Cantidad {producto}: {valores['cantidad']}, Ingreso: {valores['ingreso']}")

        if valores['cantidad'] > 10:
            print(f"El producto {producto} tiene más de 10 ventas")

def main():
    agregados_ventas = calcular_agregados(list_sales)
    imprimir_resultados(agregados_ventas)

if __name__ == "__main__":
    main()