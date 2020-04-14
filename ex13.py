__author__ = "imroot <chougale.amrut@gmail.com>"

'''
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
'''


def max_in_list(array):
    max = array[0]
    for i in range(0, len(array)):
        if max >= array[i]:
            continue
        else:
            max = array[i]
    return max


if __name__ == "__main__":
    print(max_in_list([51, 26, -9, 36, -50, -51, 11]))
