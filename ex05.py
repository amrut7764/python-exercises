__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon"
'''


def translate(str):
    array = ["a", "e", "i", "o", "u"]
    j = ""
    for i in str:
        if i == " ":
            j = j + i
            continue
        if i not in array:
            j = j + i + "o" + i
        else:
            j = j + i
    return j


if __name__ == "__main__":
    print(translate("this is fun"))
