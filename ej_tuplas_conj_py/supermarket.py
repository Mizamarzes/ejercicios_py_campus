def create_products(list_product):
    aggregates={}
    for code, name, price, cant in list_product:
        if code not in aggregates:
            aggregates[code] = {"name": name, "price": price, "cant": cant}
    return aggregates

def create_sales(list_sales):
    aggregates_sales={}
    for ballot, code1, cant_pr in list_sales:
        if code1 not in aggregates_sales:
            aggregates_sales[ballot] = {"code": code1, "cant_pr": cant_pr}
    return aggregates_sales

def most_expensive_product(list_product):
    max_product = max(list_product.values(), key=lambda x: x['price'])
    product_info = max_product
    max_name = product_info['name']
    max_price = product_info['price']
    return max_name, max_price

def value_amount_winery(list_product):
    sum_values=0
    for code, data in list_product.items():
        value=data['price']*data['cant']
        sum_values+=value
    return sum_values

def income_sales(list_product, list_sales):
    total_income=0
    for _, code1, cant_pr in list_sales:
        product_info = list_product.get(code)

        if product_info:
                price=product_info['price']
                income=price*cant_pr
                total_income+=income
    return total_income

def print_results(list_product):
    for code, data in list_product.items():
        print(f"Code: {code}, name: {data['name']}, price: {data['price']}, cant: {data['cant']}")
        
productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]

ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]

create_dictionary_products=create_products(productos)
create_dictionary_sales=create_sales(itemes)
# name_most, price_most=most_expensive_product(create_dictionary)
# print(f"Name: {name_most}, price: {price_most}")
# value_total_winery=value_amount_winery(create_dictionary)
# print(f"Value total winery: {value_total_winery}")
total_income_sales=income_sales(create_dictionary_products, create_dictionary_sales)
print(f"Total income for sales: {total_income_sales}")
# print_results(create_dictionary)