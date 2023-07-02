# OnlineShoppingCart
 Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps.

Parameterized constructor which takes the customer name and date as parameters (2 pts)
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2016"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's quantity. Has parameter ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart() (2 pts)
Returns quantity of all items in cart. Has no parameters.
get_cost_of_cart() (2 pts)
Determines and returns the total cost of items in cart. Has no parameters.
print_total()
Outputs total of objects in cart.
If cart is empty, output this message: SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description.
