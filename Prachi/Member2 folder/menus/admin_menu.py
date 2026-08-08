from services.admin_service import admin_login
from menus.customer_menu import customer_menu

def admin_menu():

    while True:

        print("\n====================================")
        print("          ADMIN PANEL")
        print("====================================")
        print("1. Admin Login")
        print("2. Back")
        print("====================================")

        choice = input("Enter Your Choice : ")

        if choice == "1":

            if admin_login():

                while True:

                    print("\n====================================")
                    print("       BANK ADMIN DASHBOARD")
                    print("====================================")
                    print("1. Customer Management")
                    print("2. Account Management")
                    print("3. Transaction Management")
                    print("4. Reports")
                    print("5. Logout")
                    print("====================================")

                    admin_choice = input("Enter Your Choice : ")

                    if admin_choice == "1":
                        customer_menu()

                    elif admin_choice == "2":
                        print("\nAccount Management Module")
                        print("Coming Soon...")

                    elif admin_choice == "3":
                        print("\nTransaction Management Module")
                        print("Coming Soon...")

                    elif admin_choice == "4":
                        print("\nReports Module")
                        print("Coming Soon...")

                    elif admin_choice == "5":
                        print("\nAdmin Logout Successfully...")
                        break

                    else:
                        print("\nInvalid Choice!")

        elif choice == "2":
            break

        else:
            print("\nInvalid Choice!")