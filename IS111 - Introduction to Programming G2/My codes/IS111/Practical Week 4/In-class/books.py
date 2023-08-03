basket = int(input("How many books do you have in your basket? "))

total_price = 0.0
count_below10 = 0

for i in range(basket):
    price = float(input("What is the price of the book number " + str(i+1) +"? :$"))
    total_price += price
    
    if i == 0:
        min_price = max_price = price

    if min_price > price:
        min_price = price
    if max_price < price:
        max_price = price
    
    if price < 10:
        count_below10 += 1

print()
print("a) Total price: $" + str(total_price))

print("b) Average price: $" + str(round(total_price/basket, 2)))

print("c) Price of the least expensive book : $" + str(min_price))

print("d) Price of most expensive book: $" + str(max_price))

print("e) Number of books cheaper than $10 : " + str(count_below10))

percentage = round(count_below10 / basket * 100, 2)
print("f) Percentage of books cheaper than $10 : " + str(percentage) + "%")