def greet_users(names):
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot', 'behzad']
greet_users(usernames)
######################page 143 printing models.py
print("\n----------------------------------")
######################## without function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
###################### with functuon page143-4
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
