class ItemToPurchase:
    def __init__(self, item_name="none", item_price= 0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
        return total_cost
def main():
    print('Item 1')
    item_name = input("Enter the item name:")
    item_price = float(input("\nEnter the item price:"))
    item_quantity = int(input('\nEnter the item quantity:'))
    item1 =ItemToPurchase(item_name, item_price, item_quantity)

    print('\nItem 2')
    item_name = input("Enter the item name:")
    item_price = float(input("\nEnter the item price:"))
    item_quantity = int(input('\nEnter the item quantity:'))
    item2 =ItemToPurchase(item_name, item_price, item_quantity)

    print('\nTOTAL COST: ')
    item1.print_item_cost()
    item2.print_item_cost()
    total = item1.print_item_cost() + item2.print_item_cost()
    print('Total: $',total)
if __name__== "__main__" :
    main()