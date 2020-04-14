__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''
from ex14 import lengths_of_words


def find_longest_word(array):
    x = 0
    ret = lengths_of_words(array)
    for i in ret.keys():
        if x > ret[i]:
            continue
        else:
            x = ret[i]
    return x


if __name__ == "__main__":
    print(find_longest_word(["fruit", "cars", "people", "amrutchougale"]))
