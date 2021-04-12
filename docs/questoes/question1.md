# Questão 1

Aqui um peseudocódigo:

1. D1
 database 1
2. D2 
  database 2
3. d1_menor, d1_maior, d2_menor, d2_maior 
  representam os subarrays que estamos restringindos nossa atenção

```

AcharMediana(D1, d1_menor, d1_maior, D2, d2_menor, d2_maior) {
  Se (d1_menor igual a d1_maior) entao
    m1 = ao único valor de D1
    m2 = ao unico valor de D2
    retornar min(m1, m2)
  fimSe

  j = (d1_maior + d1_menor - 1)/2
  m1 = ao j-ésimo menor termo de D1
  k = (d2_maior + d2_menor - 1)/2
  m2 = ao k-ésimo menor termo de D2

  Se (m1 < m2>) entao
    retornar AcharMediana (D1, m1+1, d1_maior, D2, d2_menor, m2)
  Senao
    retornar AcharMediana (D1, d1_menor, m1, D2, m2+1, d2_maior)
  fimSe
}
```

Primeira linha de comando "AcharMediana (D1, 1, n, D2, 1, n)"