# Testing Multiple Elif expressions

print("DISCOUNT CHECKER")

price = 120000
times = int(input("How many times,\n have you shopped with Us: "))
if(times == 3):
    price = price -30000
    print("Your Discounted Price is UGX", price, "Thanks for shopping with Us")
elif(times == 4):
    price = price -50000
    print("Your Discounted Price is UGX", price, "Thanks for shopping with Us")
elif(times >= 4):
    price = price -60000
    print("Your Discounted Price is UGX", price, "Thanks for shopping with Us")

else: print("You have to have shopping with Us,\n for at least 3 times to receive a discount.")


