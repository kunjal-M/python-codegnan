# one egg price is 5 rupees and what is the price of 'N' eggs

egg_price = 5
n = int(input("enter number of eggs: "))
total_price = n*egg_price
print("Total price for", n, "eggs is:", total_price, "rupees")

# if box contains N pencils and total price is M,then what price of each pencil price

N = int(input("Enter number of pencils: "))
M = int(input("Enter total price: "))
price = M/N
print("price of each pencil", price)


#red ball price is 25, green ball price is 30, if I buy N red balls and M green balls,then what is the total cost

N = int(input("enter the red balls: "))
M = int(input("enter the green balls: "))
price1 = N*25
print("total price of red balls:",price1)
price2 = M*30
print("total price of red balls:",price2)
total_price = price1 + price2
print("total price:",total_price)
