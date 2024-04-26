a = 1
b = 2
sum = 0
while b<4000000:
    c = a + b
    a = b
    b = c
    if a%2==0:
        sum = sum + a
        print(a)
print(sum)
