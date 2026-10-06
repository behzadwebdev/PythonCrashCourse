favorite_places = {
    'ali' : ['paris','zurich'],
    'sara' : ['berlin','frankfort','koln'],
    'reza' : ['vancover'],
}
for name,places in favorite_places.items():
    print(f"\n {name.title()}'s favorite places are:")
    for place in places:
        print(f'\t{place.title()}')
###################################### favorite_numbers6-10
favorite_numbers = {
    'ali': [7, 14, 21],
    'sara': [3, 6],
    'reza': [9],
    'mina': [1, 2, 3],
    'amir': [5, 10],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
################################ Cities6-11
cities = {
    'paris' :{
        'country':'France',
        'population':'21148327',
        'fact':'It is known as the "City of Light".'
    },
    'tokyo': {
        'country':'Japan',
        'population':'13929286',
        'fact':'It is the largest metropolian areain the word.'
    },
    'berlin':{
    'country':'Germany',
    'population':'3644826',
    'fact':'It has a rich history and many museums.'
    }
}
#########################Extensions 6-12
cities = {
    'paris' :{
        'country':'France',
        'population':'21148327',
        'fact':'It is known as the "City of Light".',
        'language': 'French',
        'mayor': 'Anne Hidalgo',
        'famous_for': 'Eiffel Tower'
    },
    'tokyo': {
        'country':'Japan',
        'population':'13929286',
        'fact':'It is the largest metropolian areain the word.',
        'language': 'Japanese',
        'mayor': 'Yuriko Koike',
        'famous_for': 'Shibuya Crossing'
    },
    'berlin':{
    'country':'Germany',
    'population':'3644826',
    'fact':'It has a rich history and many museums.',
    'language': 'German',
    'mayor': 'Kai Wegner',
    'famous_for': 'Brandenburg Gate'
    }
}
for city,info in cities.items():
    print(f"\nCity:{city.title()}")
    for key,value in info.items():
        print(f"{key.title()}: { value}")
