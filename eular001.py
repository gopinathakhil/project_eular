numbers_below = 1000
multiples_of_3_or_5 = []                    
for i in range(numbers_below):
    if i%3==0:
        multiples_of_3_or_5.append(i)
    else:
        if i%5==0:
            multiples_of_3_or_5.append(i)

print(sum(multiples_of_3_or_5))