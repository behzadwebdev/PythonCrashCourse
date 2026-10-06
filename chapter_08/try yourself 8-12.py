############# 8-12
def make_sandwich(*items):
    print("ساندویچ ها با مواد زیر آماده می شود")
    for item in items:
        print(f"- {item}")
        print()
make_sandwich('ژامبون', 'پنیر', 'کاهو')
make_sandwich('گوجه فرنگی', 'بوقملون', 'کره بادام زمینی')
make_sandwich('مربا','موز', 'کالباس')

################ 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
my_profile = build_profile(
    'Behzad', 'Atash sokhan', 
     age=33,
     profession='Python programmer',
     city='Mahabad'
)
print(my_profile)
############### 8-14
car = make_car('subaru', 'outback', color='blue', tow_package=True)
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car        
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
