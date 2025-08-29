def calculate_discount(price, discount_percent):
    """
    Calculate final price after discount.
    If discount >= 20%, apply it.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# --- Main Program ---
try:
    # Get inputs from user
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount)

    # Show result
    if discount >= 20:
        print(f"✅ Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"⚠ No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("❌ Please enter valid numbers for price and discount.")