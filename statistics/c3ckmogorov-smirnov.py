import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm, kstest
import math

data = pd.read_excel('D:\Program Files\Python VS Code\statistics\p4nis_values.xlsx')
loc, scale = norm.fit(data)
n = norm(loc=loc, scale=scale)
print(n)

plt.hist(data, bins=50)

mu = 13.78
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, 25*norm.pdf(x, mu, sigma))
plt.title("Penis length averaged by country \n(we can conclude that this is not normally distributed)")
plt.xlabel("Centimeters")
plt.ylabel("Number of Countries")
plt.show()

print(kstest(data, n.cdf))
