# modelo Ising bidimensional
import numpy as np
import matplotlib.pyplot as plt
from math import exp

def plotrede(l,t,s):
    x, y  = np.meshgrid(range(l), range(l))
    plt.pcolormesh(x, y, s, cmap = plt.cm.gray) #Cor preta = 1, cor branca = -1
    plt.title('Temperatura = %f'%t)
    plt.savefig('./plots/en.png')

def interação(s,i,j):
    #Condições periódicas de contorno já incluso.
    sint = s[i,j] * (s[(i+1) % l,j] + s[(i-1) % l,j] + s[i,(j-1) % l] + s[i,(j+1) % l]) 
    return sint

def caminhada(s,e,m,l,l2,t,mcs):
    e1 = m1 = me = mm = contador = 0
    for passo in range(mcs):
        i = np.random.randint(0, l-1)
        j = np.random.randint(0, l-1)
        de = 2 * interação(s,i,j)

        if de < 0 or np.random.random() < exp(-de/t):
            s[i,j] *= (-1)
            m += 2*s[i, j]
            e += de

        if passo > 30000: #Descarte dos passos iniciais para termalizar o sistema.
            e1  += e
            m1  += m
            contador += 1

    norma = 1/(contador*l2)

    me  = e1  * norma  #<e>
    mm  = m1  * norma  #<m>

    energia.append(me)
    magnetização.append(mm)

# Visualização da configuração final da rede:
    plotrede(l,t,s)

#Início da simulação:
if __name__ == '__main__':
    
#parâmetros iniciais do sistem de spins:
    l = int(input("Insira o tamanho lateral da rede: "))
    l2=l*l
#mcs = int(input("Insira o número de passos de Monte Carlo: "))
    mcs = 500000
    energia = []
    magnetização = []
    temperatura = []

#Cálculo da energia inicial da rede de spins e da magnetização
    t = 0
    while t < 5:
        t += 0.25
        print(f"T = ", t)
        s = np.random.choice([1], size = (l ,l))    # Todos os spins são up (s = 1)
        e = (-2)*np.sum(s)                          # Energia da rede
        m = np.sum(s)                               # Magnetização da rede
        temperatura.append(t)
        caminhada(s,e,m,l,l2,t,mcs)

    #Visualização dos resultados
    plt.xlabel('Temperatura')
    plt.ylabel('Magnetização')
    plt.plot(temperatura, magnetização)
    plt.savefig('./plots/mag.png')

    plt.xlabel('Temperatura')
    plt.ylabel('Energia')
    plt.plot(temperatura, energia)
    plt.savefig('./plots/en.png')