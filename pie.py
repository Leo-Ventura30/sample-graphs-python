import matplotlib.pyplot as plt 
import numpy as np

def plota_pizza_1():
        labels = ['Corinthias', 'Palmeiras', 'Santos', 'São Paulo']
        titulos = [27, 22, 22, 22]
        cores = ['lightblue', 'green', 'lightyellow', 'red']
        explode = (0, 0, 0, 0)  # somente explode primeiro pedaço
        total = sum(titulos)
        plt.pie(titulos, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), startangle=90)

plota_pizza_1()
# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
plt.axis('equal') 
plt.show()