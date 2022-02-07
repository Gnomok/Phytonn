#user1 = {'color': "green", 'points': 5, 'speed': 250}
#user2 = {'color': "green", 'points': 5, 'speed': 250}
#user3 = {'color': "green", 'points': 5, 'speed': 250}
#player = [user1, user2, user3]
#print(player)
#for i in player:
#    print(i)
player = []
for i in range(30):
    user1 = {'color': "green", 'points': 5, 'speed': 250}
    player.append(user1)
print(player)
for i in player:
    print(i)
a = len(player)
print("-"*30)
print(f"Количество игроков {a}")
