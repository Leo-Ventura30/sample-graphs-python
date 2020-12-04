import matplotlib.pyplot as plt 
import numpy as np

pop = {"São Paulo": 12000000, "Rio": 7000000, "Salvador": 4000000, "Recife": 3500000, "Porto Alegre": 2500000}
cidades = [i for i in pop.keys()]
populacao = [j for j in pop.values()]
popPos = np.arange(len(cidades))
azul = "blue"
verde = "green"
preto = "black"

def plota_barra_h_1():
        plt.barh(popPos, populacao, align='center', color=azul)
        plt.yticks(popPos, cidades)
        plt.xlabel('População')
        plt.title('População de cidades brasileiras')
        
plota_barra_h_1()
plt.show()