rivers = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'danube' : 'germany'
}
for river , country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
print("--------------------")
print("rivers:")
for river in rivers.keys():
    print(river.title())
print("------------------")
print("country")
for country in rivers.values():
    print(country.title())
