# Define a class to represent individual items to purchase
class ItemToPurchase:
    # Constructor to initialize item name, price, quantity, and description
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    # Method to print item cost in the desired format
    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}'

    # Method to print item description
    def print_item_description(self):
        return f'{self.item_name}: {self.item_description}'

# Define a class to represent the shopping cart
class ShoppingCart:
    # Constructor to initialize customer name, current date, and empty item list
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # List to store items added to the cart

    # Method to add an item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the cart by name
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print('Item is not in the cart, nothing removed.')

    # Method to modify an item in the cart
    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                found = True
                # Update description if not default
                if item.item_description != 'none':
                    cart_item.item_description = item.item_description
                # Update price if not default
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                # Update quantity if not default
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                break
        if not found:
            print('Item is not in the cart, nothing modified.')

    # Method to return the total number of items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Method to return the total cost of all items in the cart
    def get_cost_of_cart(self):
        return sum(item.item_quantity * item.item_price for item in self.cart_items)

    # Method to print the total cart including each item and overall cost
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(item.print_item_cost())
            print(f'Total: ${self.get_cost_of_cart()}')

    # Method to print descriptions of all items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions')
        for item in self.cart_items:
            print(item.print_item_description())

# Function to display the menu and handle user input for actions on the cart
def print_menu(cart):
    while True:
        # Menu options displayed
        print('\nMENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')

        choice = input('Choose an option: ')

        # Handle each menu option
        if choice == 'q':
            break
        elif choice == 'a':
            # Input item details
            name = input('Enter item name: ')
            description = input('Enter item description: ')
            price = float(input('Enter item price: '))
            quantity = int(input('Enter item quantity: '))
            # Create item and add to cart
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == 'r':
            name = input('Enter name of item to remove: ')
            cart.remove_item(name)
        elif choice == 'c':
            # Input new item data
            name = input('Enter name of item to modify: ')
            description = input('Enter new description (or leave blank to keep current): ') or 'none'
            price = input('Enter new price (or leave blank to keep current): ')
            quantity = input('Enter new quantity (or leave blank to keep current): ')

            # Convert inputs if not blank
            price = float(price) if price else 0
            quantity = int(quantity) if quantity else 0

            # Create temporary item to pass to modify method
            item = ItemToPurchase(name, price, quantity, description)
            cart.modify_item(item)
        elif choice == 'i':
            # Print item descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            # Print shopping cart summary
            print('\nOUTPUT SHOPPING CART')
            cart.print_total()
        else:
            print('Invalid option, please try again.')

# Main function to start the program
def main():
    # Gather initial customer information
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    # Create a shopping cart object
    cart = ShoppingCart(customer_name, current_date)
    # Display the menu and start interaction
    print_menu(cart)

# Program entry point
if __name__ == '__main__':
    main()


