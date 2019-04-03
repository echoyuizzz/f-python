
h = input('输入你的身高:')

w = input('输入你的体重:')
height = float(h)
weight = float(w)

bmi=weight/(height*height)
print(bmi)
if bmi < 18.5:
    print('轻')
elif bmi <= 25:
    print('型男')
elif bmi <= 32:
    print('肥胖')
else:
    print('你可真尼玛胖死了')