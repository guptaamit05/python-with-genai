try:
    order_amount = int(input("enter order amount: "))
    final_amount = 0
    discount = 0
    # discount 15%
    if order_amount >=2000:
        discount = 0.15
        discounted_amount = order_amount * discount
        final_amount = order_amount- discounted_amount

    # discount 10%
    elif (order_amount >= 1500 and order_amount < 2000):
        discount = 0.10
        discounted_amount = order_amount * discount
        final_amount = order_amount - discounted_amount

    # discount 7%
    elif (order_amount >= 1000 and order_amount < 1500):
        discount = 0.07
        discounted_amount = order_amount * discount
        final_amount = order_amount - discounted_amount

    # discount 0%
    else:
        discounted_amount = order_amount * discount
        final_amount = order_amount - discounted_amount

    print(f"Final Amount: {final_amount}")

    ## Extra
    tax = 0.05   # tax 5%
    subtotal = final_amount * tax   # taxable amount
    # final total after tax
    final_total = final_amount-subtotal
    print(f"subtotal: {subtotal}, \ntax:{tax}%  \nfinal total: {final_total}")

except ValueError as e:
    print("amount should be an interger value")


