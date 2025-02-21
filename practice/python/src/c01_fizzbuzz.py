"""
This is the classical Fizzbuzz challenge
for a given number n, return 'Fizz' if n is divisible by 3,
return 'Buzz' if n is divisible by 5,
return 'FizzBuzz' if n is divisible by both 3 and 5,
otherwise return the number as a string.
"""


def fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
  