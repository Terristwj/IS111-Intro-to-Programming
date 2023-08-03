def decrypt(my_dict,encrypted_msg):
    # YOUR CODE GOES HERE
    new_msg = ""
    for ch in encrypted_msg:
        if ch in my_dict:
            new_msg += my_dict[ch]
        else:
            new_msg += ch
    return new_msg


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
result = decrypt(cipher_dict,'v ybir clguba')
print("Expected: i love python" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = decrypt(cipher_dict,'zvln vf n onq zyoo ureb')
print("Expected: miya is a bad mlbb hero" )
print("Actual:   " + str(result))
print()