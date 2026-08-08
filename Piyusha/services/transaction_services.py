from database.db import conn, cursor


def get_account_number(prompt="Enter Account Number : "):
    while True:
        account_input = input(prompt).strip()
        try:
            return int(account_input)
        except ValueError:
            print("Account Number must be a valid number")


# ---------------- VIEW TRANSACTIONS ---------------- #

def view_transactions():

    query = """
    SELECT * FROM transactions
    ORDER BY transaction_date DESC
    """

    cursor.execute(query)

    data = cursor.fetchall()

    if len(data) == 0:
        print("\nNo Transactions Found\n")
        return

    print("\n========== TRANSACTION LIST ==========\n")

    for row in data:

        print("Transaction ID      :", row[0])
        print("Account No          :", row[1])
        print("Transaction Type    :", row[2])
        print("Amount              :", row[3])
        print("Charge              :", row[4])
        print("Balance After Txn   :", row[5])
        print("Remarks             :", row[6])
        print("Transaction Date    :", row[7])
        print("--------------------------------------")
        # ---------------- SEARCH TRANSACTION ---------------- #

def search_transaction():

    account_no = get_account_number()

    query = """
    SELECT * FROM transactions
    WHERE account_no=%s
    """

    cursor.execute(query, (account_no,))

    data = cursor.fetchall()

    if len(data) == 0:

        print("\nNo Transaction Found\n")
        return

    print("\n===== TRANSACTION HISTORY =====\n")

    for row in data:

        print("Transaction ID      :", row[0])
        print("Account No          :", row[1])
        print("Transaction Type    :", row[2])
        print("Amount              :", row[3])
        print("Charge              :", row[4])
        print("Balance After Txn   :", row[5])
        print("Remarks             :", row[6])
        print("Transaction Date    :", row[7])
        print("--------------------------------------")