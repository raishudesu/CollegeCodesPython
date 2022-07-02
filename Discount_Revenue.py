price = float(input("Enter your price: "))
quantity = float(input("Enter your quantity: "))

revenue = price * quantity
discount = float(revenue*0.10)
new_price = revenue - discount
if revenue > 5000:
    print("The discount will be: ", discount)
    print("The new price will be: ", new_price)
else:
    print("There is no discount and the revenue will be: ", revenue)
