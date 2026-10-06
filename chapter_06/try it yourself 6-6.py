favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
people = ['jen', 'john', 'edward', 'maria', 'phil']
for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()} for responding to the poll!")
    else:
        print(f"{person.title()}, please take our poll about your favorite programming language.")
