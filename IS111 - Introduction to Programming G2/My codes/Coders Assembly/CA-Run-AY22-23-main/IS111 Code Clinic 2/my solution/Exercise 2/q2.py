##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

# YOUR CODE GOES HERE.
def check_palindrome(word):
    word_size = len(word)
    is_even = (word_size % 2 == 0)
    if is_even:
        front = word[:len(word)//2]
        back = word[len(word)//2:][::-1]
    else:
        front = word[:len(word)//2]
        back = word[len(word)//2+1:][::-1]
    if front == back:
        return True
    return False

word = input("Enter a palindrome: ")
is_palindrome = check_palindrome(word)
while not is_palindrome:
    word = input("That is not a palindrome, enter a palindrome! : ")
    is_palindrome = check_palindrome(word)
print("Finally, you entered a palindrome")