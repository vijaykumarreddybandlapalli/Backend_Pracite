from turtledemo.penrose import start

num =int(input("Enter the num:"))
a=0
b=1
print(f"prev num1 :{a}")
print(f"prev num2 :{b}")
while num-2:
    temp = a +b
    a = b
    b = temp
    num = num - 1
    print(f"previous :{temp} times")
# Enter the num:12
# prev num1 :0
# prev num2 :1
# previous :1
# previous :2
# previous :3
# previous :5
# previous :8
# previous :13
# previous :21
# previous :34
# previous :55
# previous :89