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

n = int(input())

for i in range(n):
    palavra = input()

    if len(palavra) > 10:
        print(palavra[0] + str(len(palavra) - 2) + palavra[-1])
    else:
        print(palavra)
```


 
---
 
## Problema 2 —  231A - Team  
 
### O que o problema pede?

Ao ler este problema, imaginei uma situação em que três estudantes precisam decidir se conseguem resolver uma atividade em conjunto. Cada integrante informa se acredita ou não que sabe a solução do problema. A tarefa só será realizada quando pelo menos duas pessoas do grupo concordarem que conseguem resolvê-la.

Com esse entendimento, interpretei que o objetivo do exercício é analisar várias situações e verificar em quantas delas existe concordância suficiente entre os integrantes para que o problema seja resolvido.

 
### Como eu resolvi?
 
 Para resolver este problema, analisei cada equipe separadamente. Em cada situação, observei as respostas dos três integrantes, representadas pelos valores 0 e 1. Considerei que o valor 1 indicava que a pessoa tinha certeza da solução e o valor 0 indicava que ela não tinha certeza.

Em seguida, somei os valores de cada equipe. Quando o resultado da soma era 2 ou 3, considerei que pelo menos duas pessoas acreditavam conseguir resolver o problema e aumentei a contagem de problemas resolvidos. Ao final, apresentei a quantidade total de problemas que as equipes decidiram resolver.

 
### Código
```python

n = int(input())

contador = 0

for i in range(n):
    petya, vasya, tonya = map(int, input().split())

    if petya + vasya + tonya >= 2:
        contador += 1

print(contador)
```

---
 
## IA utilizada
 
**Qual IA você usou?**
<ChatGPT>
 
**Como a IA te ajudou?**
Utilizei o ChatGPT como apoio para compreender os enunciados dos problemas e aprender a lógica necessária para resolvê-los. Em vez de apenas receber a resposta pronta, procurei entender cada etapa da resolução. Fiz anotações no meu caderno, pesquisei termos no Google e também acessei o Codeforces para interpretar melhor os exercícios e compreender o significado de cada comando utilizado.

Durante o desenvolvimento, a IA me auxiliou na interpretação dos problemas, na construção da lógica de programação em Python, na correção de erros e na utilização do Visual Studio Code e do GitHub. Além disso, recebi explicações detalhadas sobre os conceitos utilizados, o que me ajudou a entender melhor o funcionamento dos códigos.

Percebi que, com a prática, fui ganhando mais confiança. No primeiro problema tive mais dificuldades para configurar o ambiente e executar o código, mas no segundo já consegui realizar várias etapas com mais facilidade. Essa experiência mostrou que aprender programação é um processo contínuo e que a prática diária contribui para o desenvolvimento do raciocínio lógico e da autonomia na resolução de problemas.
 
---
 
## Reflexão
 ### Como foi a experiência?

### Como foi a experiência?

A experiência foi desafiadora, mas também muito enriquecedora. Quando a Unicesumar divulgou a parceria com a TCS por meio da mentoria Codificadas – Além do Código, voltada especialmente para mulheres na tecnologia, minha primeira reação foi me perguntar se eu realmente deveria participar, já que não sabia programar e não tinha experiência prática na área.

Mesmo com essa insegurança, decidi participar das lives e me dedicar ao desafio porque entendi que o mais importante era o aprendizado. Durante o processo, percebi que programar não é apenas escrever códigos, mas principalmente interpretar problemas e transformar uma situação em uma sequência lógica de passos.

Uma das principais reflexões que tive foi que a prática faz muita diferença. No primeiro problema, tive mais dificuldades para entender o que fazer, configurar o ambiente e executar o código. Já no segundo problema, consegui realizar várias etapas com mais facilidade, o que mostrou que o aprendizado acontece aos poucos e se fortalece com a repetição.

Antes de iniciar a mentoria, eu acreditava que a maior dificuldade da programação seria a matemática. Porém, ao realizar os exercícios, percebi que a interpretação tem um papel muito importante. Muitas vezes, o maior desafio não foi escrever o código, mas compreender exatamente o que o problema estava pedindo para então encontrar uma solução.

Por fim, aprendi que ninguém nasce sabendo programar. É um processo que exige dedicação, paciência e prática constante. Cada erro corrigido, cada dúvida esclarecida e cada exercício resolvido representaram uma evolução no meu aprendizado. Este desafio me mostrou que, mesmo estando no início da jornada, sou capaz de aprender e desenvolver novas habilidades quando me permito enfrentar os desafios e sair da minha zona de conforto.


### Dificuldades encontradas
### Dificuldades encontradas

A principal dificuldade que encontrei foi a interpretação dos problemas. Em alguns momentos, precisei ler o enunciado várias vezes para compreender exatamente o que estava sendo pedido e qual lógica deveria ser utilizada para chegar à solução.

No segundo problema, essa dificuldade ficou ainda mais evidente, pois foi necessário entender o significado dos valores apresentados e como eles influenciavam na decisão final da equipe. Percebi que, muitas vezes, o desafio não está apenas em escrever o código, mas em interpretar corretamente a situação antes de programar.

Em relação ao GitHub e ao Visual Studio Code, encontrei algumas dúvidas iniciais por falta de prática, mas consegui aprender rapidamente os procedimentos necessários. Com o uso e a repetição das atividades, fui me sentindo mais confortável com as ferramentas.

 
 
### O que aprendi
### O que aprendi

Com este desafio, aprendi muito mais do que apenas resolver dois problemas de programação. Aprendi conceitos básicos de Python, como entrada de dados, estruturas de repetição, condicionais, contadores e manipulação de textos. No primeiro problema, aprendi sobre o uso do comando `len()` para verificar o tamanho das palavras e sobre a manipulação de strings. No segundo problema, aprendi a utilizar contadores e a trabalhar com lógica baseada em condições.

Também aprendi a utilizar ferramentas importantes para quem está estudando tecnologia, como o Visual Studio Code e o GitHub. Foi a primeira vez que organizei arquivos de programação em um repositório, editei um README.md e utilizei o terminal para executar códigos.

Além disso, percebi a importância da Inteligência Artificial como ferramenta de apoio ao aprendizado. Em vez de apenas buscar respostas prontas, utilizei a IA para compreender conceitos, esclarecer dúvidas e aprofundar meu entendimento sobre os problemas propostos.

O principal aprendizado foi entender que a programação exige raciocínio lógico, interpretação e prática constante. Cada exercício resolvido aumentou minha confiança e mostrou que o aprendizado acontece passo a passo.

 
### Como foi a experiência?
A experiência foi extremamente enriquecedora e marcou meu primeiro contato com diversas ferramentas e plataformas utilizadas na área de tecnologia. Antes de participar da mentoria Codificadas – Além do Código, eu nunca havia utilizado o GitHub, não conhecia o Codeforces e também não tinha experiência prática com programação.

Quando a Unicesumar divulgou a parceria com a TCS, minha primeira reação foi de insegurança, pois eu não me considerava preparada para participar de um desafio de programação. Mesmo assim, decidi me inscrever porque enxerguei a oportunidade de aprender algo novo e ampliar meus conhecimentos.

Ao longo das lives e atividades, fui apresentada a novas ferramentas, conceitos e formas de aprender tecnologia na prática. Além de resolver os problemas propostos, aprendi a utilizar o GitHub para organizar projetos, o Visual Studio Code para desenvolver os códigos e o Codeforces como plataforma de desafios de programação. Também pude compreender melhor como a Inteligência Artificial pode ser utilizada como uma ferramenta de apoio ao aprendizado, auxiliando na interpretação dos problemas e na construção do raciocínio lógico.

Outro ponto muito positivo foi o contato com professores e profissionais da área, que compartilharam experiências e conhecimentos de forma acessível para quem está começando. As lives foram muito importantes para diminuir o receio que eu tinha em relação à programação e me mostraram que o aprendizado acontece gradualmente, por meio da prática e da dedicação.

Finalizo esta experiência com mais confiança e motivação para continuar estudando. O campeonato acontecerá em setembro e pretendo continuar me preparando, estudando e praticando. Hoje entendo que não preciso saber tudo para começar. O mais importante é manter a curiosidade, buscar conhecimento e continuar aprendendo um passo de cada vez.
