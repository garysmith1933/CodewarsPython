def friend(x):
    friends = filter(lambda name: len(name) == 4, x)
    return list(friends)