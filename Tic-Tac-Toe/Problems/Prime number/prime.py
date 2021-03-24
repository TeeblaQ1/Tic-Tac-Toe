prime_numbers = []
for num in range(2, 1000):
    if num > 2:
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            prime_numbers.append(num)
    elif num == 2:
        prime_numbers.append(num)
print(prime_numbers)
