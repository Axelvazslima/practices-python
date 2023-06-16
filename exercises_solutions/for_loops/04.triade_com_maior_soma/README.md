# Soma de Tríades (Encontrar a Maior)

Uma tríade em uma sequência de números inteiros é formada por 3
elementos consecutivos da sequência. Logo, para saber todas as
tríades de uma sequências basta, a partir da posição inicial,
agrupar 3 elementos vizinhos (janela de 3 elementos) e deslizar
essa janela uma posição à direita até chegar no úlyimo
agrupamento possível. Por exemplo, a lista **[3, 1, 0, 4, -5]**
possui as seguintes possíveis tríades: **(3, 1, 0)**, **(1, 0,
4)** e **(0, 4, -5)**.

Escreva um programa que recebe uma lista de inteiros e determina
a tríade com a maior soma. No exemplo acima, a soma da maior
tríade seria 5 da tríade **(1, 0, 4)**.

## Entrada

O programa deve ler uma sequência de inteiros separados por um
espaço em branco. **IMPORTANTE:** assume que a sequência tem pelo
menos 3 números

# Saída

Na saída, seu programa deve imprimir a maior soma entre todas as
tríades e as posições que formam a tríade de maior soma. **Se mais
de uma tríade tiver o mesmo valor da maior soma, considerar a
última tríade que tem o valor derssa maior soma**. Veja os
exemplos abaixo para entender o formato esperado na saída. O
segundo exemplo mostra a situação que mais de uma tríade possui o
mesmo valor da maior soma.

# Restrições e Permissões

É permitido o uso do ** split()** para separar os elementos da
sequência lida na entrada. Não é permitido usar funções prontas
que iterem sobre listas. Por exemplo, sum() e map().



# Exemplos de Execução

```
$ python3 solucao.py
3 1 0 4 -5
maior soma: 5
tríade: posições 1, 2 e 3
```

```
$ python3 solucao.py
1 2 3 1 1 3 1 2
maior soma: 6
tríade: posições 5, 6 e 7
```


