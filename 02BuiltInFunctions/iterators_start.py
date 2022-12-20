# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    # TODO: iterate using a function and a sentinel
    with open("testfile.txt","r") as fp:
        for line in iter(fp.readline,""):
            print(line)
    # TODO: use regular interation over the days
        for i in range(len(days)):
            print(i+1,days[i])
    # TODO: using enumerate reduces code and provides a counter
        for i in enumerate(days):
            print(i)
    # TODO: use zip to combine sequences
        for i,m in enumerate(zip(days,daysFr)):
            print(i,m[0],m[1])

if __name__ == "__main__":
    main()
