import matplotlib.pyplot as plt
from numpy.random import normal
from scipy.stats import norm
from numpy import mean, std

sample =  normal(loc = 30, scale = 3, size=300)
sample_mean = mean(sample)
sample_std = std(sample)
dist = norm(sample_mean, sample_std)
values = [value for value in range(20,40)]
probabilitas = [dist.pdf(values) for values in values]
plt.figure(figsize=(5,4))   
plt.hist(sample,bins=10 ,density=True)
plt.plot(values, probabilitas)
plt.show()