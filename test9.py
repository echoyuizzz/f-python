from functools import reduce
def str2float(s):
    n = 0
    for i in s:
        if i == '.':
            break
        n = n+1
    def zuobian(x,y):
        return x*10 + y
    a = reduce(zuobian,map(int,s[:n]))
    b = reduce(zuobian,map(int,s[(n+1):]))
    return a + b/(10**(len(s[(n+1):])))
print( str2float('123.456'))
