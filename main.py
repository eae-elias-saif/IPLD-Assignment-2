import random
import string

inventory = {
    # For dictionary management, the key will be the product_id, this is just a main example for 
    "A001": {
        "Name": "Iphone 13", 
        "Units": 15,
        "Price": 25.50,
        "Reorder_Level": 5
    },
    "B045": {
        "Name": "Samsung Galaxy s25", 
        "Units": 8,
        "Price": 12.00,
        "Reorder_Level": 10
    },
}

def add_product(product_stock):
    """Add a new product to the stock"""
    print("\n---ADD NEW PRODUCT TO STOCK---")
    
    while True:
        random_letter = random.choice(string.ascii_uppercase)
        random_number = random.randint(1000, 9999) 
        product_id = random_letter + str(random_number)
        if product_id not in product_stock:
            print(f"✅ Generated Product ID: {product_id}")
            break

    #Input product name and validates it
    product_name = input(f"Enter the name of the product: ").strip()
    
    #Input units and validates it
    while True:
        try:
            units = int(input("Enter how many units are in stock: "))
            if units >= 0:
                break
            else:
                print("❌ Units must be a positive integer or zero.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number for units.")
        
        #Input price and validates it
    while True:
        try:
            price_float = float(input("Enter the unit price of the product: "))
            price = round(price_float, 2) #rounding up to two decimals in case
            if price > 0:
                break
            else:
                    print("❌ Price can't be negative number.")
        except ValueError:
                print("❌ Invalid input. Please enter a numerical price.")
    #Prepare data for returning, assembling all variables into a dictionary called new_product_data
    new_product_data = {
        "Name": product_name,
        "Units": units,
        "Price": price
    }
    product_stock[product_id] = new_product_data
    print(f"\n📦 New product ID {product_id} added to the inventory!.")
    


#Menu like console interface (just like the example)

menu = """
╔════════════════════════════════════════╗
║      Inventory Management System       ║
╚════════════════════════════════════════╝

1. Add new product
2. Search for product
3. Reorder product
4. Exit (ctrl + c works too)

"""


#main menu function to handle all the features (Just copied the same approach of the professor)
def main_menu ():
     
    stock_item = {}
        
    while True:
          
        print(menu)

        user_option = input("Select an option (1-4): ")

        if user_option == '1':
            add_product(stock_item)
        elif user_option == '2':
             print('Lets add feature 2 instead of this print')
        elif user_option == '3':
             print('lets add feature 3 instead of this print')
        elif user_option == '4':
             print('bye bye!')
             break
        else:
             print('Invalid option! Please select 1-4')

main_menu()