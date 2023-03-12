# Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


num = int(input())
count_tails = 0
count_eagle = 0
for i in range(num):
    coins = int(input())
    if coins == 0:
        count_tails += 1
    else:
        count_eagle += 1
if count_eagle > count_tails:
    print(count_tails)
else:
    print(count_eagle)
