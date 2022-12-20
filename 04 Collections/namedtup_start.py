# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point","X Y")
    p1 = Point(10,12)
    p2 = Point(1,6)
    print(p1,p2)
    print(p1.X,p2.Y)
    # TODO: use _replace to create a new instance
    p1 = p1._replace(X=100)
    print(p1)
    pass


if __name__ == "__main__":
    main()
