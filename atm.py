card_holder_name = "Faiq Ahmad"
card_pin = 7356
account_balance = 100000
daily_account_limit = 100000

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
        transaction_choice = int(input("Enter Your Choice (1 or 2):"))

        if transaction_choice == 1:
            print(f"Your Account Balance is {account_balance}")

        elif transaction_choice == 2:
            print("\nChoose the amount you want to withdraw :")
            print("1: RS 1000")
            print("2: RS 5000")
            print("3: RS 10000")
            print("4: RS 20000")
            print("5: RS 50000")
            print("6: Enter Your Amount")

            amount_choice = input("Enter your Choice (1-6): ")

            if amount_choice == "1":
                withdraw_amount = 1000
            elif amount_choice == "2":
                withdraw_amount = 5000
            elif amount_choice == "3":
                withdraw_amount = 10000
            elif amount_choice == "4":
                withdraw_amount = 20000
            elif amount_choice == "5":
                withdraw_amount = 50000
            elif amount_choice == "6":
                withdraw_amount = int(input("Enter the amount you want to withdraw :"))
            else:
                print("Invalid Option")
                exit()

            
            if withdraw_amount > account_balance:
                print("Insufficient Balance!")
            elif withdraw_amount > daily_account_limit:
                print("Your Daily Limit has been exceeded!")
            else:
                print("Transaction Successful!")
                remaining_balance = account_balance - withdraw_amount
                print(f"Remaining Balance: {remaining_balance}")

        else:
            print("Invalid transaction option.")

    else:
        print("Invalid account type.")

else:
    print("Incorrect Pin, Try again.")

    
  
           
                    
            
                
                
                
    
                      
        

        
    

    
    




