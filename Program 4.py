def count_multiples(input_list):
    result = {i: 0 for i in range(1, 10)}
    for number in input_list:
        for key in result:
            if number % key == 0:
                result[key] += 1
    return result

# Example usage
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(input_list))
