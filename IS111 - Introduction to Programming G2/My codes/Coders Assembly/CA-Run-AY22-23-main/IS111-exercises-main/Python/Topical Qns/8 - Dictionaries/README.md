<b><h1>Dictionaries</h1></b>
<hr>
<h3>Q1</h3>
Complete the function <i>contains_key</i>, which takes in 3 parameters:
- a dictionary (d1)
- another dictionary (d2)
- An integer or string (key)

The function should return True if the variable key is present as a key in both dictionaries d1 and d2, and returns False if otherwise.

You may refer to the test cases provided in q1.py
<hr>
<h3>Q2</h3>
Complete a function <i>contains_value</i>, which takes in 3 parameters:
- a dictionary (d1)
- another dictionary (d2)
- a string or integer (value)

The function should return True if the variable value is present as a <b>value</b> in both dictioanries d1 and d2 (the key that is linked to the value does not matter), and returns False if otherwise.

You may refer to the test cases provided in q2.py
<hr>
<h3>Q3</h3>
<i>This question was taken from Coders Assembly Run 1 AY2020-2021</i>

Complete the function <i>create_prime_dict</i> that takes in a list of integers greater than 1 (without any duplicates) as its parameter. The function creates a dictionary that maps each integer in the list to a boolean value that indicates whether or not this integer is a prime number.

Recall that a prime number is a number that is divisible only by 1 and itself.

For example, create_prime_dict([2, 3, 5, 10, 20, 23]) returns a dictionary that looks like the following: {2:True, 3:True, 5:True, 10:False, 20:False, 23:True}.

You may refer to the test cases provided in q3.py
<hr>
<h3>Q4a</h3>
<i>This question was taken from Coders Assembly Run 1 AY2020-2021</i>

You are given a dictionary that stores the mappings from English lowercase letters to their replacements. Note that no two letters will be mapped to the same replacement.

Define a function called encrypt() that takes in two parameters:
- my_dict (type: dict): a dictionary as described above.
- msg (type: str): a message consisting of only lowercase letters and spaces.
The function returns the encrypted message using my_dict as the substitution cipher. Note that a space remains untouched in the encrypted message.

You may refer to the test cases provided in q4a.py
<hr>
<h3>Q4b</h3>
<i>This question was taken from Coders Assembly Run 1 AY2020-2021</i>

Now define a function called decrypt(). This function also takes in two parameters:
- my_dict (type: dict): a dictionary as described above.
- encrypted_msg (type: str): an encrypted message.
The function returns the original message, i.e., the message that has been encrypted into the string encrypted_msg.

You may refer to the test cases provided in q4b.py
<hr>
<h3>Q5</h3>
Write a program that prompts the user to enter a word. This word will then be added to a dictionary that records the number of times the word has been added to the dictionary. 

Once the word has been added, the user will be prompted if they wish to continue adding words. You may assume that the user will only input "Yes" or "No".

If "No" has been input, the program will display the words in the dictioanry, as well as the number of time they have been added.

Sample outputs:
```
Enter the word: you 
Word added to dictionary. Continue adding? [Yes / No]Yes
Enter the word: you
Word added to dictionary. Continue adding? [Yes / No]Yes
Enter the word: cannot
Word added to dictionary. Continue adding? [Yes / No]Yes
Enter the word: fail
Word added to dictionary. Continue adding? [Yes / No]No
Here are the following words present in your dictionary: 
you with 2 appearances.
cannot with 1 appearance.
fail with 1 appearance.
```
```
Enter the word: is
Word added to dictionary. Continue adding? [Yes / No]No
Here are the following words present in your dictionary: 
is with 1 appearance.
```
