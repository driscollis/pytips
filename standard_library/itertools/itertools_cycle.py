from itertools import cycle

count = 0
for item in cycle('XYZ'):
     if count > 7:
          break
     print(item)
     count += 1
