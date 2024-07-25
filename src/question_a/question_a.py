def test_config():
    return True

def input_values(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"The lowest number is: {lowest}")
    print(f"The highest number is: {highest}")
    print(f"The total of the numbers is: {total}")
    print(f"The average of the numbers is: {average}")