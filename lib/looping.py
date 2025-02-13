def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

# Test the function
happy_new_year()


def square_integers(int_list):
    return [num ** 2 for num in int_list]  # List comprehension for squaring

# Test the function
print(square_integers([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]



def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Run the function
fizzbuzz()
