#lista continuação

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
cars.sort()
print(cars)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

#exemplo2

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
new_friends = list(friends)
print(friends)
print(new_friends)