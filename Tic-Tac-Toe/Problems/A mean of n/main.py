n = int(input())
counter = 0
result = 0

for _ in range(0, n):
    int_ = int(input())
    counter += 1
    result = result + int_

mean = float(result / counter)
print(mean)
