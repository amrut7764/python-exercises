__author__ = "imroot <chougale.amrut@gmail.com>"

'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

```
****
*********
*******
```
'''
from ex11 import n_chars


def histogram(array):
    for i in array:
        str = n_chars(i, "*")
        print(str)


if __name__ == "__main__":
    histogram([14, 2, 17])
