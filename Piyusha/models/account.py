class Account:

    def __init__(self, account_no, customer_id, account_type,
                 balance, account_status, opening_date):

        self.account_no = account_no
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance
        self.account_status = account_status
        self.opening_date = opening_date