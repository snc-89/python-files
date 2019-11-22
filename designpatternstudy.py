from random import randrange

arr = ['strategy','observer','decorator',
        'iterator','composite','singleton',
        'command','adapter','facade',
        'creational','behavioural','structural',
        'only talk to your friends','strive for loosely coupled objects',
        'encapsulate what varies','favour composition over inheritance',
        'don\'t expose your internals','code to interfaces, not implementations',
        'open for extension, closed for modification']

print('\n')
for i in range(10):
    idx = randrange(len(arr))
    print(arr[idx])
    arr.pop(idx)