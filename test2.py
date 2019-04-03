def s(n):
    if n < 1:
        print('输入错误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return (s(n-1)+s(n-2))
sub = s(5)
if sub != -1:
    print(sub)
