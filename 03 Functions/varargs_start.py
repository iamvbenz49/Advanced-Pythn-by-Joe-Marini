# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*numbers):
    return sum(numbers)
    pass


def main():
    # TODO: pass different arguments
    print(addition(1,2,3,4,5,56,7))

    # TODO: pass an existing list


if __name__ == "__main__":
    main()
