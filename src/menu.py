from models.product import Product

products: list[Product] = []


def menu() -> None:
    print("-" * 40)
    print("Welcome to AgriPath!")
    while True:
        print("-" * 40)
        print("1. Add a Product")
        print("2. Add an Event to a Product")
        print("3. Show Products and Events")
        print("4. Quit")
        print("-" * 40)
        option: str = input("Which option would you like to use? ").strip()
        print("-" * 40)

        if option == "1":
            id_ = input("Enter the Product Id: ")
            name = input("Enter the Product name: ")

            if not id_ or not name:
                print("Decription and register name cannot be empty!")
                continue

            products.append(Product(id_, name))

        elif option == "2":
            if not products:
                print("No Product registered. Add a Product to continue!")
                continue

            print("\n----Products----")
            for index, product in enumerate(products):
                print(f"{index + 1}. {product}")
            print("-" * 40)

            user_input: str = input("Chose a Product to add a Event (or 0 to cancel): ")
            print("-" * 40)

            if user_input == "0":
                print("Operation cancelled.")
                continue

            try:
                chosen_product = int(user_input)
            except ValueError:
                print(f"{user_input} is not a valid number. Please try again.")
                continue

            if not (1 <= chosen_product <= len(products)):
                print(
                    f"Product not found! Choose a number between 1 and {len(products)}!"
                )
                continue

            description: str = input("Enter the Event description: ").strip()
            registered_by: str = input("Enter whose registering: ").strip()

            if not description or not registered_by:
                print("Decription and register name cannot be empty!")
                continue

            products[chosen_product - 1].add_event(description, registered_by)
            print("Event added successfully!")

        elif option == "3":
            if not products:
                print("No Product registered. Add a Product to continue!")
                continue

            print("----Products----")
            for product in products:
                product.print_history()

        elif option == "4":
            break

        else:
            print(f"{option} is not a valid option. Try again!")
