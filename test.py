s = [(1, 2, 4), (5, 6, 8), (4, 5, 7)]
taco = 0
for i in s:


    for g in i:


        if g == 4:
            taco = 1
    if taco == 1:
        s.remove(i)
print(s)


