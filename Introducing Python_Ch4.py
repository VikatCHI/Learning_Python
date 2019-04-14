# 4.1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4.2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else start > guess_me:
        print('oops')
        break
    start += start

# 4.3
for i in [3, 2, 1, 0]:
    print(i)

# 4.4
even = [number for number in range(10) if number % 2 ==0]

# 4.5
squares = {key: key * key for key in range(10)}

# 4.6
odd = {number for number in range(10) if number % 2 == 1}

# 4.7
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']

# 4.9
def get_odds():
    for number in range(1, 10, 2):
        yield number
for count, number in enumerate(get_odds(), 1):
    if count == 3：
        print("The third odd number is", number)
        break

# 4.10
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

# 4.11
class OopsException(Exception):
    pass
try:
    raise OopsException
except OopsException:
    print('Caught an opps')

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))

