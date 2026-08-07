from services.customer_services import *

def admin_menu():

    while True:

        print("\n======================================")
        print("     CUSTOMER MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Exit")
        print("======================================")

        choice = int(input("Enter Your Choice : "))

        match choice:

            case 1:
                add_customer()

            case 2:
                view_customer()

            case 3:
                search_customer()

            case 4:
                update_customer()

            case 5:
                delete_customer()

            case 6:
                print("Thank You")
                break

            case _:
                print("Invalid Choice")