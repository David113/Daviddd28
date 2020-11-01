# Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
#Дан число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
#Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).

print('''
Возможные направления робота:
11 - север
12 запад
13 - юг
14 - восток

Возможные маневры робота:
0 - продолжение движения
1 - поворот налево
-1 - поврот направо
''')

#Направление робота
napr = int(input("Введите направление робота:  "))

if napr == 11:
    print("Робот движется на север")
if napr == 12:
    print("Робот движется на запад")
if napr == 13:
    print("Робот движется на юг")
if napr == 14:
    print("Робот движется на восток")

#Маневры робота
pov = int(input("Введите маневр робота:  "))

if napr == 11 and pov == 0:
    print("Робот продолжил движение на север")
if napr == 11 and pov == 1:
    print("Робот свернул налево и двинулся на запад")
if napr == 11 and pov == -1:
    print("Робот свернул направо и двинулся на воток")

if napr == 12 and pov == 0:
    print("Робот продолжил движение на запад")
if napr == 12 and pov == 1:
    print("Робот свернул налево и двинулся на юг")
if napr == 12 and pov == -1:
    print("Робот свернул направо и двинулся на север")

if napr == 13 and pov == 0:
    print("Робот продолжил движение на юг")
if napr == 13 and pov == 1:
    print("Робот свернул налево и двинулся на восток")
if napr == 13 and pov == -1:
    print("Робот свернул направо и двинулся на запад")

if napr == 14 and pov == 0:
    print("Робот продолжил движение на восток")
if napr == 14 and pov == 1:
    print("Робот свернул налево и двинулся на север")
if napr == 14 and pov == -1:
    print("Робот свернул направо и двинулся на юг")