def apply_discount(price, discount_percent = 5):

    # early return condition
    if discount_percent > 60 or discount_percent < 0:
        return price
    
    # calculate discounted_value
    discounted_value = price* (discount_percent/100)

    # return price after apply discount
    final_value = price-discounted_value

    return final_value

print(apply_discount(1000, 10))
print(apply_discount(500))