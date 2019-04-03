# 系数a、b为零，c不为零此时是一个不等式
if a == 0 and b == 0 and c != 0:
    print('无解')

# 系数a为零，b不为零是一元一次方程
elif a == 0 and b != 0:
    print('此方程为一元一次方程,解为:X=', -c / b)

# 系数a、c不为零，b为零此时是一元二次方程
elif a != 0 and b == 0 and c != 0:
    if - c / a < 0:
        return '无解'
    else:
        num1 = '{0:.1f}'.format(math.sqrt(-c / a))
        num2 = '{0:.1f}'.format(-math.sqrt(-c / a))
        print('该一元二次方程有两个解为:X1 =', num1, ', X2 =', num2)