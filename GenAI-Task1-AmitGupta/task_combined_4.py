products = ['shirt','t-shirt', 'kurtas', 'jeans', 'kurtas']
price_dict = {"jeans":950, "pants":3000, "shirt":500, "t-shirt":545, "pajama":350, "belt":200}

# Task-4
catelog =[]
for product, price, category in zip(products, price_dict.values(), price_dict.keys()):
    catelog.append((product, price, category))

print(f"catelog: {catelog}")

category_to_products = {}
for item in catelog:
    if item[0] in category_to_products:
        category_to_products[item[0]].append(item[2])
    else:
        category_to_products[item[0]] = [item[2]]

print(category_to_products)


max_category = max(category_to_products, key=lambda x :len(category_to_products[x]))
print(max_category)
print(category_to_products[max_category])