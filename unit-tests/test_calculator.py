from calculator import square


# def test_square():
#     # try:
#     #     assert square(2) == 4
#     # except AssertionError:
#     #     print("2 square was not 4")
#     assert square(2) == 4
#     assert square(3) == 9 
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
#     # try:
#     #     assert square(-2) == 4
#     # except AssertionError:
#     #     print("-2 square was not 4")

# categorising the test, pytest automatically test each one independently even if one fails
def test_positive():
    assert square(2) == 4
    assert square(3) == 9 

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# def main():
#     test_square()

# if __name__ == "__main__":
#     main()
#     # run pytest test_calculator.py 