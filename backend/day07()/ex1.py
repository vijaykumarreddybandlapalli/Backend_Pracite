x= 5
y= 10
print(f"")
x=x+y
x=x+y
y =x-y
x =x-y
print(x+y)
# single line swapping
a1="vijay"
a2="bhanu"
a3="gannu"

print(f"before swap a1 and a2:{a1,a2}")
a2,a1=a1,a2
print(f"after swap a1 and a2:{a1,a2}")


# using third swap
# a=100
# b=200
# temp=a<b
# print(temp)
num =int(input("Enter the num:"))
a=0
b=1
while num-2:
    temp=a
    a=a+b
    b=temp
    print(f"prev num :{b}")
    num=num-1
# Enter the num:12
# prev num :0
# prev num :1
# prev num :1
# prev num :2
# prev num :3
# prev num :5
# prev num :8
# prev num :13
# prev num :21
# prev num :34

