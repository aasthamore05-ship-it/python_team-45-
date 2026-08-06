class Transaction:

    def __init__(self,
                 transaction_id,
                 account_no,
                 transaction_type,
                 amount,
                 charge,
                 balance_after_transaction,
                 remarks,
                 transaction_date):

        self.transaction_id = transaction_id
        self.account_no = account_no
        self.transaction_type = transaction_type
        self.amount = amount
        self.charge = charge
        self.balance_after_transaction = balance_after_transaction
        self.remarks = remarks
        self.transaction_date = transaction_date