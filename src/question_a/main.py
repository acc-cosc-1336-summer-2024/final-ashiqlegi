#add import
from question_a import input_values
def get_numbers():
    numbers = []
    for i in range(5):
        while True:
            try:
                num = float(input(f"Please enter a number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return numbers

numbers = get_numbers()
input_values(numbers)