from services.customer_service import (
    add_customer,
    view_customers,
    search_customer,
    update_customer,
    delete_customer
)


def customer_menu():

    while True:

        print("\n====================================")
        print("      CUSTOMER MANAGEMENT")
        print("====================================")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back")
        print("====================================")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            update_customer()

        elif choice == "5":
            delete_customer()

        elif choice == "6":
            break

        else:
            print("\nInvalid Choice!")