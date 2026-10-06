sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'beef', 'egg', 'pastrami', 'veggie']
finished_sandwiches = []
print("Sorry, the deli has run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()} sandwich")
