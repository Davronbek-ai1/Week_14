items = ["Apple", "Banana", "Cherry"]
prices = [0.50, 0.30, 0.10]
quantities = [4, 2, 10]

total = 0
for x, (item, price, quantity) in enumerate(zip(items, prices, quantities), start=1):
    print(f"Line #{x}: {item} x{quantity} = ${price * quantity}")
    total += price * quantity
print("--------------------")
print(f"Grand Total: ${total}")