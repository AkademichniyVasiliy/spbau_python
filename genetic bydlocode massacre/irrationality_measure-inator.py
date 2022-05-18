import math
import random
import numpy

def c_fraction(x):          # Строим цепную дробь числа
    fraction = []
    q = math.floor(x)
    fraction.append(q)
    x = x - q
    i = 0
    while x != 0 and i < 25:
        q = math.floor(1/x)
        fraction.append(q)
        x = 1 / x - q
        i = i + 1
    return fraction

def fitness(x):                     # Определяем, насколько число иррационально
    candidate = c_fraction(x)
    score = 0
    for i in range(len(candidate)):
        score += 1/candidate[i] * (1/10)**i   # Чем число меньше и "ближе к левой части" дроби, тем выше score
    return score

def population(samples):
    specimen = [0 for i in range(samples)]
    gen_score = [0 for i in range(samples)]
    for gen in range(50):                       
        for i in range(samples):
            if specimen[i] == 0:
                specimen[i] = random.uniform(1, 2)
                gen_score[i] = fitness(specimen[i])
        if gen != 49:
            for i in range(samples):
                if specimen[i] < numpy.percentile(specimen, 50):    # Заменяем 50% самых рациональных чисел нулями, на место нулей генерируем новые числа
                    specimen[i] = 0
    sorted_by_score = zip(specimen, gen_score)
    sorted_by_score = list(sorted(sorted_by_score, key=lambda x: x[1])) # Сортируем по score'у
    for i in range(samples):
        print('Number and its score: ', sorted_by_score[i])
        print('Continued fraction: ', c_fraction(specimen[i]))
        
        
print(population(68))

    
        
    

    
    
        


