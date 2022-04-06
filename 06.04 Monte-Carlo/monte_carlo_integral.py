from random import uniform
from math import exp  
import matplotlib.pyplot as plt       
area = 0
#интегрируем e^(-x^2)

def integral(n):                    #геометрический вариант алгоритма Монте-Карло, n раз сравниваем рандомный y со значением функции 
    under = 0
    for i in range(n):
        x = uniform(-25, 25)
        y = uniform(0, 1)
        if y <= exp(-x**2):
            under += 1
    return 50*1*under/n             #(площадь прямоугольника, охватывающего наши x и y) * (отношение точек под графиком ко всем точкам)

                                    #обычный алгоритм Монте-Карло, используя теорему о среднем и всё такое
def approx_int(n):                  #изначальный вариант, n иксов выбираются случайно из [-25, 25], функция uniform обеспечивает равномерное распределение
    summa = 0 
    for i in range(n):
        x = uniform(-25, 25)
        fx = exp(-(x**2))     
        summa += fx
    return summa*50/n        


def approx_int_improved(n):     
    total = 0
    for tries in range(500):
        summa = 0 
        for i in range(n):
            x = uniform(-25, 25)
            fx = exp(-(x**2))   
            summa += fx
        total += summa*50/n
    return total/500

def approx_int_plot(n, samples):    #построим график распределения площадей
    total = 0
    areas = []
    for tries in range(samples):
        summa = 0 
        for i in range(n):
            x = uniform(-25, 25)
            fx = exp(-(x**2))   
            summa += fx
        total += summa*50/n
        areas.append(summa*50/float(n))
    print(total)
    global area 
    area = total/samples
    print(area)
    return areas


#result0 = geometric_int(10_000)
#print(f"Интеграл e^(-x^2) приближенно равен {result0}, погрешность около {abs(result0/sqrt(pi)-1)*100} процента")
#result1 = approx_int(10_000)
#print(f"Интеграл e^(-x^2) приближенно равен {result1}, погрешность около {abs(result1/sqrt(pi)-1)*100} процента")
#result2 = approx_int_improved(10_000)
#print(f"Интеграл e^(-x^2) приближенно равен {result2}, погрешность около {abs(result2/sqrt(pi)-1)*100} процента")
areas = approx_int_plot(10000, 1000)
plt.title(f"Распределение посчитанных площадей, интеграл ≈{area}")
plt.hist(areas, bins = 20, ec = 'black')
plt.xlabel("Площадь")
plt.ylabel("Количество")
plt.show()



    
