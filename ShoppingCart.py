# Shopping Cart Project :

Foods  = []
Prices = []
Total  = 0
while True :
    Food = input("Enter a food to BUY (q to quit) : ").lower()
    if Food == 'q' :
        break
    else :
        Price = float(input(f"Enter the price of {Food} : $ "))
        Foods.append(Food)
        Prices.append(Price)
print("------ Your Cart -------")
for Food in Foods :
    print(Food)
for Price in Prices :
    Total = Total + Price
print(f"Your Total is = {Total}")
