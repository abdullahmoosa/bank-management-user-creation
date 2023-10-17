from user import User,users
import sys

account_types = {
    1 : "Savings",
    2 : "Current",
}


if __name__ == '__main__':
    while True:
        print('''
            1 : Create Account
            2 : Deposit
            3 : Withdraw
            4 : Transfer
            5 : Check Balance
            6 : Take Loan
            7 : Check Transaction History
        ''')
        sequence = int(input("Please Select your desired task : "))
        if sequence == 1:
            get_account_type = int(input("Please Enter your desired account Type\n 1 : Savings 2 : Current "))
            account_type = account_types[get_account_type]
            email_address = input("Please type your email address")
            address = input("Please type your home address")
            user = User()
            user.create_account(account_type= account_type, email= email_address, address= address)
            created_account_number = user.get_account_info()['account_no']
            print(f"Congratulations! You have successfully created your account. Your account number is : {created_account_number}")
        elif sequence == 2:
            account_number = int(input("Please enter your Account Number"))
            try :
                user = users[account_number]
                amount = int(input("Please enter your desired amount"))
                user.deposit(amount)
            except Exception as e:
                print("Account number is invalid! Please try again!")
                sys.exit()
        elif sequence == 3:
            account_number = int(input("Please enter your Account Number"))
            try :
                user = users[account_number]
                amount = int(input("Please enter your desired amount"))
                user.withdraw(amount)
            except Exception as e:
                print("Account number is invalid! Please try again!")
                sys.exit()
        elif sequence == 4:
            account_number = int(input("Please enter your Account Number"))
            try :
                try :
                    user = users[account_number]
                    amount = int(input("Please enter your desired amount"))
                    transer_account = int(input("Please enter the account number where you want to transfer"))
                    user.withdraw(amount, transer_account)
                except Exception as e:
                    print("Invalid Transfer Account Number or Invalid Amount")
                    sys.exit()
            except Exception as e:
                print("Account number is invalid! Please try again!")
                sys.exit()
        elif sequence == 5: 
            account_number = int(input("Please enter your Account Number"))
            try :
                user = users[account_number]
                user.check_balance()
            except Exception as e:
                print("Account number is invalid! Please try again!")
                sys.exit()
        elif sequence == 6:
            account_number = int(input("Please enter your Account Number"))
            try :
                user = users[account_number]
                amount = int(input("Please enter desired loan amount"))
                user.take_loan(amount)
            except Exception as e:
                print("Transaction Invalid! Please check your account number or number of times loans taken!")
                sys.exit()
        else:
            account_number = int(input("Please enter your Account Number"))
            try :
                user = users[account_number]
                user.check_transaction_history()
            except Exception as e:
                print("Account No Invalid")
                sys.exit()

