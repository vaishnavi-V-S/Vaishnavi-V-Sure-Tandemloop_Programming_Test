def generate_series(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 == 1:  # Only add odd numbers
            series.append(i)
    return series

# Example usage
a = int(input("Enter an integer: "))
print(generate_series(a))

