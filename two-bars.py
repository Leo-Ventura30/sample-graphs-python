import matplotlib.pyplot as plt 
import numpy as np

pop = {"São Paulo": 12000000, "Rio": 7000000, "Salvador": 4000000, "Recife": 3500000, "Porto Alegre": 2500000}
cidades = [i for i in pop.keys()]
populacao = [j for j in pop.values()]
popPos = np.arange(len(cidades))
azul = "blue"
verde = "green"
preto = "black"
def plota_bar_dupla_1():
        grupos = 5
        media_chico = (9.1, 5.4, 4.0, 7.5, 7.0)
        media_joao = (8.6, 6.3, 5.5, 3.5, 5.6)
        # fig, ax = plt.subplots()
        indice = np.arange(grupos)
        bar_larg = 0.4
        transp = 0.7
        plt.bar(indice, media_chico, bar_larg, alpha=transp, color=azul, label='Chico')
        plt.bar(indice + bar_larg, media_joao, bar_larg, alpha=transp, color=verde, label='João')
        plt.xlabel('Matéria') 
        plt.ylabel('Notas') 
        plt.title('Notas por pessoa') 
        plt.xticks(indice + bar_larg, ('Matemática', 'Português', 'Biologia', 'Física', 'Química')) 

plota_bar_dupla_1()
plt.legend() 
plt.tight_layout() 
plt.show()