################################# 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
my_restaurant = Restaurant('Shiraz Palace', 'Persian') 
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#################################### 9-2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
restaurant1 = Restaurant('Shiraz Palace', 'Persian')
restaurant2 = Restaurant('Tokyo', 'Japanese')
restaurant3 = Restaurant('La Bella', 'Italian')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

##################################  9-3
class User:
    def __init__(self, first_name, last_name, username=None, email=None, age=None, city=None):
        self.first_name = first_name
        self.last_name=last_name
        self.username = username
        self.email = email
        self.age = age
        self.city = city
    def describe_user(self):
        print("User profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        if self.username:
            print(f"  Username: {self.username}")
        if self.email:
            print(f"  Email: {self.email}")
        if self.age is not None:
            print(f"  Age: {self.age}")
        if self.city:
            print(f"  City: {self.city}")
        print("-" * 30)   
    def greet_user(self):
        
        if self.username:
            print(f"Hello, {self.username}! Welcome back.")
        else:
            print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
        print()

user1 = User("Ali", "Rezaei", username="alireza", email="ali@example.com", age=28, city="Tehran")
user2 = User("Sara", "Ahmadi", username="sara_ah", email="sara@example.com", city="Isfahan")
user3 = User("John", "Doe")

for u in (user1, user2, user3):
    u.describe_user()
    u.greet_user()
