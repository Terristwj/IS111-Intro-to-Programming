def encrypt(my_dict, msg):
    # YOUR CODE GOES HERE

    return None

# DO NOT CHANGE THE FOLLOWING CODE BELOW
cipher_dict = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

print('----Test Case 1----')
result = encrypt(cipher_dict,'i love python')
print("Expected: v ybir clguba" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = encrypt(cipher_dict,'miya is a bad mlbb hero')
print("Expected: zvln vf n onq zyoo ureb" )
print("Actual:   " + str(result))
print()