<b><h1>While Loops</h1></b>
<hr>
<h3>Q1</h3>
Write a program that prompts the user to enter his or her gender (M or F). If the user enters anything other than the two letters, the program will continue to prompt them until they have given a valid input.

The program should then display the salutation based on the gender (Mr. for M, Ms. for F)

Your output should look like one of these outputs when you run q1.py with the following inputs:
```
What is your gender? S
Wrong input, please enter your gender again!
What is your gender? Goma
Wrong input, please enter your gender again!
What is your gender? M
Got it! Thank you Mr.
```
```
What is your gender? Shelby 
Wrong input, please enter your gender again!
What is your gender? Uchiha
Wrong input, please enter your gender again!
What is your gender? F
Got it! Thank you Ms.
```
<hr>
<h3>Q2</h3>
Write a program that prompts the user for an integer. The program will then prompt the user to guess that number again.

If the user guesses a number that is lesser than the first prompt, the program will print "Your guess was too low."
if the user guesses a number that is higher than the first prompt, the program will print "Your guess was too high."

Incorrect guesses will cause the program to prompt the user to guess again. When the user guesses correctly, the program stops.

Sample output:
```
Enter a number to guess: 82  
Now forget all about that number, and try to guess it: 81
Your guess was too low.
Enter your guess again: 100
Your guess was too high.
Enter your guess again: 83
Your guess was too high.
Enter your guess again: 80
Your guess was too low.
Enter your guess again: 82
You got it!
```
