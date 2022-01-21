friends = [
    {
        'name': 'rolf',
        'location': 'san fransico'
    },
    {
        'name': 'jose',
        'location': 'san fransico'
    }
]

your_loc = input('where are u right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_loc]

if len(friends_nearby) > 0:
    print(' u r not alone')
# same as
if any(friends_nearby):
    print('u r not alone')

if all(friends_nearby):
    print('u r not alone')

print(all([0,1,2,3,4,5]))
print(any([0,1,2,3,4,5]))
print(bool(-0.0))
print(bool(0))
print(bool(0.00000000000000000000001))

print(bool([]))
print(bool([None]))