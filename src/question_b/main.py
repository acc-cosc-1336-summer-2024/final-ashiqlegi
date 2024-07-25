# 1. The program continues until the user opts out.
# 2. Create the following menu:
#      1-Display stock purchase history
#      2-Exit
#      Option 1 calls the stock_purchase_history function.
#      Option 3 exits the program

from question_b import stock_purchase_history

def menu():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


menu()

