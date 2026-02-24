total_cost=0.00
for i in range(1, 6):
    price = float(input(f"Enter price of item {i}: "))
    quantity = int(input(f"Enter quantity of item {i}: "))
    
    item_cost = price * quantity
    total_cost += item_cost

print("\nOriginal Total Amount: Rs.", total_cost)

discount = 0.0

if total_cost > 100:
    discount = total_cost * 0.10
    print("Discount Applied (10%): Rs.", discount)
else:
    print("No Discount Applied")

final_amount = total_cost - discount

print("Final Amount to Pay: Rs.", final_amount)