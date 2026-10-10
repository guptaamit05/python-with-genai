prices = [100, 250, 400, 1200, 50]

gst = lambda price: price + (0.18 * price)

def price_with_gst(amount):
    return gst(amount)

prices_with_gst = list(map(price_with_gst, prices))

print(f"Original prices: {prices}")
print(f"Prices after GST: {prices_with_gst}")