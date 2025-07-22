def arithmetic_operations(a, b, c):
    print("Starting complex arithmetic calculations...\n")

    # Mixed arithmetic expression
    result1 = a + b * c
    print(f"{a} + {b} * {c} = {result1} (Multiplication before addition)")

    # Parentheses to change order
    result2 = (a + b) * c
    print(f"({a} + {b}) * {c} = {result2} (Parentheses change the order)")

    # Floor division and modulus
    floor_div = a // b
    remainder = a % b
    print(f"{a} // {b} = {floor_div} (Floor Division)")
    print(f"{a} % {b} = {remainder} (Modulus / Remainder)")

    # A compound formula
    result3 = ((a + c) % b) * c - (a // c)
    print(f"Complex Expression: (({a} + {c}) % {b}) * {c} - ({a} // {c}) = {result3}")

    # Conditional check based on values
    if remainder == 0:
        print(f"\n{a} is evenly divisible by {b}")
    else:
        print(f"\n{a} is NOT evenly divisible by {b}, remainder is {remainder}")

    return result1, result2, result3


# Assign values
x = 10
y = 3
z = 2

# Call function
arithmetic_operations(x, y, z)
