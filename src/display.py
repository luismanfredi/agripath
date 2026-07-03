from models.product import Product


def print_history(product: Product):
    print(product)
    for item in product.events:
        print(item)
