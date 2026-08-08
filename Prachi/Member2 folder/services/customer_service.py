from database.db import conn, cursor
from models.customer import Customer


# ---------------- ADD CUSTOMER ----------------

def add_customer():

    first_name = input("Enter First Name : ")
    last_name = input("Enter Last Name : ")
    dob = input("Enter DOB (YYYY-MM-DD) : ")
    gender = input("Enter Gender (Male/Female/Other) : ")
    mobile = input("Enter Mobile : ")
    email = input("Enter Email : ")
    password = input("Enter Password : ")

    customer = Customer(
        first_name,
        last_name,
        dob,
        gender,
        mobile,
        email,
        password
    )

    query = """
    INSERT INTO customer
    (first_name,last_name,DOB,Gender,mobile,email,password)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        customer.first_name,
        customer.last_name,
        customer.dob,
        customer.gender,
        customer.mobile,
        customer.email,
        customer.password
    )

    cursor.execute(query, values)
    conn.commit()

    print("Customer Added Successfully")


# ---------------- VIEW CUSTOMER ----------------

def view_customer():

    query = "SELECT * FROM customer"

    cursor.execute(query)

    customers = cursor.fetchall()

    print("\n================ CUSTOMER LIST ================\n")

    for customer in customers:
        print(customer)


# ---------------- SEARCH CUSTOMER ----------------

def search_customer():

    customer_id = int(input("Enter Customer ID : "))

    query = "SELECT * FROM customer WHERE customer_id=%s"

    cursor.execute(query, (customer_id,))

    customer = cursor.fetchone()

    if customer:
        print(customer)
    else:
        print("Customer Not Found")


# ---------------- UPDATE CUSTOMER ----------------

def update_customer():

    customer_id = int(input("Enter Customer ID : "))

    mobile = input("Enter New Mobile Number : ")

    query = """
    UPDATE customer
    SET mobile=%s
    WHERE customer_id=%s
    """

    cursor.execute(query, (mobile, customer_id))
    conn.commit()

    print("Customer Updated Successfully")


# ---------------- DELETE CUSTOMER ----------------

def delete_customer():

    customer_id = int(input("Enter Customer ID : "))

    query = "DELETE FROM customer WHERE customer_id=%s"

    cursor.execute(query, (customer_id,))
    conn.commit()

    print("Customer Deleted Successfully")