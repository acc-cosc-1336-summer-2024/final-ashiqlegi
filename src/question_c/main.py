#add import

from question_c import create_multiplication_table, display_multiplication_table
def main():
    while True:
       multiplication_table = create_multiplication_table()
       display_multiplication_table(multiplication_table)
        

       user_input = input("Do you want to display the multiplication table again? (type 'yes' to continue or 'no' to quit): ").strip().lower()
       if user_input != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()