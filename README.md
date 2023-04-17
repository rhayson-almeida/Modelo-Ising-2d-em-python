# Modelo Ising 2d em python

## Sobre o modelo:

O hamiltonino desse sistema é dado por:

$$\hat{H} = - J \sum_{\langle i, j \rangle} s_i s_j - H \sum_i^{N} s_i$$
no qual $s$ são os spins localizados nos vértices de uma rede quadrada que podem apontar ou para cima ($s = 1$) ou para baixo ($s = -1$). $H$ é o campo magnéticos externo e $J$ é a constante de acoplamento dos spins. Se $J > 0$, os pares de spin apontam na mesma direção, isto é, fase ferromagnética. Se $J < 0$, os pares de spin apontam em direções opostas, isto é, fase ferromagnética. No main.py $J = 1$ e $H = 0$.

Quando o sistema está em equilíbrio térmico, a rede cristalina e os spins terão os graus de liberdade descritos por uma temperatura $T$. Com $J >0$ e $H = 0$ em altas temperaturas ($T >> J/k_B$), o sistema se encontra na fase paramagnética, ou seja, os spins apontam em ambas as direções com igual frequência, portanto, nenhuma direção sendo privilegiada e, consequentemente, o momento magnético total é zero. Em baixas temperaturas, ($T << k_B$) os spins tendem a se linhar ao longo de uma direeção particular no espaço, mesmo na ausência de campo externo, ou seja, existeuma magnétização espontânea e, portanto, o sistema se encontra na fase ferromagnética. 

A característica distintiva da maioria das transições de fase é o parâmetro de ordem, ou seja, de alguma propriedade do sistema que é diferente de zero na fase ordernada, mas nula na fase desordadena. No caso do sistem Ising bidimensional, o parâmetro de ordem nesse sistema é definido como o a magnetização por spin da rede cristalina:

$$ m = \frac{1}{N} \left\langle \sum_{i = 1}^{N} s_i \right\rangle $$

## O algoritmo de Metropolis
