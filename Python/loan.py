# Get the loan details
from calendar import month


money_owned = float(input('How much money do you owe, in dollars?\n')) #50,000
apr = float(input("What is the annual percentage rate?\n")) #3%
payment = float(input("What will your monthly pament be, in dollars?\n")) # $, 1000
months=int(input("How many months you want to see results for ?\n")) #24

# Divide apr by 100 to make it a percentage, then divide by 12 to make monthly

monthly_rate = apr/100/12

#Add in interest

for i in range(months):
    interest_paid = money_owned * monthly_rate
    money_owned = money_owned + interest_paid

    # make payment
    if (money_owned - payment < 0) : 
        print("the last payment is ",money_owned)
        print("you paid of loan in",i+1," months")
        break
    money_owned = money_owned - payment

    # Print the result after this

    print("Paid",payment,"of which",interest_paid,"was interest",end='.')
    print("Now I owe",money_owned,sep=' ')


