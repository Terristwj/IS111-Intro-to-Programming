num_books = int(input('How many books do you have in your basket? '))

total_price = 0.0
num_books_cheaper_than_10 = 0

# Assume num_books >= 1.
price = float(input('What is the price of the book number 1? :$'))
total_price += price
min_price = price
max_price = price
if price < 10.0:
    num_books_cheaper_than_10 += 1

for i in range(2, num_books + 1):
    price = float(input('What is the price of the book number ' + str(i) + '? :$'))
    
    # update total price
    total_price += price
    
    # update min price if necessary
    if price < min_price:
        min_price = price
    
    # update max price if necessary
    if price > max_price:
        max_price = price
    
    # update num books cheaper than $10 if necessary
    if price < 10.0:
        num_books_cheaper_than_10 += 1

print('\na) Total price: $'+ str(round(total_price, 2))
print('b) Average price: $'+ str(round(total_price/num_books, 2)))
print('c) Price of the least expensive book : $'+ str(min_price))
print('d) Price of the most expensive book : $'+ str(max_price))
print('e) Number of book cheaper than $10 : '+ str(num_books_cheaper_than_10))
print('f) Percentage of book cheaper than $10 : '+ str(round(num_books_cheaper_than_10/num_books*100,2)) +'%')    