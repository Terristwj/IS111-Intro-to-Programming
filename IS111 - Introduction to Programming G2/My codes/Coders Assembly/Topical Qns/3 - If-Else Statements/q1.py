# YOUR CODE GOES HERE
age = int(input("Enter your age in integer: "))
text = "You're "
if age <= 12:
    text += "a kid!"
elif age <= 30:
    text += "okay."
else:
    text += "too old!"
print(text)