for i in range(1,101):
    if (i%7==0 and i%3!=0):
        print("Fizz")
    elif (i%3==0 and i%7!=0):
        print("Buzz")
    elif (i%3==0 and i%7==0):
        print("FizzBuzz")
    else:
        print(i)
