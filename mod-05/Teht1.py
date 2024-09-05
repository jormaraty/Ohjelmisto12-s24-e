# from random import randint
import random

maara = int(input("Arpakuutioiden määrä: "))
summa = 0   # noppien summa on aluksi nolla

for i in range(maara):
    # kuutio = randint(1,6)
    kuutio = random.randint(1, 6)
    summa = summa + kuutio

print(f"Kuutioiden summa: {summa}")