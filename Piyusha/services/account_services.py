from database.db import conn, cursor
from models.account import Account


# ---------------- OPEN ACCOUNT ---------------- #

def open_account():

    customer_id = int(input("Enter Customer ID : "))
    account_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Opening Balance : "))
    opening_date = input("Enter Opening Date (YYYY-MM-DD): ")

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

    account_no = int(input("Enter Account Number : "))

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

    account_no = int(input("Enter Account Number : "))

    query = "SELECT * FROM account WHERE account_no=%s"

    cursor.execute(query, (account_no,))

    data = cursor.fetchone()

    if data is None:

        print("Account Not Found")
        return

    account_type = input("Enter New Account Type : ")

    balance = float(input("Enter New Balance : "))

    status = input("Enter Status (Active/Frozen/Closed): ")

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

    account_no = int(input("Enter Account Number : "))

    query = """
    UPDATE account
    SET account_status='Closed'
    WHERE account_no=%s
    """

    cursor.execute(query, (account_no,))

    conn.commit()

    print("\nAccount Closed Successfully\n")
