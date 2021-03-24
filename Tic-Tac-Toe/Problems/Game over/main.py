scores = input().split()
# put your python code here

i_counter = 0
c_counter = 0
for char in scores:
    if char == 'I':
        i_counter += 1
    else:
        c_counter += 1
    if i_counter == 3:
        print("Game over")
        print(c_counter)
        break
else:
    print("You won")
    print(c_counter)
