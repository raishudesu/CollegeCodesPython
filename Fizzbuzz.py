user = int(input())

def fizzbuzz(user):
    for i in range(user):
        i += 1
        if i%3 and i%5 == 0:
            print('FIZZBUZZ')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(user)
