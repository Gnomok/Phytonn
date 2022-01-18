a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("Треугольник не существует")
else:
    if a==b and b==c:
        print("Треугольник Равносторонний")
    elif a==b or b==c :
        print("Равнобе.")
    else:
        print("Разно.")
