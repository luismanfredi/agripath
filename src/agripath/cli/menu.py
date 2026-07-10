from agripath.cli.display import print_history
from agripath.db.repository import (
    add_event_to_product,
    get_all_products,
    get_product,
    save_product,
)
from agripath.enums.event_type import EventType
from agripath.models.event import Event
from agripath.models.product import Product
from agripath.utils.prompt import choose_index
from agripath.utils.separator import separator

EVENT_TYPES: list[EventType] = list(EventType)


def menu() -> None:
    separator()
    print("Welcome to AgriPath!")
    while True:
        separator()
        print("1. Add a Product")
        print("2. Add an Event to a Product")
        print("3. Show Products")
        print("4. Show Events of a Product")
        print("5. Quit")
        separator()
        option: str = input("Which option would you like to use? ").strip()
        separator()

        if option == "1":
            id_: str = input("Enter the Product Id: ").strip()
            name: str = input("Enter the Product name: ").strip()

            if not id_ or not name:
                separator()
                print("Product Id and name cannot be empty!")
                continue

            save_product(Product(id_, name))

            separator()
            print("Product saved successfully!")

        elif option == "2":
            product_id: str = input("Enter the Product Id: ").strip()

            product: Product | None = get_product(product_id)

            if product is None:
                separator()
                print(f"Product with id '{product_id}' was not found.")
                continue

            print("----Event Types----")
            event_index = choose_index(
                labels=[event.label for event in EVENT_TYPES],
                prompt="Chose an Event type (or 0 to cancel): ",
            )

            if event_index is None:
                separator()
                print(f"Index {event_index} is invalid.")
                continue

            event_type: EventType = EVENT_TYPES[event_index]

            description: str = input("Enter the Event description: ").strip()
            registered_by: str = input("Enter whose registering: ").strip()

            if not description or not registered_by:
                separator()
                print("Decription and register name cannot be empty!")
                continue

            add_event_to_product(
                product_id, Event(event_type, description, registered_by)
            )

            separator()
            print("Event added successfully!")

        elif option == "3":
            products: list[Product] = get_all_products()
            if not products:
                separator()
                print("No Products found.")
                continue

            print("----Products----")
            for product in products:
                print(product)

        elif option == "4":
            product_id = input("Enter the Product Id: ").strip()

            product = get_product(product_id)

            if product is None:
                separator()
                print(f"Product with id '{product_id}' was not found.")
                continue

            separator()
            print_history(product)
        elif option == "5":
            break
        else:
            print(f"{option} is not a valid option. Try again!")
