def linear_search_product(product_list, target_product_name):
    indices = []
    for index, product in enumerate(product_list):
        if product["name"] == target_product_name:
            indices.append(index)
    return indices
if __name__ == "__main__":
    products = [
        {"name": "Product A", "price": 10.99},
        {"name": "Product B", "price": 19.99},
        {"name": "Product A", "price": 15.99},
        {"name": "Product C", "price": 25.99},
        {"name": "Product A", "price": 12.99},
    ]

    target_product_name = "Product A"
    result_indices = linear_search_product(products, target_product_name)

    if result_indices:
        print(f"The target product '{target_product_name}' was found at indices: {result_indices}")
    else:
        print(f"The target product '{target_product_name}' was not found in the list.")