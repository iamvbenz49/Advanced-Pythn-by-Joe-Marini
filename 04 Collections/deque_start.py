# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    print(d)

    # TODO: deques support the len() function
    print("count",len(d))
    # TODO: deques can be iterated over
    for i in d:
        print(i,end=" ")
    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    print("  ".join(d))

    # TODO: rotate the deque
    print(d)
    print(d.rotate(2))
    print(d)


if __name__ == "__main__":
    main()
