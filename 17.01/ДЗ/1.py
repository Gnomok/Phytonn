print("k!=1*2*3*...*k")
k=int(input("Введите k"))
f=1
for t in range(1, k+1):
    f*=t
print(f)
