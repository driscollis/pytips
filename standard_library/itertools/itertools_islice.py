from itertools import count, islice

for i in islice(count(10), 5):
    print(i)