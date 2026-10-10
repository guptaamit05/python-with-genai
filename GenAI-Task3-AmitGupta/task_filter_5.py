prices = [100, 250, 400, 1200, 50, 2000, 850]

def greater_than_500(num):
    if num > 500:
        return num

def less_than_500(num):
    if num <= 500:
        return num

greater_500 = list(filter(greater_than_500, prices))
lessthan_500 = list(filter(less_than_500, prices))

print(f"Greater than 500: {greater_500}")
print(f"Less than than 500: {lessthan_500}")