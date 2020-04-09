__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
'''


def max(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "Both numbers are equal"


if __name__ == "__main__":
    ret = max(4, 5)
    print(ret)
    ret = max(232, 50)
    print(ret)
    ret = max(4545, 4545)
    print(ret)
