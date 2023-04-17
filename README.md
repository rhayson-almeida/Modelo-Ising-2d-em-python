# Modelo Ising 2d em python

O hamiltonino desse sistema é dado por:

$$\hat{H} = - J \sum_{\langle i, j \rangle} s_i s_j - H \sum_i^{N} s_i$$
no qual $s$ são os spins localizados nos vértices que podem apontar ou para cima ($s = 1$) ou para baixo ($s = -1$). $H$ é o campo magnéticos externo e $J$ é a constante de acoplamento dos spins. Se $J > 0$, os pares de spin apontam na mesma direção, isto é, fase ferromagnética. Se $J < 0$, os pares de spin apontam em direções opostas, isto é, fase ferromagnética.
