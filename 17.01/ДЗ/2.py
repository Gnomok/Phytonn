print("подсчитать количество цифр записи целого положительного числа")
n= int(input("введите число"))
r = len(str(n))
for t in range(r+1):
    n=n/10
print(t)
