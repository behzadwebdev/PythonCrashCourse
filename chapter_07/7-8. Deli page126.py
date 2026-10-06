sandwich_orders = ['tuna' , 'chicken' , 'beef' , 'egg' , 'veggie']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()} sandwich")
