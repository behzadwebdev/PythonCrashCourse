############# 8-1
def display_message():
        print("I am learning about functions in Python.")
display_message()
#############8-2
def favorite_book(title):
        print(f"One of my favorite book is {title}.")
favorite_book("Alice in Wonderland")
#############
def book_info(author="Rowling", title="Harry Potter"):
    print(f"The book {title} is written by {author}.")
book_info(title="1984", author="George Orwell")
############# more exercise by chatgpt
def book_details( title , author ,year):
    print(f"The book {title} was written by {author} in {year}.")
book_info = {"title" : "1984", "author" : "George Orwell" , "year" : 1949}
book_details(**book_info)
##############8-3
def make_shirt(size , message):
    print(f"The shirt size is {size} and the message on it is: {message}.")
make_shirt("M" , "Hello World")
make_shirt(size = "l" , message = "python is fun!")
###############8-4
def make_shirt(size='large', message='I love Python'):
      print(f"The shirt size is {size} and the message on it is: {message}.")
make_shirt()
make_shirt('medium')
make_shirt('small', 'Hello!')
###############8-5
def describe_city(city , country= 'Germany'):
      print(f"{city} is in {country}.")
describe_city('Berlin')
describe_city('Munich')
describe_city('Paris', 'France')