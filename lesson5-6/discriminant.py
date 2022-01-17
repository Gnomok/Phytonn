import math
print('Решим квадратное уравнение ax^2+bx+c=0')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c
if d > 0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print(f"первый корень {x1}, \nвторой корень {x2}")
elif d==0:
    x=-b/2*a
    print(f"Корень {x}")
else:
    print('Корней нету')
