import random

#1 ----------------------------------------------------------------------

s = 0
for i in range(10):
    x = int(input()
    print(x, end = " ")
    s += x
print()
print('Sum =', s)

#3 ---------------------------------------------------------------------

n = 0
for i in range(10):
    y = int(input())
    print(y, end = " ")
    n += y
print()
print('Arithmetic mean =', n / 10)

#5 ----------------------------------------------------------------------

N = random.randrange(1,10)
print("N =",N)
s = 0
for i in range(N):
    x = random.uniform(0, 10)
    y = int(x)
    s += y
    print(y," : ",s," : ",x)
print()
print('Sum =', s)

#8 ----------------------------------------------------------------------

N = int(input())
print("N =",N)
K = 0
for i in range(N):
    x = random.randrange(0, 10)
    if x % 2 == 0:
        print(x)
        K += 1

#12 ---------------------------------------------------------------------

s = 1
for i in range(10):
    x = random.randrange(1, 5)
    print(x, end = " ")
    s *= x
print()
print('Inc =', s)

#3 ---------------------------------------------------------------------

s = 0
for i in range(10):
    x = random.randrange(1, 5)
    print(x, end = " ")
    s += x
print()
print('Arithmetic mean =', s / 10)

#12 ------------------------------------------------------------------

x = random.randrange(1, 10)
print(x, end='; ')
k = 0

while x != 0:
    x = random.randrange(-6, 7)
    print(x, end='; ')
    k += 1
    
print() # для enter между строками вывода
print("Amount:", k)

#13 ---------------------------------------------------------------------

x = random.randrange(1, 10)
print(x, end='; ')
k = 0

if x > 0 and x % 2 == 0:
    k += x
        
while x != 0:
    x = random.randrange(-6, 5)
    print(x, end='; ')
    
    if x > 0 and x % 2 == 0:
        k += x
    
print()
print("Sum:", k)

#26 ------------------------------------------------------------------

N = random.randrange(3, 10)
k = random.randrange(2, 5)

for i in range(N):
    i **= k
    print(i, end="; ")

#14 --------------------------------------------------------------------

K = random.randrange(-3, 5)
print("K =", K)
x = random.randrange(1, 10)
k = 0
 
while x != 0:
    if x < K:
        k += 1
    x = random.randrange(-5, 6)
    print(x, end = '; ')
    
print()
print("Less then K:", k)