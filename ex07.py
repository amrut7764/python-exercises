__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
'''


def reverse(str):
    retString = ""
    for i in range(0, len(str)):
        retString = str[i] + retString
    return retString


if __name__ == "__main__":
    reverse("I am testing")
