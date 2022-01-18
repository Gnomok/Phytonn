print("s=1/2+1/4+1/8+...")
n= int(input("введите количество слагаемых"))
s=0
i=1
a=1/2
while i<=n:
    s+=a
    i+=1
    a/=2
print(s)
