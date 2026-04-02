# input reading from user

name = input()
print(type(name), name)

#reading integers from user

num = int(input())
print(type(num), num)

#reading float value from user

val = float(input())
print(type(val), val)

#raeding complex value from user

x = int(input())
y = int(input())
c = complex(x,y)
print(type(c), c)

#reading boolean values

n = bool(input())
print(type(n), n)

n = bool(int(input()))
print(type(n), n)

print(bool(1))
print(bool(0))
print(bool(10))
print(bool(-1))
print(bool('hi'))
print(bool(''))
print(bool(' '))
print(bool([]))
print(bool([0]))
