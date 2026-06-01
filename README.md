# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema         | Link                                            | Dificuldade |
| - | ------------------------ | ----------------------------------------------- | ----------- |
| 1 | 71A - Way Too Long Words | https://codeforces.com/problemset/problem/71/A  | 800         |
| 2 | 231A - Team              | https://codeforces.com/problemset/problem/231/A | 800         |

 
---
 
## Problema 1 — Way Too Long Words 
 
### O que o problema pede?

Ao ler este problema, pensei em uma situação em que eu precisasse preparar uma publicação com espaço limitado. Para que palavras muito longas não ocupassem tanto espaço, elas precisariam ser abreviadas. Já as palavras menores poderiam continuar escritas normalmente.

Com esse entendimento, interpretei que o objetivo do exercício é analisar várias palavras e verificar o tamanho de cada uma delas. Quando a palavra possui mais de 10 letras, ela deve ser abreviada utilizando a primeira letra, a quantidade de letras do meio e a última letra. Caso contrário, a palavra é exibida normalmente.
 
### Como eu resolvi?

Para resolver este problema, pensei primeiro na situação que imaginei anteriormente: se eu tivesse um espaço limitado para uma publicação, precisaria identificar quais palavras eram grandes demais e quais poderiam permanecer da forma original.

Com essa ideia, analisei cada palavra separadamente e verifiquei a quantidade de letras que ela possuía. Quando a palavra tinha mais de 10 letras, utilizei a primeira letra, contei quantas letras ficaram no meio e depois acrescentei a última letra, formando uma versão abreviada. Quando a palavra tinha 10 letras ou menos, mantive a palavra original sem alterações.

Depois transformei essa lógica em código utilizando Python para que o processo fosse realizado automaticamente para todas as palavras informadas.

 
### Código
```python

### Código

```python
n = int(input())

for i in range(n):
    palavra = input()

    if len(palavra) > 10:
        print(palavra[0] + str(len(palavra) - 2) + palavra[-1])
    else:
        print(palavra)
```


 
---
 
## Problema 2 — [Nome do Problema]
 
### O que o problema pede?
 
 
### Como eu resolvi?
 
 
### Código
```python
# Cole seu código aqui
```
 
---
 
## Problema 3 — [Nome do Problema]
 
### O que o problema pede?
 
 
### Como eu resolvi?
 
 
### Código
```python
# Cole seu código aqui
```
 
<!-- Remova as linhas dos problemas que não foram resolvidos caso tenha escolhido menos de 3.-->

---
 
## IA utilizada
 
**Qual IA você usou?**
<!-- Ex: Claude, ChatGPT, Gemini... -->
 
**Como a IA te ajudou?**
<!-- Descreva como você usou a IA no processo. Ela explicou o problema? Sugeriu uma estratégia? Ajudou a corrigir um erro? -->
 
---
 
## Reflexão
 
### Dificuldades encontradas
<!-- O que foi mais difícil? Entender o problema? Escrever o código? Usar o GitHub? -->
 
 
### O que aprendi
<!-- O que você aprendeu de novo com este desafio? Pode ser sobre programação, sobre usar IA, ou qualquer coisa. -->
 
 
### Como foi a experiência?
<!-- Conta um pouco como foi no geral. O que mais gostou? O que mudaria? -->
