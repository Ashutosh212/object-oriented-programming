
def cheer(n: int) -> str:
    """
    Repeat the word 'Ashutosh' n times, each on a new line.

    :param n: Number of times to Ashutosh
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n Ashutosh, one pre line
    :rtype: str

    """
    return "Ashutosh\n"*n

n: int = int(input("Number: "))
cheers: str = cheer()
print(cheers, end="") # using end to avoid last empty line due to \n

# run mypy typehints.py to check any type error
