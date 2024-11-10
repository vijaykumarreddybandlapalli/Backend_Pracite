# sum_n(10) returns 10 + sum_n(9)
# sum_n(9) returns 9 + sum_n(8)
# sum_n(8) returns 8 + sum_n(7)
# sum_n(7) returns 7 + sum_n(6)
# sum_n(6) returns 6 + sum_n(5)
# sum_n(5) returns 5 + sum_n(4)
# sum_n(4) returns 4 + sum_n(3)
# sum_n(3) returns 3 + sum_n(2)
# sum_n(2) returns 2 + sum_n(1)
# sum_n(1) returns 1 + sum_n(0)
# sum_n(0) returns 0
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

result = sum_n(10)
print(result)