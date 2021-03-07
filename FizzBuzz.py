def FizzBuzz():
    for i in range(1, 101):
        if(i % 15 == 0):
            f = "FizzBuzz"
            print(f, end=' ')
            continue
        elif(i % 3 == 0):
            k = "Fizz"
            print(k, end=' ')
            continue
        elif(i % 5 == 0):
            k = "Buzz"
            print(k, end=' ')
            continue
        else:
            print(i, end=' ')
    return f
