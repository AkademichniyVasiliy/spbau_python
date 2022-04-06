import numpy as np
import matplotlib.pyplot as plt
from random import uniform
volume = 0
def sphere_integral(n, r):                                                              #Просто считаем объем сферы по методу Монте-Карло
    count = 0
    for i in range(n):
        coordinates = np.random.uniform(-r, r, 3)
        if coordinates[0]**2 + coordinates[1]**2 + coordinates[2]**2 <= r**2:
            count += 1
    return (2*r)**3*count/n


def sphere_integral_points(n, r):                                                           #Можно построить график, посмотреть распределение наших случайных величин    
    points = []
    count = 0                                                                               #Для этого сохраняем полученные рандомные точки в массив
    for i in range(n):
        coordinates = np.random.uniform(-r, r, 3)
        if coordinates[0]**2 + coordinates[1]**2 + coordinates[2]**2 <= r**2:
            count += 1
        points.append([coordinates[k] for k in range(3)])
    global volume 
    volume = (2*r)**3*count/n
    return points
        

def sphere_plot(r, points):                                                                   #Строим сферу
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='pink', alpha = 0.3)

    Set1 = plt.cm.get_cmap("Set1")                                                            #На сферу вываливаем наши точечки
    xs, ys, zs = [], [], []
    for i in range(len(points)):
        xs.append(points[i][0])
        ys.append(points[i][1])
        zs.append(points[i][2])

    l = ax.scatter(xs, ys, zs, c=zs, cmap=Set1)
    plt.title(f"Интеграл по объему приближённо равен {volume}")
    plt.show()                                                                               #Осталось добавить соль и перец по вкусу





#print(sphere_integral(10_000, 1))
print(sphere_plot(1, sphere_integral_points(1000, 1)))
