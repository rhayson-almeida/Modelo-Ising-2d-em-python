# modelo Ising bidimensional
import numpy as np
import matplotlib.pyplot as plt
from math import exp

def interação(s,i,j):
    #Condições periódicas de contorno já incluso.
    sint = s[i,j] * (s[(i+1) % l,j] + s[(i-1) % l,j] + s[i,(j-1) % l] + s[i,(j+1) % l]) 
    return sint

def caminhada(s,e,m,l,l2,kt,mcs):
    se = se2 = sm = sm2 = me2 = mm2 = 0

    for passo in range(mcs):
        i = np.random.randint(0, l-1)
        j = np.random.randint(0, l-1)
        de = 2 * interação(s,i,j)

        if de < 0 or np.random.random() < exp(-de/kt):
            s[i,j] *= (-1)
            m += 2*s[i, j]
            e += de

        if passo > 30000: #Descarte dos passos iniciais para termalizar o sistema.
            se  += e
            se2 += e*e
            sm  += m
            sm2 += m*m

    norma1 = 1/(mcs*l2)
    norma2 = 1/(kt*kt*mcs*l2)
    norma3 = 1/(kt*mcs*l2)

    me  = se  * norma1                  #<e>
    me2 = se2 * norma1                #<e^2>
    mm  = sm  * norma1                  #<m>
    mm2 = sm2 * norma1                #<m^2>
    cv = (me2 - (me*me)) *  norma2     #(<e^2> - <e>^2)/T^2
    chi = (mm2 - (mm*mm)) * norma3    #(<m^2> - <m>^2)/T

    energia.append(me)
    magnetização.append(mm)
    calor.append(cv)
    susceptibilidade.append(chi)


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
    calor = []
    susceptibilidade = []

#Cálculo da energia inicial da rede de spins e da magnetização
    kt = 0
    while kt < 5:
        kt += 0.1
        print(f"T = ", kt)
        s = np.random.choice([1], size = (l ,l))    # Todos os spins são up (s = 1)
        e = (-2)*np.sum(s)                          # Energia da rede
        m = np.sum(s)                               # Magnetização da rede
        temperatura.append(kt)
        caminhada(s,e,m,l,l2,kt,mcs)

    #Visualização dos resultados
    plt.xlabel('Temperatura')
    plt.ylabel('Magnetização')
    plt.plot(temperatura, magnetização)
    plt.savefig('./mag.png')
    plt.show()

    plt.xlabel('Temperatura')
    plt.ylabel('Energia')
    plt.plot(temperatura, energia)
    plt.savefig('./en.png')
    plt.show()

    plt.xlabel('Temperatura')
    plt.ylabel('Calor Específico')
    plt.plot(temperatura, calor)
    plt.savefig('./calor.png')
    plt.show()

    plt.xlabel('Temperatura')
    plt.ylabel('Susceptibilidade magnética')
    plt.plot(temperatura, susceptibilidade)
    plt.savefig('./sus.png')
    plt.show()