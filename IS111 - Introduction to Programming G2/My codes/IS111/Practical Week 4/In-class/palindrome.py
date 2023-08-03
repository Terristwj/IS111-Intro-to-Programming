word = input("Enter a word :")
# Solution 1
is_palindrome = True
for i in range(len(word)//2):
    # print(word[i], word[-(i+1)])
    if not word[i] == word[-(i+1)]:
        is_palindrome = False

if is_palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is NOT a palindrome")


# Solution 2
# if len(word) % 2:
#     str_1 = word[0:len(word)//2]
#     str_2 = word[-1:len(word)//2:-1]
# else:
#     str_1 = word[0:len(word)//2]
#     str_2 = word[-1:len(word)//2-1:-1]

# is_palindrome = True
# for i in range(len(str_1)):
#     if not str_1[i] == str_2[i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print(word, "is a palindrome")
# else:
#     print(word, "is NOT a palindrome")


# Solution 3
# def palindrome (word):
#     length = len(word)
#     times_to_check = length // 2
#     palindrome_counter = 0
#     for i in range (0, times_to_check):
#         if (word[0 + i] == word[length - 1 - i]):
#             palindrome_counter += 1
    
#     if (palindrome_counter == times_to_check):
#         print (word + " is a palindrome")
#     else:
#         print (word + " is NOT a palindrome")
        
# word = input("Input a word: ")
# palindrome(word)