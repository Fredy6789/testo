# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inaective', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'ineactive':
        del users[user]
        print(user)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(user)



