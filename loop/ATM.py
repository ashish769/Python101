#
balance=40000
pin_code=7107

print("------welcome to nabil bank-------")
print("**************001")
print("processing ......")

user=int(input("enter your valid pin code : \n"))

if user==pin_code:
    while True:
        print("""
         1.Balance Enquirey
         2.Withdraw
         3.deposite balance
         4.Exit
        """)

        choice=input("enter your choice : ")
        if choice=='1':
            print(f"you total balance {balance}")
            break
        elif choice=='2':
            withdraw_amt=float(input("enter your balance to withdraw : "))
            balance-=withdraw_amt
            print(f"{withdraw_amt} is debit from you account and Your total balance is {balance}")

        elif choice=='3':
            deposite_amt=float(input("enter your deposite amount : "))
            balance += deposite_amt
            print(f"{deposite_amt} is created in your account and Totol amount is {balance}")
        elif choice=='4':
            print("thanks for visit!!! ")
            break

else:
    print("invalid pincode")