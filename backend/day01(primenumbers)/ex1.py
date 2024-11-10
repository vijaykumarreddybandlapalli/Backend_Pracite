start = 1
end = 100
prime_count = 0

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
print("Total prime numbers between", start, "and", end, "are:", prime_count)