#Task-2
products = ['shirt','t-shirt', 'kurtas', 'jeans', 'kurtas']

categories = set(products)
print(categories)

#duplicate ignored
categories.add("jeans")
print(f"updated categories have still same length: {categories}")

# category exist or not
print( 'jeans' in categories)  # True 
print( 'mobile' in categories)  # False

# total unique cateogries
print(f"total number of categories: {len(categories)}")
