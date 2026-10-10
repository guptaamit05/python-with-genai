# Task-6
def process_prices(prices):

    discounted_price = list(map(lambda x: x + x * 0.10, prices))
    filtered_price = list(filter(lambda x: x > 300, discounted_price))
    print(f"Pricess after 10% discount: {discounted_price}")
    print(f"Discounted pricess>300: {filtered_price}")

process_prices([100, 500, 900, 50, 750])
