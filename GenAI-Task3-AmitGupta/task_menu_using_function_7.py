# Task-7
def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list) if len(prices_list) > 0 else None

def get_max_price(prices_list):
    return max(prices_list) if len(prices_list) > 0 else None

msg = """
    Menu:
        1 -> add price
        2 -> show average price
        3 -> show highest price
        q -> Quit
"""
prices_list = []
while True:
    try:
        # print menu
        print(msg)
        # get user input
        user_input = input("Select one option from menu:")

        # add price in prices_list
        if user_input == "1":
            price = int(input("enter price: "))
            if price <0:
                print("Price can not be negative")
                continue
            add_price(prices_list, price)
            print(f"Item added. New list is : {prices_list}")
            continue

        # get average price
        if user_input == "2":
            print(f"Average price is: {get_average_price(prices_list)}")
            continue

        # get highest price
        elif user_input == "3":
            print(f"Highest price is: {get_max_price(prices_list)}")
            continue

        # Quit the loop
        elif user_input == "q":
            print(f"Final prices list: {prices_list}")
            break
        else:
            print("Invalid option: Please select 1,2,3, or q.")

    except Exception as e:
        print(f"Error: {e}")
        continue