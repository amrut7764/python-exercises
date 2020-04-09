__autho__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
'''

from ex09 import is_member


def overlapping(x, y):
    '''Using two nested for-loops'''
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i] == y[j]:
                return True
            else:
                continue
    return False


def overlapping1(x, y):
    '''overlapping() using the is_member() function from ex09'''
    for i in range(0, len(x)):
        if (is_member(x[i], y)):
            return True
    return False


if __name__ == "__main__":
    print(overlapping(["q", "w", "e", "r", "t", "y"],
                      ["a", "q", "d", "f", "g"]))  # Returns True
    print(overlapping(["q", "w", "e", "r", "t", "y"],
                      ["a", "s", "d", "f", "g"]))  # Returns False
    print(overlapping1(["q", "w", "e", "r", "t", "y"],
                       ["a", "s", "d", "f", "g"]))  # Returns False
    print(overlapping1(["q", "w", "e", "r", "t", "y"],
                       ["a", "s", "d", "q", "g"]))  # Returns True
