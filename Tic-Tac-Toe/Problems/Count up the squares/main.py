# put your python code here
num = 0
i = 0
squares = 0
while True:
    digits = int(input())
    if digits == 0 and i < 1:
        print(i)
        break
    i += 1
    num = num + digits
    squares = squares + (digits ** 2)
    if num == 0:
        print(squares)
        break
