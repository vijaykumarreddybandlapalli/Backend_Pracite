def flip_all(s):
    return ''.join('1' if c == '0' else '0' for c in s)

def flip_odd(s):
    return ''.join(s[i] if i % 2 == 0 else ('1' if s[i] == '0' else '0') for i in range(len(s)))

def flip_even(s):
    return ''.join(('1' if s[i] == '0' else '0') if i % 2 == 0 else s[i] for i in range(len(s)))

def flip_3k1(s):
    return ''.join(('1' if s[i] == '0' else '0') if (i - 1) % 3 == 0 else s[i] for i in range(len(s)))

def distinct_final_strings(N, M, operations):
    initial_string = '1' * N  # Start with all '1's
    current_strings = {initial_string}  # Use a set to store unique strings

    for _ in range(M):
        next_strings = set()  # Prepare for the next iteration
        for s in current_strings:  # Iterate over current unique strings
            for op in operations:
                if op == 1:
                    next_strings.add(flip_all(s))
                elif op == 2:
                    next_strings.add(flip_odd(s))
                elif op == 3:
                    next_strings.add(flip_even(s))
                elif op == 4:
                    next_strings.add(flip_3k1(s))
        current_strings = next_strings  # Move to the next iteration's results

    return len(current_strings)  # Return the count of unique strings

# Input handling
T = int(input())
for _ in range(T):
    try:
        N, M = map(int, input().split())
        operations = list(map(int, input().split()))
        result = distinct_final_strings(N, M, operations)
        print(result)
    except ValueError:
        print("Invalid input format. Please enter two integers for N and M.")
