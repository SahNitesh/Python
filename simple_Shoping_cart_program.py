          

                      #10 shopping cart program 
# using a  for loop / while loop and if else statemnts along with collections

items = []
prices = []
total = 0

while True: #( makes it a infinnite loop until break statemnet)
    item = input("enter an item, or (press q to quit): ") #asking user to enter any item name of choice
    if item.lower() == "q":
        break
    else:
        price = float(input("enter price: "))# asking user to enter the price of choice for item selected
        items.append(item)#putting it in the list of items and prices
        prices.append(price)

print("********'Your Cart'*********")#some design

for item in items: #printing the items in the list of items
    print(item, end=", ")
print()
for price in prices: #printing the price from the list of prices
    print(price, end=", ")
print()
for price in prices: # calculatng the totaal price by adding all in list of prices
    total += price
print(f"your total is: {total}")