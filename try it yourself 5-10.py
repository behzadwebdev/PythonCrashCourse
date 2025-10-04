current_users = ['ahmad', 'reza', 'hadi', 'behzad', 'rostam']
new_users = ['ahmad', 'behzad', 'sohrab','soran', 'payamn']
current_lower = [user.lower()for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_lower:
        print(f'Sorry, {new_user} is already taken, Please enter a new username.')
    else:
        print(f'Great!{new_user} is available.')
        