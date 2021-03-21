# if-elif, else statements in Python

# simple program to see if the user is eligible to borrow capital 🗽🛺 from our software # bank 

print("CREDIT CHECKER")

salary = int(input("How much is your monthly Salary: "))

if(salary > 100000):
    amount = 200000
    print("You are elegible for the loan by First paying UGX", amount,"Colateral ")

elif(salary == 100000):
    amount = 250000
    print("You are elegible for the loan by First paying UGX", amount,"Colateral ")
else:
    
    print("You are not elegible for the loan ")

