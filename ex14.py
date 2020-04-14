__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
'''


def lengths_of_words(array):
    ret = {}
    for i in range(0, len(array)):
        x = 0
        for j in range(0, len(array[i])):
            x += 1
        ret[array[i]] = x
    return ret


if __name__ == "__main__":
    print(lengths_of_words(["fruit", "cars", "people"]))
