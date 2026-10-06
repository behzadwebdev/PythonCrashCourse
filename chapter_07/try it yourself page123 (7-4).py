prompt = "\nPlease enter a topping for your pizza:"
prompt += "\n(Enter 'quit' when you are finished)"
while True :
    topping = input(prompt)
    if topping == 'quit' :
        break
    else: 
        print(f"I'll add {topping} to your pizza.")
############## 7-5
prompt = "\nplease enter your age: "
prompt += "\n(Enter 'quit' to stop)"
while True :
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age <3 :
        print("Your ticket is free.")
    elif age <= 12 :
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
