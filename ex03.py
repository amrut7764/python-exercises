__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
'''


def length_of_string(str):
    count = 0
    for i in str:
        count = count + 1

    return count


if __name__ == "__main__":
    print(length_of_string("Define function."))
