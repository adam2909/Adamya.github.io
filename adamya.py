# -*- coding: utf-8 -*-
"""adamya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pVlWih1SSgtzXnC01Dw2qoPSDnlhj1ch
"""

def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(is_prime(78), is_prime(79))
evenOdd(2)
evenOdd(3)
