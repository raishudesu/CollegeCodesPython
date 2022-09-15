user = int(input())
def fizzbuzz(user):
    for i in range(user):
        i += 1
        if i%3 == 0 and i%5 == 0: #to know if the value is divisible by 3 AND 5
            print('FIZZBUZZ')
        elif i%3 == 0:            #to know if the value is divisible by 3
            print('Fizz')
        elif i%5 == 0:            #to know if the value is divisible by 5
            print('Buzz')
        else:
            print(i)
fizzbuzz(user)
