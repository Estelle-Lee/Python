def fizzbuzz(num):
    for number in range(num+1):
        if number%3==0 and number%5==0:
            print("FizzBuzz")
        else:
            if number%3==0:
                print("Fizz")
            elif number%5==0:
                print("Buzz")
            else:
                print(number)

fizzbuzz(50)
        
