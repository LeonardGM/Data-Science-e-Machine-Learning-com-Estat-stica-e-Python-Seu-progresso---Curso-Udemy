import pandas as pd
import matplotlib.pyplot as plt 
import statistics as stats

valores = [4,6,6,7,11,6,13,18,21,24,26,27,35,36,36,42,43,45,49]

#media

print(stats.mean(valores))
print(sum(valores)/len(valores))

#mediana

print(stats.median(valores))

#moda

print(stats.mode(valores))