from functools import reduce
def au(L):
    def ass(a,b):
        S = a * b
        return S
    return reduce(ass,L)
print('3 * 5 * 7 * 9 =', au([3, 5, 7, 9]))
if au([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

