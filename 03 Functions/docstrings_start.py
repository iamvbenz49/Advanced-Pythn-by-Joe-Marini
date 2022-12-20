# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1,arg2) -->JUST PRINTS THE ARUEMENTS

    Parameters
    arg1 :the first arguement
    arg2 :the second arguement,defaults to None
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
