msg = '''
    Menu options:
        1 -- Add order amount to a running list
        2 -- Show all orders and total after applying discount
        q -- Quit
    '''
order_list= []
final_amount = 0
discount = 0

while True:
    try:
        print(f"{msg} \n")
        menu_option = (input("Select any one option from menu: "))
        # discount 15%
        if( menu_option == "1"):
            order_amount = int(input('enter order amount: '))
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
        
            order_list.append(final_amount)
            continue

        elif (menu_option == "2"):
            print(f"all orders after applying discount : {order_list}")
            break

        elif (menu_option == 'q'):
            break
      
    except ValueError as e:
        print("amount should be an interger value")
        continue

