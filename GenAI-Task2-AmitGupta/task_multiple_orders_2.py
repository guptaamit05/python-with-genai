try:
    orders = [1200, 2500, 800, 1750, 3000]
    total_revenue = 0
    orders_with_discount = []
    for order_amount in orders:

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

        if discount:
            orders_with_discount.append(order_amount)

        total_revenue += final_amount
        
        print(f"order_amount: {order_amount} -> discount% {discount} ->  final_amount: {final_amount}")
    
    print(f"total revenue: {total_revenue}")
    print(f"number of orders that received a discount: {orders_with_discount}")

except Exception as e:
    print(f"something went wrong: {e}")

