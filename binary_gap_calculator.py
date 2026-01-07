A = bin(int(37)).lstrip('0b')

print(A)
zero_counter = 0
max_counter = 0
started = False
for i in range(len(A)):
    if A[i] == '1':
        if started:
            max_counter = max(max_counter, zero_counter)
        started = True
        zero_counter = 0
    elif A[i] == '0' and started:
        zero_counter += 1
print(max_counter)
