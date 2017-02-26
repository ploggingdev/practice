for ix in range(1,101):
    res = ''
    if ix%3 == 0:
        res += 'Fizz'
    if ix%5 == 0:
        res += "Buzz"
    print(res or ix)