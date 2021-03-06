class CustomError(Exception):
    def __init__(self, n):
        Exception.__init__(self)
        self.n = n

class CustomError2(Exception):
    pass

try:
    raise CustomError(3)
except CustomError as c:
    print(c.n)

try:
    raise CustomError2
except CustomError2:
    print("Caught")

try:
    assert 1 > 2
except AssertionError:
    print("Assertion failed")
