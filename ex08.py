__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True
'''


def is_palindrome(str):
    palString = ""
    for i in range(0, len(str)):
        palString = str[i] + palString

    if palString == str:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome("radar"))
    print(is_palindrome("this is palindrome"))
