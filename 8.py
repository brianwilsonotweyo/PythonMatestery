# Age calculating Program

print("Answer the Queries Below to know how long you've roamed the earth")
name = input("Name: ")
print("What is your age mate ",(name),"?")

age = int(input("Age: "))
# int is the operator for integers in python. these are numbers with out decimal digits/points

days = age*365 
minutes = age*525948
seconds = age*31556926

print("Hello, my dear", name," you've been alive for", days,"days",minutes,"minutes and", seconds,"seconds")
print("Thanks for using 8.py, my dear ", name)