import random
import time

import numpy as np
import matplotlib.pyplot as plt


point = int(input('Введите желаемое число точек: '))

a = []
b = []
x = []

for i in range(0, point + 1):
    c = random.randint(60, 300)
    a.append(c)
    d = random.randint(60, 300)
    b.append(d)

for i in range(len(a)):
    x.append((a[i], b[i]))
print(x)

M = np.mean(x, axis=0)      # вычисление средних по каждой координате
D = np.var(x, axis=0)       # вычисление дисперсий по каждой координате
K = 5                       # число кластеров
ma = [np.random.normal(M, np.sqrt(D / 10), 2) for n in range(K)]        # начальные центры кластеров
ro = lambda x_vect, m_vect: np.mean((x_vect - m_vect) ** 2)             # евклидова метрика

COLORS = ('green', 'blue', 'brown', 'black', 'purple')     # цветов должно быть не меньше кластеров (>= K)

plt.ion()
n = 0
while n < 10:
    X = [[] for i in range(K)]                  # инициализация пустого двумерного списка для хранения объектов кластеров

    for x_vect in x:
        r = [ro(x_vect, m) for m in ma]         # вычисление расстояний для текущего образа до центров кластеров
        X[np.argmin(r)].append(x_vect)          # добавление образа к кластеру с ближайшим центром

    ma = [np.mean(xx, axis=0) for xx in X]      # пересчет центров кластеров

    plt.clf()
    # отображение найденных кластеров
    for i in range(K):
        xx = np.array(X[i]).T
        plt.scatter(xx[0], xx[1], s=10, color=COLORS[i])

    # отображение центров кластеров
    mx = [m[0] for m in ma]
    my = [m[1] for m in ma]
    plt.scatter(mx, my, s=50, color='white')

    plt.draw()
    plt.gcf().canvas.flush_events()
#    plt.savefig(f"lloyd {n+1}.png")
    time.sleep(0.2)

    n += 1

plt.ioff()

# отображение найденных кластеров
for i in range(K):
    xx = np.array(X[i]).T
    plt.scatter(xx[0], xx[1], s=10, color=COLORS[i])

# отображение центров кластеров
mx = [m[0] for m in ma]
my = [m[1] for m in ma]
plt.scatter(mx, my, s=50, color='red')

plt.show()
