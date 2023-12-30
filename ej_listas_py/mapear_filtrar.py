def mapear(f, valores):
    # Aplicar la función f a cada elemento de la lista valores
    resultados = [f(valor) for valor in valores]
    return resultados

def filtrar(f, valores):
    # Filtrar los elementos de la lista valores para los cuales f retorna True
    resultados_filtrados = [valor for valor in valores if f(valor)]
    return resultados_filtrados

# Ejemplo de uso
def cuadrado(x):
    return x ** 2

def es_larga(palabra):
    return len(palabra) > 4

# Ejemplos de uso
lista_original_mapear = [5, 2, 9]
resultado_mapeo = mapear(cuadrado, lista_original_mapear)
print("Mapear:", resultado_mapeo)

lista_original_filtrar = ['arroz', 'leon', 'oso', 'mochila']
resultado_filtrado = filtrar(es_larga, lista_original_filtrar)
print("Filtrar:", resultado_filtrado)

















