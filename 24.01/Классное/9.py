user = ['u1','u2' ,'u3' ,'u4']
user_v = []

while user:
    del_user = user.pop(0)
    user_v.append(del_user)
    v = f"{del_user} будет верифицирован на вашем сайте"
    print(v)

print(user)
print(user_v)
