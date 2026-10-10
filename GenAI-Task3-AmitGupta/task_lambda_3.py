def apply_discount(x, discount=5):
    return x * (discount / 100)

# ----------------------------------------
# Task-3 Lambda function
gst = lambda price: price + (0.18 * price)
print(gst(100))

final_price = lambda x: apply_discount(x) + x

print(gst(1000))
print(final_price(gst(1000)))