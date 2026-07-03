from enums.event_type import EventType
from models.product import Product
from src.display import print_history
from utils.option import choose_index

products: list[Product] = []
event_types: list[EventType] = list(EventType)


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
            id_: str = input("Enter the Product Id: ")
            id_repeated: bool = False

            for product in products:
                if product.id_ == id_:
                    print("A Product with this id already exist. Try again!")
                    id_repeated = True
                    break

            if id_repeated:
                continue

            name: str = input("Enter the Product name: ")

            if not id_ or not name:
                print("Description and register name cannot be empty!")
                continue

            products.append(Product(id_, name))

        elif option == "2":
            if not products:
                print("No Product registered. Add a Product to continue!")
                continue

            print("----Products----")
            product_index = choose_index(
                labels=[str(product) for product in products],
                prompt="Chose a Product to add a Event (or 0 to cancel): ",
            )

            if product_index is None:
                continue

            print("----Event Types----")
            event_index = choose_index(
                labels=[event.label for event in event_types],
                prompt="Chose an Event type (or 0 to cancel): ",
            )

            if event_index is None:
                continue

            event_type: EventType = event_types[event_index]

            description: str = input("Enter the Event description: ").strip()
            registered_by: str = input("Enter whose registering: ").strip()

            if not description or not registered_by:
                print("Decription and register name cannot be empty!")
                continue

            products[product_index].add_event(
                event_type, description, registered_by
            )
            print("Event added successfully!")

        elif option == "3":
            if not products:
                print("No Product registered. Add a Product to continue!")
                continue

            print("----Products----")
            for product in products:
                print_history(product)

        elif option == "4":
            break

        else:
            print(f"{option} is not a valid option. Try again!")
