class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")
        return int(total_cost)

    def print_item_description(self):
        print(self.item_description)


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        if item_name not in self.cart_items:
            print('Item not found in cart. Nothing removed.')
        else:
            self.cart_items = [item for item in self.cart_items if item.item_name != item_name]

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print('Item not found in cart. Nothing modified.')

    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            total_cost = 0
            print('\nTOTAL COST')
            for item in self.cart_items:
                total_cost += item.print_item_cost()
            print('\nTotal: ${}'.format(total_cost))

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost


def main():
    print('Item 1')
    item_name = input("Enter the item name: ")
    item_price = float(input("\nEnter the item price: "))
    item_quantity = int(input('\nEnter the item quantity: '))
    item1 = ItemToPurchase(item_name, item_price, item_quantity)

    print('\nItem 2')
    item_name = input("Enter the item name: ")
    item_price = float(input("\nEnter the item price: "))
    item_quantity = int(input('\nEnter the item quantity: '))
    item2 = ItemToPurchase(item_name, item_price, item_quantity)

    shopping_cart = ShoppingCart()
    shopping_cart.add_item(item1)
    shopping_cart.add_item(item2)

    print()
    shopping_cart.print_total()

    num_items = shopping_cart.get_num_items_in_cart()
    print('Number of items in cart:', num_items)

    cart_cost = shopping_cart.get_cost_of_cart()
    print('Cost of cart: ${}'.format(cart_cost))


if __name__ == "__main__":
    main()