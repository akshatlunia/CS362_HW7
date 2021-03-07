def FizzBuzz():
    for i in range(1, 101):
        if(i % 3 == 0):
            k = "Fizz"
            print(k, end=' ')
        elif(i % 5 == 0):
            k = "Buzz"
            print(k, end=' ')
        else:
            print(i, end=' ')
    return k
