# Grade calculator

x = int(input("enter the marks: "))
if x > 100 or x < 0:
        print("invalid input")   
elif x >= 90:
        print("Grade A")
elif x >= 80:
        print("Grade B")
elif x >= 60:
        print("Grade C")
elif x >= 40:
        print("Grade D")   
else:
        print("Fail")

# check wheather number is positive even or odd , negative even or odd

num = int(input("enter the number: "))
if num >= 0 and num % 2 == 0:
    print("The number is positive and even")
elif num < 0 and num % 2 == 0:
    print("The number is negative and even")
elif num > -1 and num % 2 == 1:
    print("The number is positive and odd")
else:
    print("The number is negative and odd")

#Nested if

n = int(input("Enter the number: "))
if n % 2 == 0:
   if n >= 0:
        print("the number is positive and even")
else:
        print("the number is negative and even")
if n % 2 == 1:
   if n >= 0:
        print("the number is positive and odd")
else:
        print("the number is negative and odd")
