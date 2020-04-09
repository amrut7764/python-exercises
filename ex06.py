__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''


def sum(array):
    _sum = 0
    for i in array:
        _sum = _sum + i
    return _sum


def multipy(array):
    _multi = 1
    for i in array:
        _multi = _multi * i
    return _multi


if __name__ == "__main__":
    print(sum([-4, -5, -6, -7, -8]))
    print(multipy([4, 5, 6, 7, 8]))
    print(multipy([1, 1, 1, 1]))
    print(multipy([0, 10, 20]))
