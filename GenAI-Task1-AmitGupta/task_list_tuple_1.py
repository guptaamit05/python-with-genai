#Task-1 
products = ['shirt','t-shirt', 'kurtas', 'jeans', 'kurtas']
sample_product = ("shirt", 500, 'mens-wear')
print(f"first product: {products[1]}, and last product: {products[-1]}")

products.append("pajama")
products.append('polo-shirt')

print(f"updated products: {products}")

changed_tuple = list(sample_product)
changed_tuple[1] = 1000

original_tuple = tuple(changed_tuple)
print(f"original tuple: {original_tuple}")
