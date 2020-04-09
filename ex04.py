__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''


def is_vowel():
    char = input("Enter character:> ").rstrip()
    array = ['a', 'e', 'i', 'o', 'u']
    if char in array:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_vowel())
