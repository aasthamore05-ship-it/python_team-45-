from Database.db import connection


# ---------------- ADMIN LOGIN ----------------

def admin_login():

    conn = connection()
    cursor = conn.cursor()

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    sql = """
    SELECT *
    FROM admin
    WHERE username=%s AND password=%s
    """

    cursor.execute(sql, (username, password))

    admin = cursor.fetchone()

    conn.close()

    if admin:

        print("\n====================================")
        print("     LOGIN SUCCESSFUL")
        print("Welcome,", admin[1])
        print("====================================")

        return True

    else:

        print("\n====================================")
        print("Invalid Username or Password")
        print("====================================")

        return False