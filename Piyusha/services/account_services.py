from datetime import datetime

from database.db import conn, cursor
from models.account import Account


def validate_account_type(account_type):
    valid_types = {"savings", "current"}
    if account_type.lower() not in valid_types:
        raise ValueError("Account type must be Savings or Current")
    return account_type.title()


def validate_balance(balance):
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    return balance


def validate_status(status):
    valid_statuses = {"active", "frozen", "closed"}
    if status.lower() not in valid_statuses:
        raise ValueError("Status must be Active, Frozen, or Closed")
    return status.title()


def validate_opening_date(opening_date):
    try:
        parsed_date = datetime.strptime(opening_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Opening date must be in YYYY-MM-DD format")
    return parsed_date.strftime("%Y-%m-%d")


def get_int_input(prompt="Enter Number : "):
    while True:
        input_value = input(prompt).strip()
        try:
            return int(input_value)
        except ValueError:
            print("Input must be a valid number")


# ---------------- OPEN ACCOUNT ---------------- #

def open_account():

    customer_id = get_int_input("Enter Customer ID : ")

    customer_check_query = "SELECT customer_id FROM customer WHERE customer_id=%s"
    cursor.execute(customer_check_query, (customer_id,))
    if cursor.fetchone() is None:
        print("\nCustomer Not Found. Cannot open account.\n")
        return

    account_exists_query = "SELECT account_no FROM account WHERE customer_id=%s"
    cursor.execute(account_exists_query, (customer_id,))
    if cursor.fetchone() is not None:
        print("\nThis customer already has an account. Cannot open another account under the current schema.\n")
        return

    while True:
        try:
            account_type = validate_account_type(input("Enter Account Type (Savings/Current): ").strip())
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            balance = validate_balance(float(input("Enter Opening Balance : ")))
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            opening_date = validate_opening_date(input("Enter Opening Date (YYYY-MM-DD): ").strip())
            break
        except ValueError as e:
            print(e)

    account = Account(
        None,
        customer_id,
        account_type,
        balance,
        "Active",
        opening_date
    )

    query = """
    INSERT INTO account
    (customer_id, account_type, balance, account_status, opening_date)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        account.customer_id,
        account.account_type,
        account.balance,
        account.account_status,
        account.opening_date
    )

    cursor.execute(query, values)
    conn.commit()

    print("\nAccount Opened Successfully.\n")


# ---------------- VIEW ACCOUNT ---------------- #

def view_account():

    query = "SELECT * FROM account"

    cursor.execute(query)

    data = cursor.fetchall()

    if len(data) == 0:
        print("\nNo Account Found\n")
        return

    print("\n----------- ACCOUNT LIST -----------")

    for row in data:

        print("Account No      :", row[0])
        print("Customer ID     :", row[1])
        print("Account Type    :", row[2])
        print("Balance         :", row[3])
        print("Status          :", row[4])
        print("Opening Date    :", row[5])
        print("-----------------------------------")
        # ---------------- SEARCH ACCOUNT ---------------- #

def search_account():

    account_no = get_int_input()

    query = "SELECT * FROM account WHERE account_no=%s"

    cursor.execute(query, (account_no,))

    data = cursor.fetchone()

    if data:

        print("\nAccount Found\n")

        print("Account No   :", data[0])
        print("Customer ID  :", data[1])
        print("Account Type :", data[2])
        print("Balance      :", data[3])
        print("Status       :", data[4])
        print("Opening Date :", data[5])

    else:

        print("\nAccount Not Found\n")
        # ---------------- UPDATE ACCOUNT ---------------- #

def update_account():

    account_no = get_int_input()

    query = "SELECT * FROM account WHERE account_no=%s"

    cursor.execute(query, (account_no,))

    data = cursor.fetchone()

    if data is None:

        print("Account Not Found")
        return

    while True:
        try:
            account_type = validate_account_type(input("Enter New Account Type (Savings/Current): ").strip())
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            balance = validate_balance(float(input("Enter New Balance : ")))
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            status = validate_status(input("Enter Status (Active/Frozen/Closed): ").strip())
            break
        except ValueError as e:
            print(e)

    update_query = """
    UPDATE account
    SET account_type=%s,
        balance=%s,
        account_status=%s
    WHERE account_no=%s
    """

    values = (
        account_type,
        balance,
        status,
        account_no
    )

    cursor.execute(update_query, values)

    conn.commit()

    print("\nAccount Updated Successfully\n")
    # ---------------- CLOSE ACCOUNT ---------------- #

def close_account():

    account_no = get_int_input()

    check_query = "SELECT account_status FROM account WHERE account_no=%s"
    cursor.execute(check_query, (account_no,))
    existing = cursor.fetchone()

    if existing is None:
        print("Account Not Found")
        return

    if existing[0].lower() == "closed":
        print("\nAccount is already closed\n")
        return

    query = """
    UPDATE account
    SET account_status='Closed'
    WHERE account_no=%s
    """

    cursor.execute(query, (account_no,))

    conn.commit()

    print("\nAccount Closed Successfully\n")
