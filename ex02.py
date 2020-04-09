__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''


def max_of_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    elif y > z:
        return y
    else:
        return z


if __name__ == "__main__":
    print(max_of_three(38, 36, 116))
    print(max_of_three(1, 1, 1))
