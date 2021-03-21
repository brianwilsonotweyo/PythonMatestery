# Using the "or" in if else statements
T = 10
F =5
# Works when one of the conditions is true and doesnt if both are false
# i.e  T ==F s false and T==F or T<=F is also false thus will print FALSE
# WILL ONLY PRINT TRUE WHEN ONE OF THE STATEMENTS IS TRUE OR BOTH TRUE 🙂😏
if(T >= F or T == F):
    T = 0
    print("TRUE")
else:
    print("FALSE")