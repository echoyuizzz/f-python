temp = [1,2,3,4,5,5,4,3,1,0]
a = []
for i in temp:
    if i not in a:
        a.append(i)
print(a)