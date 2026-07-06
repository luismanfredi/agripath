from agripath.models.product import Product


def print_history(product: Product) -> None:
    print(product)
    for item in product.events:
        print(item)
