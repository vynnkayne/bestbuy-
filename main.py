import products
import store

def start(store_obj):
    while True:
        print("Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.show())
        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")
        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter the product name (or 'q' to finish): ")
                if product_name == "q":
                    break

                quantity = int(input("Enter the quantity: "))
                product = None
                for prod in store_obj.products:
                    if prod.name == product_name:
                        product = prod
                        break

                if product is None:
                    print("Product not found.")
                elif quantity > product.get_quantity():
                    print("Not enough stock available.")
                else:
                    shopping_list.append((product, quantity))

            if shopping_list:
                order_total = store_obj.order(shopping_list)
                print(f"Order cost: {order_total} dollars.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)
    best_buy = store.Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()

