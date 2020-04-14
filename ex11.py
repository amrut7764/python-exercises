__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
'''


def n_chars(x, y):
    a = ""
    for i in range(0, x):
        a = a + y
    return a


if __name__ == "__main__":
    print(n_chars(534, "a"))
