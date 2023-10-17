import datetime
import time
import sys

class CustomException(Exception):
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)
users = dict()
class User:
    next_account_number = 10000000

    def __init__(self):
        self.__balance = 0
        self.__user_info = dict()
        self.__user_info['balance'] = 0
        self.__transaction_info = dict()
        self.__loan_cnt = 0
        self.__loan_amount = 0


    def create_account(self, account_type,email,address):
        """
        The function creates a new user account with the specified account type, email, and address.
        
        :param account_type: The account type of the user (e.g., savings, checking, credit card, etc.)
        :param email: The email parameter is a string that represents the email address of the user
        creating the account
        :param address: The address parameter is used to store the address of the user when creating an
        account
        """
        User.next_account_number +=1
        self.__account_type = account_type
        self.__email = email
        self.__address = address
        self.__account_number = User.next_account_number
        self.__user_info['email'] = self.__email
        self.__user_info['account_type'] = self.__account_type
        self.__user_info['address'] = self.__address
        self.__user_info['account_no'] = self.__account_number
        users[self.__account_number] = self.__user_info


    def check_balance(self):
        print(f"Your Account Balance is {self.__balance}")
    

    def withdraw(self, amount):
        """
        The function withdraws a specified amount from the user's balance and updates the user's
        information and transaction history.
        
        :param amount: The amount parameter represents the amount of money that the user wants to
        withdraw from their account
        """
        if amount > self.__balance:
            print("Withdrawal amount exceeded")
        elif amount < 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        else:
            self.__balance -= amount
            self.__user_info['balance'] = self.__balance
            self.__transaction_info[datetime.datetime.now()] = {
                'Withdraw' : amount
            }
        users[self.__account_number] = self.__user_info
        time.sleep(0.5)
    
    def deposit(self, amount):
        """
        The `deposit` function increases the balance of a user's account, updates the user's information
        and transaction history, and prints a message confirming the deposit amount.
        
        :param amount: The amount parameter represents the amount of money that is being deposited into
        the account
        """

        if amount <0:
            raise ValueError("Amount must be greater than zero")

        self.__balance += amount
        self.__user_info['balance'] = self.__balance
        self.__transaction_info[datetime.datetime.now()] = {
            'Deposit' : amount
        }
        users[self.__account_number] = self.__user_info
        print(f"{amount} TK has been Deposited")
        time.sleep(0.5)
        
    def check_transaction_history(self):
        """
        The function `check_transaction_history` prints the transaction history of an account, including
        deposits, withdrawals, and loans.
        """
        print("Your transaction history : ")
        for transaction_time , transaction_amount in self.__transaction_info.items():
            transaction_type = list(transaction_amount.keys())[0]

            if transaction_type == 'Deposit':
                print(f"Your Account has been deposited {transaction_amount[transaction_type]} TK at {transaction_time}")
            elif transaction_type == 'Withdraw':
                print(f"Your Account has been withdrawn {transaction_amount[transaction_type]} TK at {transaction_time}")
            else:
                print(f"Your have taken a loan of {transaction_amount[transaction_type]} TK at {transaction_time}")
            
    def take_loan(self,amount):
        """
        The `take_loan` function allows a user to take a loan, but restricts them from taking more than
        two loans at a time.
        
        :param amount: The amount parameter represents the amount of money that the user wants to borrow
        as a loan
        """
        self.__loan_cnt +=1
        if self.__loan_cnt > 2:
            print("You are not allowed to take loan untill repay the previous loans.")
        else:
            self.__loan_amount +=amount
            self.__balance += amount
            self.__transaction_info[datetime.datetime.now()] = {'Loan' : amount}
            self.__user_info['Loan_amount'] = self.__loan_amount
        users[self.__account_number] = self.__user_info
        time.sleep(0.5)

    def transfer_amount(self,amount, account_no):
        """
        The function transfers a specified amount from one account to another if there is enough balance
        and the destination account exists.
        
        :param amount: The amount parameter represents the amount of money that is being transferred
        from one account to another
        :param account_no: The account number of the recipient account
        """
        if(amount > self.__balance):
            print("Not Enough Balance to Transfer!")
        elif(User.__users.has_key(account_no)):
            raise CustomException("This account does not exist!")
        else:
            print(f"{amount} has been transferred to {account_no}")
            self.__balance -= amount

    def get_account_info(self):
        return self.__user_info
    


    

    
    


