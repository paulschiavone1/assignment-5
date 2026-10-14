# pos_checkout.py

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

subtotal = 0.0
units = 0

while True:
    item_name = input("Item name (or DONE): ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == "":
        print("Item name cannot be blank.")
        continue

    while True:
        try:
            price = float(input("Unit price: "))
            if price > 0:
                break
            print("Price must be greater than 0.")
        except ValueError:
            print("Enter a valid price.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity >= 1:
                break
            print("Quantity must be at least 1.")
        except ValueError:
            print("Enter a valid whole number.")

    subtotal = subtotal + price * quantity
    units = units + quantity

if units >= 10 or subtotal >= 100:
    discount_percent = 10
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100
total = subtotal - discount

if seed % 2 == 1:
    total = total - 3.00
    perk_applied = "YES"
else:
    perk_applied = "NO"

if total < 0:
    total = 0.00

print("Seed:", seed)
print("Units:", units)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print("Perk applied:", perk_applied)
print(f"Total: ${total:.2f}")