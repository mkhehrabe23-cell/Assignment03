import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/content/data-2.csv", encoding='latin1')

print("Available columns:", data.columns.tolist())


x = data['no2'].dropna().values


ROLL_NUMBER = 102303221

ar = 0.05 * (ROLL_NUMBER % 7)
br = 0.3 * ((ROLL_NUMBER % 5) + 1)

z = x + ar * np.sin(br * x)

mu = np.mean(z)
sigma2 = np.var(z)

lamda = 1 / (2 * sigma2)
c = np.sqrt(lamda / np.pi)

print("Estimated Parameters:")
print("mu =", mu)
print("lambda =", lamda)
print("c =", c)

z_range = np.linspace(min(z), max(z), 500)
pdf = c * np.exp(-lamda * (z_range - mu)**2)

plt.hist(z, bins=35, density=True, alpha=0.4, label="Histogram of z")
plt.plot(z_range, pdf, 'r', linewidth=2, label="Estimated PDF")
plt.xlabel("z")
plt.ylabel("Density")
plt.legend()
plt.title("Estimated Probability Density Function")
plt.show()
