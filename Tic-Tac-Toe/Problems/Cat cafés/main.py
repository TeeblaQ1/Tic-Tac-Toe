lst = []
while True:
    text = input().split()
    if 'MEOW' not in text:
        lst.append(text[0])
        lst.append(text[1])
    else:
        break
new_lst = [int(x) if x.isdigit() else x for x in lst]
maxi = max(new_lst[1::2])
i = 0
for elem in new_lst:
    if elem == maxi:
        print(new_lst[i - 1])
        break
    i += 1
