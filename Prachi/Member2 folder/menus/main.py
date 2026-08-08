from menus.admin_menu import admin_menu

def main():

    while True:

        print("\n======================================")
        print("     BANK MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Admin Panel")
        print("2. Exit")
        print("======================================")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            admin_menu()

        elif choice == "2":
            print("\nThank You...")
            break

        else:
            print("\nInvalid Choice!")

if __name__ == "__main__":
    main()