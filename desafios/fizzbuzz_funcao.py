

def fizzbuzz(b):
    msg = b

    fizz = b % 3 == 0
    buzz = b % 5 == 0 

    if fizz and buzz:
        msg = "FizzBuzz"
    elif fizz:
        msg = "Fizz"
    elif buzz:
        msg = "Buzz"

    return msg


def teste_fizzBuzz1():
    fizzbuzz(3) == "Fizz"

def teste_fizzBuzz2():
    fizzbuzz(5) == "Buzz"

def teste_fizzBuzz3():
    fizzbuzz(15) == "FizzBuzz"

def teste_fizzBuzz4():
    fizzbuzz(22) == 22
