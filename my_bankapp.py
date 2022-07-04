import random 
import time 




with open("my.bank.txt", "r") as file:
    data = eval(file.read())
balance = 0

while True:
    print("Welcome to Skill Up Banking and Insurrance.\nThe leading Financial Company in the TECH Industry!")
    print((data))
    print("What would you like to do?")
    print("1. CREATE AN ACCOUNT  \n2. LOGIN TO AN EXISTING ACCOUNT \n3. QUIT")
    input_1 = input("Choose out of the options to continue.\n::>>")
    if input_1 == "1":
        print("Enter your legal first name...")
        f_name = input("::>>>").capitalize()
        print("Enter legal last name...")
        l_name = input("::>>>").capitalize()
        print("Kindly choose an account type below.")
        print("Savings \n Current \n Fixed Deposit \n Insurance")
        acc_type = input("::>>").capitalize()
        print("Weldone, now kindly choose a four digit pin you'll like to use for your login security")
        pin1 = input("::>>")
        print("You can as well set a four digit pin for your transaction security")
        pin2 = input("::>>")
        def generate_otp(n):
            otp = "0"
            for _ in range(n):
                otp=otp+str(random.choice(range(10)))
            return otp
        acc_num = generate_otp(9)
        print("Hold on a bit your account is been created")
        time.sleep(2)
        print("Congratulation your account as now been succesfully created!")
        time.sleep(1)
        print(f"Dear, {l_name} {f_name} for your {acc_type} account , your account number is {acc_num} and it will be used as your login ID for your mobile login.\nYour special pin is {pin1} and your transaction pin is {pin2} keep safe to avoid risk of scam.\nThank you for choosing skill up Banking and Insurance ")
        
        data[acc_num] = {
            'first_name' : f_name,
            'last_name' : l_name,
            'login pin' : pin1,
            'transaction pin' : pin2,
            'balance' : balance
        }
    elif input_1 == "2":
        print("Input Login ID and Login pin to sign in to your account")
        acc_num = input("Input your login ID here::>>")
        account_data = data.get(acc_num, False)
        if acc_num:
            log_id = input("Input your login pin here::>>")
            login_data = data[acc_num].get("login pin", False)
            if login_data == log_id:
                print(f"Welcome {data[acc_num]['first_name']}, you have successfully signed in to your account")
      
        while True:
            print(f"{data[acc_num]['first_name']}, What would you like to do?")
            print("1. Check balance \n2. Deposit \n3. Transfer \n4. Withdraw to own Accounts \n5. Sign Out")
            input_2 = input("::>>")
            if input_2 == "1":
                print("Enter transaction pin")
                input_pin1 = input("::>>")
                bal_data = data[acc_num].get('transaction pin', False)
                time.sleep(1)
                if bal_data == input_pin1:
                    print("Retreiving balance...")
                    time.sleep(2)
                    account_balance = data[acc_num].get('balance')
                    print(f"Your account balance is {account_balance}")
                else:
                    print("Invalid pin")
            elif input_2 == "2":
                print("How much would you like to deposit?")
                amt = int(input("::>>"))
                print("Enter transaction pin!")
                input_pin2 = input("::>>")
                dep_data = data[acc_num].get('transaction pin', False)
                if dep_data == input_pin2:
                    data[acc_num]['balance'] += amt
                    print(f"You have succesfullly deposited {amt}")
                    print("Check balance to see status update")
            elif input_2 == "3":
                trs_amt = int(input("How much would you like to transfer.\n::>>"))
                print("Enter recipent ID")
                rec_id = input("::>>")
                rec_data = data.get(rec_id)
                if rec_data:
                    print("Verifying account numbuer...")
                    print(f"You are about to send {trs_amt} to user {rec_id} {data[rec_id]['first_name']} {data[rec_id]['last_name']}")
                    time.sleep(3)
                    if data[acc_num]['balance'] >= trs_amt:
                        data[acc_num]['balance'] -= trs_amt
                        data[rec_id]['balance'] += trs_amt
                    
                        print("Input transaction pin to complete transfer...")
                        input_pin3 = input("::>>")
                        trans_data = data[acc_num].get('transaction pin', False)
                        if trans_data == input_pin3:
                            print("Transaction Successful!")
                            print("Check balance to see status update")
                        else:
                            print("Invalid pin.")
                    else:
                        print("Insufficient Balance!!")
                else:
                    print(f"User {rec_id} not found.")
            elif input_2 =="4":
                wit_amt = int(input("How much would you like to withdraw?\n::>>"))
                print(f"You are about to withdraw the sum of {wit_amt} from your balance of {account_balance}")
                if data[acc_num]['balance'] >= wit_amt:
                        data[acc_num]['balance'] -= wit_amt
                        data[rec_id]['balance'] += wit_amt
                        print("Input transaction pin to complete transfer...")
                        input_pin4 = input("::>>")
                        wit_data = data[acc_num].get('transaction pin', False)
                        if wit_data == input_pin4:
                            print("Transaction Successful!")
                            print("Check balance to see status update")
                        else:
                            print("Invalid pin.")
                else:
                    print("Insufficient Balance")
                
            elif input_2 == "5":
                    break
            print("Thank you for choosing Skill up Banking and Insurrance")
    elif input_1 == "3":
        break
    else:
        print("Invalid input!")


with open("my.bank.txt", "w") as file:
    data = file.write(str(data))