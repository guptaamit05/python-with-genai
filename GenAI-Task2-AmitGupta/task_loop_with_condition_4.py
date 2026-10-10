daily_sales = [200, 150, 0, 400,50, -1, 300]
total_sales = 0
for sale in daily_sales:
    if sale == -1:
        print("stopped due to corrupted data")
        break
    if sale == 0:
        print("no sales")
        continue
    total_sales +=sale
    print(f"running total: {total_sales}")

print(f"Final Total: {total_sales}")