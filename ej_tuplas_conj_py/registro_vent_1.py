
list_sales=[
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
]

def calculations(sales):
    sum_amount_productA=0;sum_income_productA=0
    sum_amount_productB=0;sum_income_productB=0
    sum_amount_productC=0;sum_income_productC=0
    for product,cant,income in sales:
        if product=="ProductoA":
            sum_amount_productA+=cant
            sum_income_productA+=income
        elif product=="ProductoB":
            sum_amount_productB+=cant
            sum_income_productB+=income
        elif product=="ProductoC":
            sum_amount_productC+=cant
            sum_income_productC+=income

    if sum_amount_productA>10:
        print("Product A to has more than 10 sales")

    if sum_amount_productB>10:
        print("Product B to has more than 10 sales")

    if sum_amount_productC>10:
        print("Product C to has more than 10 sales")

    print(f"Amount product A: {sum_amount_productA}, income: {sum_income_productA}")
    print(f"Amount product B: {sum_amount_productB}, income: {sum_income_productB}")
    print(f"Amount product C: {sum_amount_productC}, income: {sum_income_productC}")


calculations(list_sales)

# cant_ventas={
#     "ProductoA": 10,
#     "ProductoB": 5,
#     "ProductoA": 8,
#     "ProductoC": 12,
#     "ProductoB": 3,
#     "ProductoA": 15,
#     "ProductoC": 7
# }
    
# for product, cant in cant_ventas.items():
#     print(f"{product}: {cant}")
   
    

# print("TOTAL DE VENTAS: ", totalVent)
# print("PRODUCTOS CON MAS DE 10 VENTAS: ", maxP)



# persona = {
#     "nombre": "Juan",
#     "edad": 25,
#     "ciudad": "Ciudad de México",
#     "ocupacion": "Desarrollador"
# }


# for jugador, puntaje in puntajes.items():
#     print(f"{jugador}: {puntaje}")















