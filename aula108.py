#count é um iterador sem fim
from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)
print()
print('range')
for i in r1:
    print(i)