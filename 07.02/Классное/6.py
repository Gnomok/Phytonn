speed =(input('Какую скорость ты предпочитаешь'))
massive = {'x': 0, 'y': 25, 'speed': speed}
print(f"Оригинальная позиция игрока {massive['x']}")

if massive['speed'] == 'slow':
    x_inc = 1
elif massive['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3
massive['x'] += x_inc
print(f"Новая позиция игрока {massive['x']}")
