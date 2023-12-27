def process(n,cant):
    i=0
    total=0
    desc=0
    while i<cant:
        i+=1
        print(f"Enter the price of product {i}:")
        
        try:
            price = float(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            i -= 1
            continue
        
        dif=cant/n
        a=n*int(dif)

        if i<=a:
            if i <= n:
                discount_rate = 0.2
            elif n < i <= n * 2:
                discount_rate = 0.1
            else:
                discount_rate = 0.05
        
            discount = price * discount_rate
            desc+=discount

        total+=price

    return total,desc


print("WELCOME")
try:
    n = int(input("Enter a number: "))
    cant = int(input("Enter the number of products: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

total, desc = process(n, cant)
total_after_discount = total - desc

print(f"TOTAL: ${total}")
print(f"DISCOUNT: ${desc}")
print(f"PAYABLE: ${total_after_discount}")

