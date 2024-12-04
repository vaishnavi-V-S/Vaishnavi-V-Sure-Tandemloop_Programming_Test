def generate_odd_series(a):
    return [2 * i - 1 for i in range(1, a + 1)]

# Example usage
a = int(input("Enter an integer: "))
print(generate_odd_series(a))
