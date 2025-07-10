card_holder_name = "Faiq Ahmad"
card_pin = 7356
account_balance = 100000
daily_account_limit = 100000
CNIC_number = (3460381511307)
account_number = 291009176257

pin_user_input = int(input("Enter Your Pin :"))

if pin_user_input == card_pin:
    print(f"Welcome {card_holder_name}")
    print("Choose Your Account :")
    print("1: Current Account")
    print("2: Savings Account")

    account_type = input("Enter Your Account Type (1 or 2) :")
    if account_type in ['1', '2']:
        print("\nSelect Transaction Type :")
        print("1: Balance Inquiry")
        print("2: Cash Withdrawal")
        print("3: Cash Deposit")
        transaction_choice = int(input("Enter Your Choice (1-3):"))

        if transaction_choice == 1:
            inq_receipt = print("Do you want a Printed Receipt (1 or 2)")
            print("1: Yes")
            print("2: No")
            inq_receipt_input = input("Enter Your Choice :")
            if inq_receipt_input == "1":
                import datetime
                dt_time = datetime.datetime.now()
                print(f"Transaction time : {dt_time}")
                print(f"Your Account Balance is : {account_balance}")
            else:
                print(f"Your account balance is : {account_balance}")
                print("Thank You for using our ATM")
                exit()    
            

        elif transaction_choice == 2:
            print("\nChoose the amount you want to withdraw :")
            print("1: RS 1000")
            print("2: RS 5000")
            print("3: RS 10000")
            print("4: RS 20000")
            print("5: RS 50000")
            print("6: Enter Your Amount")
            
            amount_choice = input("Enter your Choice (1-6): ")
            if amount_choice in ["1", "2", "3", "4", "5", "6"]:
                
                if amount_choice == "1":
                    withdraw_amount = 1000
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice :")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f'Transaction Time: {now}')
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance} ")
                        exit()
                          
                if amount_choice == "2":
                    withdraw_amount = 5000     
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice :")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f'Transaction Time: {now}')
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance} ")
                        exit()
                    
                if amount_choice == "3":
                    withdraw_amount = 10000
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice :")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f'Transaction Time: {now}')
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance} ")
                        exit()
                    
                if amount_choice == "4":
                    withdraw_amount = 20000
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice :")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f'Transaction Time: {now}')
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance} ")
                        exit()
                
                if amount_choice == "5":
                    withdraw_amount = 50000
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice :")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f'Transaction Time: {now}')
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance} ")
                        exit()
                    
                if amount_choice == "6":
                    withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                    print("Do you want a printed receipt?")
                    print("1: Yes")
                    print("2: No")
                    input_receipt = input("Enter your choice: ")
                    if input_receipt == "1":
                        import datetime
                        now = datetime.datetime.now()
                        print(f"Transaction Time: {now}")
                        print(f"Transaction amount: {withdraw_amount}")
                        rem_balance = account_balance - withdraw_amount
                        print(f"Your remaining balance is {rem_balance}")
                        exit()

                    if withdraw_amount > account_balance:
                        print("Insufficient Balance")
                    elif withdraw_amount > daily_account_limit:
                        print("Your daily limit has exceeded")

        elif transaction_choice == 3:
            input_cnic = int(input("Enter Your CNIC Number :"))
            if input_cnic == CNIC_number:
                input_account_number = int(input("Enter Your Account Number :"))
                if input_account_number == account_number:
                    deposit_money = int(input("Enter the money you want to deposit :"))
                    print("Money Deposit Successful!")
                    new_account_balance = deposit_money + account_balance
                    print(f'Your Account Balance is {new_account_balance}')
                else:
                    print("Invalid Account Number, Please try again")
                    exit()
            else:
                print("Invalid CNIC Number, Please try again")
                exit()
    else:
        print("Invalid account type.")
else:
    print("Incorrect Pin, Try again.")
           
                    
            
                
                
                
    
                      
        

        
    

    
    




