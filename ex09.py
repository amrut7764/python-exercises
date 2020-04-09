__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
'''


def is_member(x, a):
    for i in a:
        if x == i:
            return True
        else:
            continue
    return False


if __name__ == "__main__":
    print(is_member("a", ["v", "c", "r", "b"]))
