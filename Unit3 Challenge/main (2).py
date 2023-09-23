def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
products = ["apple", "banana", "apple", "orange", "apple"]
target = "apple"
result = linear_search_product(products, target)
print("Indices of '{}' in the list: {}".format(target, result))
