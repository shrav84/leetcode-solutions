# This is the same question as the 9th check palindrome of a 
# number but with a different more raw approach because you can 
# just change the syntax and implement this version into any language 
# the previous version is only implementable in python because only python
#  has reverses string but this version you can implement in C, c++, Javascript
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False  # negative numbers can't be palindromes

    orig = x
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x //= 10

    return rev == orig
