import os

def clear_screen():
    os.system('clear')

def register_city(sismos_of_cities):
    name_city = input("Enter the name of the city: ")
    sismos_of_cities.append({"name": name_city, "earthquakes": []})
    print(f"City: {name_city} successfully registered")

def register_earthquakes(sismos_of_cities):
    if not sismos_of_cities:
        print("No city registered. Register a city first.")
        return

    print("Select a city to record the earthquake:")
    for i, city in enumerate(sismos_of_cities):
        print(f"{i + 1}. {city['name']}")

    try:
        option_city = int(input())
        city_selection = sismos_of_cities[option_city - 1]
        magnitud_sismo = float(input("Enter the magnitude of the earthquake: "))
        city_selection['earthquakes'].append(magnitud_sismo)
        print(f"Earthquake registered at the city {city_selection['name']}.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid city option.")

def search_sequential(sismos_of_cities):
    if not sismos_of_cities:
        print("No city registered. Register a city first.")
        return
    
    for i, city in enumerate(sismos_of_cities):
        print(f"{i + 1}. {city['name']}")

    try:
        option_city = int(input("Select a city to show the earthquakes: "))
        print(f"{sismos_of_cities[option_city - 1]['name']}, Earthquakes: {sismos_of_cities[option_city - 1]['earthquakes']}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid city option.")

def risk_report(sismos_of_cities):
    if not sismos_of_cities:
        print("No city registered. Register a city first.")
        return

    for city in sismos_of_cities:
        average_sismos = sum(city['earthquakes']) / len(city['earthquakes'])
        riesgo = ""

        if average_sismos < 2.5:
            riesgo = "Amarillo (Sin riesgo)"
        elif 2.6 <= average_sismos <= 4.5:
            riesgo = "Naranja (Riesgo medio)"
        else:
            riesgo = "Rojo (Riesgo alto)"

        print(f"Ciudad: {city['name']}, Promedio de sismos: {average_sismos:.2f}, Riesgo: {riesgo}")

# variables
sismos_of_cities = []

while True:
    print("\nMenu:")
    print("1. Register city")
    print("2. Register earthquakes")
    print("3. Search for earthquakes by city ")
    print("4. Risk Report")
    print("5. Exit")
    
    try:
        option = int(input("Enter: "))
        clear_screen()

        if option == 1:
            register_city(sismos_of_cities)
        elif option == 2:
            register_earthquakes(sismos_of_cities)
        elif option == 3:
            search_sequential(sismos_of_cities)
        elif option == 4:
            risk_report(sismos_of_cities)
        elif option == 5:
            print("¡THANK YOU FOR USING OUR SERVICE!")
            break
        else:
            print("Option not valid. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")