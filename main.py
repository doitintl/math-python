"""
A simple service that responds with whether an input (post) is
prime or not.

Usage::
./web-server.py [port]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "num=4" http://localhost
"""

from math import factorial
from flask import Flask
application = Flask(__name__)


def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number**0.5)
    f = 5
    while f <= r:
        if number % f == 0:
            return False
        if number % (f+2) == 0:
            return False
        f += 6
    return True


def sum_primes(num):
    sum = 0
    while (num > 1):
        if is_prime(num):
            sum = sum+num
        num = num - 1
    return sum


@application.route("/factorial/<int:num>")
def get_factorial(num):
    return 'The factorial of %d is %d' % (num, factorial(num))


@application.route("/")
def hello():
    return "Server successfully started!"


@application.route("/prime/<int:num>")
def detect_prime(num):
    return 'The sum of all primes less than %d is %d' % (num, sum_primes(num))
