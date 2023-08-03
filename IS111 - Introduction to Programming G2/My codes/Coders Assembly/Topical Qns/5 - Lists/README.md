<b><h1>Lists</h1></b>
<hr>
<h3>Q1</h3>
Write a program that prompts the user for a sentence. Afterwards, the program should display the number of words in the sentence, as well as printing out all the words in the sentence (per line).

You may assume that there is no punctuation in the sentence.

Sample outputs:
```
Enter a sentence: I am crazy but I am also very mad
There are a total of 9 words in this sentence. They are: 
I
am
crazy
but
I
am
also
very
mad
```
```
Enter a sentence: I think that Prof Kyong is my OPPAAAA
There are a total of 8 words in this sentence. They are: 
I
think
that
Prof
Kyong
is
my
OPPAAAA
```
<hr>
<h3>Q1b</h3>
Now, reusing your code from q1.py, modify it such that the program displays UNIQUE words (In other words, no duplicated words should appear). The word count remains the same.

Sample outputs:
```
Enter a sentence: I am crazy but I am also very mad
There are a total of 9 words in this sentence. They are: 
I
am
crazy
but
also
very
mad
```
```
Enter a sentence: Are you a tuple because I think you have a immutable behaviour
There are a total of 12 words in this sentence. They are: 
Are
you
a
tuple
because
I
think
have
immutable
behaviour
```
<hr>
<h3>Q2</h3>
Complete the function <i>get_longest_string</i> that takes in a list of strings (str_list). The function should return the string with the <b>longest length</b>.

Use the test cases in q2.py to test your code.

<hr>
<h3>Q3</h3>
Complete the function <i>get_odd_numbers</i> that takes in a list of integers (num_list). The function should return a <b>list containing ONLY odd numbers</b>.

Use the test cases in q3.py to test your code.
<hr>
<h3>Q4</h3>
Write a program that prompts the user for an integer to represent the length of a list of numbers. The program should then prompt the user to enter numbers to put inside their list (e.g. if length is input as 5, the user will be prompted to enter 5 numbers)

The program should then calculate and display the minimum, maximum and median number based on the list of numbers you created. 
Sample outputs:
```
Enter length of number list: 4
Enter number 1: 2
Enter number 2: 5
Enter number 3: 6
Enter number 4: 10

The minimum is 2
The maximum is 10
The median is 5.5
```
```
Enter length of number list: 7
Enter number 1: 1
Enter number 2: 4
Enter number 3: 6
Enter number 4: 2
Enter number 5: 15
Enter number 6: 28
Enter number 7: 10

The minimum is 1
The maximum is 28
The median is 6
```
<hr>
<h3>Q5</h3>
Complete the function <i>get_purchase_price</i> that takes in a list of strings (item_list) and a list of tuples (item_price_list). There are 2 elements in each tuple, the first represents the item name, while the second element represents the price e.g. ('Cabbage',2.50).

The function should return the total cost of the items in item_list, based on the prices shown in item_price_list. You may assume that all the items in item_list are present in item_price_list (in other words, you won't encounter an item in item_list that is not present in item_price_list)

You may use the test cases in q5.py to help you test your code.
