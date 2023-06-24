import datetime
num =0
total_price =0.0
name = input("Please enter your name")
print("{}'s Shopping Cart-{}".format( name, datetime.date.today()))
while True:
    items_name = input("Please enter the item name: ")
    items_price = float(input("Please enter the price: "))
    items_quantity = int(input("Please enter the quantity: "))

    total_cost = items_price * items_quantity
    num=num+items_quantity
    total_price = total_price + total_cost
    print('TOTAL COST:\n{} {} @ ${} = ${}'.format(items_name, items_quantity, items_price, total_cost))

    choice = input("Do you want to enter another item? (yes/no): ")
    if choice.lower() != "yes":
        break
print( "number of Items:", num)
print("Total:", total_price, '$')
