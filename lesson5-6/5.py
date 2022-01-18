print("введите координаты точки A(x;y)")
x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print("в 1 четверти")
elif x<0 and y>0:
    print("в 2 четверти")
elif x<0 and y<0:
    print("в 3 четверти")
else:
    print("в 4 четверти")
