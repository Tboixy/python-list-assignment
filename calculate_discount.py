# Function to calculate final price after applying discount
def calculate_discount(price, discount_percent):
    # Apply discount only if it is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount)

    # Display result
    if discount >= 20:
        print(f"Final price after {discount}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
