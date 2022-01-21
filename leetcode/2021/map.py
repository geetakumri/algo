friends = ['rolf', 'jose', 'randy', 'anna', 'mary']
friends_upper = map(lambda x: x.upper(), friends)
friends_upper = [friend.upper() for friend in friends]
friends_upper = (friend.upper() for friend in friends)
print(next(friends_upper))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'geeta', 'password': '456'}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)
