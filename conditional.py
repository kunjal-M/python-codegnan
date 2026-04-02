#check number is zero or non zero

x = int(input())
if x==0:
    print("The value is equal to zero")
else:
    print("The number is non-zero")


#check number is postive or negative

a = int(input())
if a>=0:
    print("The number is positive")
else:
    print("The number is negative")


#check number is even or odd

num = int(input())
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


#check whether number is divisible with 3 or not

num1 = int(input())
if num1 % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")


#check whether number is divisible by both 3 and 5

num2 = int(input())
if num2 % 3 == 0 and num2 % 5 == 0 :
    print("The number is divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")


#check wheather the person is eligible to vote or not

age = int(input())
if age>=18:
    print("Eligible to vote")
else:
    print("not eligible")


#find the bigger number among two numbers

x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
if x>y:
        print("x is bigger value")
else:
    print("y is bigger value")
