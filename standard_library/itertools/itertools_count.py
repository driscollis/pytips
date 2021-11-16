from itertools import count

for i in count(10):
    if i > 20:
        break
    else:
        print(i)
        