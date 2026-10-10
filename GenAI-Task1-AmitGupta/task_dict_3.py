#Task-3
price_dict = {"jeans":950, "pants":3000, "shirt":500, "t-shirt":545, "pajama":350, "belt":200}
# add new product
price_dict['watch'] = 4500

#update existing product
price_dict['belt'] = 140

try:
    del price_dict['be0lt']
except KeyError as e:
    print("product not found!")

#print the avg price of products..
product_avg = sum(price_dict.values())/ len(price_dict)

# max and min products
print(f"Max= {max(price_dict.values())} and Min={min(price_dict.values())}")
