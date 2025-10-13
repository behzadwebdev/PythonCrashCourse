car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")
####################### 7-2
people = input("How many people are in your dinner group? ")
people = int(people)
if people > 8:
     print("Sorry, you'll have to wait for a table.")
else:
     print("Your table is ready!")
####### 7-3
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0 : 
    print("The number is multiple of 10.  ")
else:
     print("The number is not multiple of 10. ")
    