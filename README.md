# Python-avancando-na-linguagem-Desenvolve-Boticario
 Este projeto faz parte do plano de estudos elaborado pela Alura para o programa de formação Desenvolve (3ª edição), trilha de dados, em parceria com a Boticário.

# Avançando na linguagem Python

Entendendo mais como funciona o Python 3 e as diferentes estruturas de dados.

1. [Preparando o jogo da forca](#1-preparando-o-jogo-da-forca)
2. [Manipulando strings](#2-manipulando-strings)
3. [Conhecendo e trabalhando com listas](#3-conhecendo-e-trabalhando-com-listas)
4. [Conhecendo e trabalhando com tuplas](#4-conhecendo-e-trabalhando-com-tuplas)
5. [Implementando o encerramento do jogo](#5-implementando-o-encerramento-do-jogo)
6. [Escrita e leitura de arquivos](#6-escrita-e-leitura-de-arquivos)
7. [Melhorando o código e a apresentação](#7-melhorando-o-código-e-a-apresentação)

Saiba mais sobre o curso [aqui](https://cursos.alura.com.br/course/python-3-avancando-na-linguagem) ou acompanhe minhas anotações abaixo. ⬇️

## 1. Preparando o jogo da forca

### **Tipo booleano**

Para representar verdadeiro e falso no Python, deve-se utilizar o tipo `bool`. Então se o valor de uma variável é `true`, o tipo dela é bool. Além disso, valores vazios e zeros são considerados como `false`.

```py
existe = True
type(existe)    # resultado no console <class 'bool'>

bool(0)         # false
bool(1)         # true

bool("")        # false
bool("teste")   # true

bool(None)      # false
bool(True)      # true
```

Existe uma função de busca que retorna a posição de uma letra num texto. Porém, ela não retorna letras repetidas. Então numa palavra com 6 letras, em que há letras repetidas, ela irá retornar apenas a posição da primeira.

```py
palavra = "banana"

palavra.find("b")   # retorna 0
palavra.find("n")   # retorna 2
palavra.find("n")   # retorna 2 novamente

palavra.find("z")   # retorna -1 para letra não que não existe na palavra
```

## 2. Manipulando strings

### **Iterando em uma palavra**

> Uma palavra nada mais é do que uma sequência de caracteres. Tanto isso é verdade, que podemos usar o laço for para iterar. Nesse contexto, iterar significa receber a cada iteração uma letra da palavra.

### **Funções importantes da string**

O Python diferencia letras maiúscula e minúscula. Essa questão dificulta a interação do usuário ao digitar algo no `input`, pois só será reconhecido se for digitado da mesma forma que está registrado. Algumas das funções utilizados em strings são:

- `format` formata uma string, adicionando e/ou substituindo valores de variáveis entre chaves.
- `find` retorna a posição (índice) de um caractere numa string, retornando -1 caso seja falso.
- `index` funciona como o find, mas retorna um erro quando não encontra o valor especificado.
- `capitalize` retorna a cópia de uma string, com apenas o primeiro caractere em maiúsculo.
- `lower` retorna a cópia de uma string, pega todos os caracteres e transforma em minúsculo.
- `uper` retorna a cópia de uma string, pega todos os caracteres e transforma em maiúsculo.
- `startswith` testa o prefixo da string, a partir de um ponto ou até certo ponto da string.
- `endswith` testa o sufixo da string, a partir de um ponto ou até certo ponto da string.
- `strip` retorna a cópia de uma string, removendo espaços em branco ou caracteres predefinidos.

> Essas funções devolvem uma nova string que representa, mas não altera a original.

## 3. Conhecendo e trabalhando com listas

### **Estrutura de dados: List**

As listas são sequências mutáveis, normalmente usadas para armazenar caracteres. O construtor cria uma lista cujos itens são os mesmos e na mesma ordem dos itens da sequência. Por exemplo, `list('abc')` retorna **['a', 'b', 'c']** e `list(1, 2, 3)` retorna **[1, 2, 3]**. As listas podem ser construídas das seguintes formas:

- Usando um par de colchetes `[]` vazio
- Com caracteres `[a, b, c]` separados por vírgulas.
- Se um valor está dentro de uma sequência `[x in s]`.

Outras funções úteis de lista são `min()` e `max()`. Eles retornam o menor e maior valor da lista atual. Não retornam a posição e, sim, o valor. Já o `len()` retorna o total de valores de uma lista. O `append()` e o `pop()` adicionam e removem itens ao final de uma lista.

```py
valores = []    # lista vazia

valores = [0, 1, 2, 3, "x"]

6 in valores    # retorna false
3 in valores    # retorna true

valores[0]      # retorna 0
valores[5]      # retorna erro
valores[4]      # retorna "x"

"a" in "banana" # retorna true

valores = [0, 1, 2, 3, 5]

min(valores)    # retorna 0 // funciona em itens do mesmo tipo
max(valores)    # retorna 5
len(valores)    # retorna 5

# adiciona o valor definido ao final da lista [0, 1, 2, 3, 5, 7]
valores.append(7)
valores

# retorna um valor e também o remove da lista [0, 1, 2, 3, 5]
valores.pop()
valores
```
> Para verificar se um determinado elemento existe em uma Lista, podemos utilizar o operador `in`. Ele nos retorna True ou False caso o elemento esteja ou não dentro da lista verificada.

### **Outros recursos com lista**

> Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função `.count()`. O código abaixo nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela. Podemos, também, detectar quantas letras ainda faltam para o nosso usuário preencher.

```py
valores = [0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
```
> Uma outra função que pode ser bastante útil é a função `.index()`, que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista. O código abaixo nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas. Retornando um erro caso você tente buscar pelo índice de um elemento que não existe.

```py
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))
# "ValueError: 'Melancia' is not in list"
```

> É sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter o seu índice. Um código ideal que faz uso da função index() é demonstrado abaixo. Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.

```py
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
```

> Muitas outras operações também produzem listas, como a funçao `sorted()`.

## 4. Conhecendo e trabalhando com tuplas

### **Reforçando as listas**

Foi dito que a função `len()` retorna o total de valores de uma lista. Isso significa que, se numa lista de números temos `lista = [2, 5, 2, 8, 5]` , len irá retornar 5 números. Porém, quando fala-se de strings, ele retorna o número de caracteres tendo assim `palavra = "banana"` , o len irá retornar 6 letras. Enquanto isso, o `min()` e `max()` em relação a string, irão retornar em ordem alfabética.

```py
lista = [2, 5, 2, 8, 5]

len(lista)  # retorna 5 números
min(lista)  # retorna 2 como menor número
max(lista)  # retorna 8 como maior número
lista[3]    # retorna 8 como número na posição 3

palavra = "banana"

len(palavra)  # retorna 6 letras
min(palavra)  # retorna 'a'
max(palavra)  # retorna 'n'
```

### **O que são tuplas?**

Tupla também é uma sequência, mas é uma lista imutável. Então as funções `append()` e `pop()` não funcionam. Como exemplo, pode-se listar os dias da semana que são fixos e imutáveis. Não é possível remover um dia na realidade, assim como não é possível remover na tupla. *Obs. Listas usam colchetes e tuplas usam parênteses.*

```py
dias = ["D", "S", "T", "Q", "Q", "S", "S"]
dias.append("D")    # adiciona um domingo ao final da lista
dias                # verifica inserção do novo elemento
dias.pop()          # retorna o último valor da lista e o remove
dias                # verifica remoção do último elemento

dias = ("D", "S", "T", "Q", "Q", "S", "S")
dias.append("D")
dias.pop()
```

> Uma sequência é nada mais do que um conjunto de valores ordenados. Essa ordem é definida pelo índice. Por isso podemos acessar listas, tuples ou strings através dos colchetes.

```py
# usando uma lista
>>>palavra = "alura"
>>>palavra[3] 
r

# usando uma tupla
>>>letras = ("p", "y", "t", "h", "o", "n")
>>>letras[2] 
t
```

### **Diferenças entre sequências**

- `list` usa colchetes [] para inicialização, `tuple` usa parênteses ().
- list é `mutável`, podendo adicionar ou remover elementos, tuple é `imutável`, não pode ser alterada.
- `str` e `range` também são sequências imutáveis, como a tuple.

Para transformar uma tupla em uma lista, existe a função `list()`. Para transformar de list para tupla deve-se usar `tuple()`. Ambas são funções built-in.

Exemplos mais propensos a serem usados como tuplas em vez de listas, pois não fixos e imutáveis:

- Meses
- Estados
- Estações do ano

### **Para saber mais: Set**

As sequências guardam valores de qualquer tipo de dado e possuem uma determinada ordem, pois possuem um índice. Elas também são chamadas de coleções. Porém, em alguns casos, uma sequência não é suficiente. Tanto listas, quanto tuplas aceitam valores repetidos e no caso de uma lista contendo vários CPF's, o correto é que não tenha valores duplicados, pois existe apenas 1 CPF para cada pessoa.

```py
lista = [11122233344, 22233344455, 33344455566]

lista.append(11122233344) # funciona!
```

Para corrigir isso, existe a coleção `set`. Nela, os elementos são declarados entre chaves `{}`. Para adicionar elementos a um set, utiliza-se a função `add`. Mas aqui não vai ser possível adicionar um elemento duplicado. Isso ocorre porque o `set` não possui um índice, ou seja, não é uma sequência. Ao tentar buscar um elemento pela posição é retornado um erro. Se não tem índice, não se sabe em qual ordem os valores são impressos.

```py
colecao = {11122233344, 22233344455, 33344455566}

colecao.add(44455566677) # funciona, pois esse elemento ainda não existe
colecao.add(11122233344) # não vai funcionar pois este elemento já existe

# retorna erro
colecao[0]

# retorna os elementos de forma desordenada
for cpf in colecao:
     print(cpf)

11122233344
44455566677
33344455566
22233344455
```

> Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.

### **Para saber mais: Dictionary**

E se não sabemos a posição do instrutor na lista? Como podemos descobrir a idade de um instrutor sem saber a posição dele? No `dictionary` os elementos são sempre em pares, do lado esquerdo tem a `chave` e do lado direito tem o `valor` e, estando entre chaves `{}`, pode-se recuperar o valor.

```py
#cria-se a tuple
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

# depois a list
instrutores = [pessoa1, pessoa2, pessoa3]

# imprime
instrutores
[('Nico', 39), ('Flavio', 37), ('Marcos', 30)]

# filtra
instrutores[1][1]
37

# os nomes estão associados às idades, então pode-se descobrir a idade pelo nome
nome : idade
instrutores['Flavio']   # não funciona em listas e tuplas, nem combinando os dois

# iniciando o dictionary / funciona como se fosse um set
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
#              chave : valor

# imprime
instrutores['Flavio']
37
```

## 5. Implementando o encerramento do jogo

### **Operadores**

Assim como em outras linguagens, o Python utiliza diversos tipos de operadores para realizar cálculos, comparar valores e trabalhar as estruturas dos dados.

- Aritméticos ou de Atribuição:
  - `=` "x = 5" significa que x recebe 5
  - `+` adição
  - `-` subtração
  - `*` multiplicação
  - `/` divisão (resultado decimal)
  - `//` divisão (resultado inteiro)
  - `%` (porcentagem)
  - `+=` "x += 3" é o mesmo que "x = x + 3"  
    `-=` "x -= 3" é o mesmo que "x = x - 3"  
    `*=` "x *= 3" é o mesmo que "x = x * 3"  
    `/=` "x /= 3" é o mesmo que "x = x / 3"
  - `**` exponenciação

- Identidade:
  - `is` retorna "True" se ambas as variáveis ​​forem o mesmo objeto
  - `is not` retorna "True" se ambas as variáveis ​​não forem o mesmo objeto

> Os operadores de identidade são usados ​​para comparar os objetos, não se forem iguais, mas se forem realmente o mesmo objeto, com o mesmo local de memória.

- Comparação:
  - `==` igual
  - `!=` diferente (ou não igual)
  - `>` maior que
  - `<` menor que
  - `>=` maior igual
  - `<=` menor igual

- Associação:
  - `in` retorna "True" se uma sequência com o valor especificado estiver presente no objeto
  - `not in` retorna "True" se uma sequência com o valor especificado não estiver presente no objeto

> Os operadores de associação são usados ​​para testar se uma sequência é apresentada em um objeto.

- Lógicos:
  - `and` "e" retorna "True" se ambas as declarações forem verdadeiras
  - `or` "ou" retorna "True" se uma das declarações for verdadeira
  - `not` "não" inverte o resultado, retorna "False" se o resultado for verdadeiro

### **List comprehensions**

Função que otimiza a utilização de listas, sua criação e seu manuseio. É uma forma concisa de criar e manipular lista, reduzindo as linhas de código. Ver [PEP 202](https://peps.python.org/pep-0202/).

> Sintaxe básica: `[expr for item in lista]`. Em outras palavras: aplique a expressão em cada item da lista.

```py
# forma usual
palavra_secreta = "banana".upper()
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")

# list comprehension
palavra_secreta = "banana".upper()
letras_acertadas = ["_" for letra in palavra_secreta]


# exemplo com range
for item in range(10):
  lista.append(item**2)

lista = [item**2 for item in range(10)]


# exemplo com string
for item in lista:
  resultado.append(str(item).upper())

resultado = [str(item).upper() for item in lista]
```

> List comprehensions podem utilizar expressões condicionais para criar listas ou modificar listas existentes. Com a sintaxe: `[expr for item in lista if cond]`. Ou seja, aplique a expressão em cada item da lista caso a condição seja satisfeita.
>
> Sintaxe para "if" + "else": `[resultado_if if expr else resultado_else for item in lista]`. Para cada item da lista, aplique o "resultado_if" se a expressão for verdadeira, caso contrário, aplique "resultado_else".

```py
resultado = [numero for numero in range(20) if numero % 2 == 0]
# resultado = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
# resultado = [0, 30, 60, 90]

resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
# resultado = ['1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1']
```

## 6. Escrita e leitura de arquivos

### **Utilizando a função open**

A função `open()` serve para abrir um arquivo, dentro de uma pasta específica. Essa função recebe dois parâmetros: o nome do arquivo e o modificador de acesso. O segundo parâmetro é opcional, caso não seja passado o arquivo será aberto no modo padrão de leitura.

- `"r"` Ler
- `"w"` Escrever
- `"a"` Adicionar

```py
# abrindo um arquivo no modo escrita e adicionando itens
>>> arquivo = open("palavras.txt", "w")
>>> arquivo
<_io.TextIOWrapper name='palavras.txt' mode='w' encoding='cp1252'>
>>> arquivo.write("banana")
6
>>> arquivo.write("melancia")
8
>>> arquivo.close()

# abrindo o arquivo no modo append e inserindo mais itens na lista, com quebra de linha
>>> arquivo = open("palavras.txt", "a")
>>> arquivo.write("morango\n")
8
>>> arquivo.write("maça\n")
5
>>> arquivo.close()

# abrindo o arquivo no modo leitura
>>> arquivo = open("palavras.txt", "r")

# tentando escrever no modo leitura
>>> arquivo.write()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: TextIOWrapper.write() takes exactly one argument (0 given)

>>> arquivo.write("xxx")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not writable

# lendo o conteúdo do arquivo
>>> arquivo.read()
'bananamelanciamorango\nmaça\n'
>>> arquivo.read()
''
>>> arquivo.close()

# criando um laço de repetição no arquivo e verificando que já existe quebra de linha
>>> arquivo = open("palavras.txt", "r")
>>> for linha in arquivo:
        print(linha)
>>> linha = arquivo.readline()
>>> linha
'banana\n'
>>> for linha in arquivo:
        print(linha, end="\n")

# removendo a quebra de linha manual
>>> linha
'maça\n'
>>> linha.strip()
'maça'
```

> Se desejamos ler linha a linha de nosso arquivo, podemos utilizar a função `readline()`. Ela nos retorna uma linha por vez, e faz com que a nossa leitura seja feita de modo mais controlado. Também existe a função read() que por sua vez lê o arquivo inteiro.

### **Para saber mais: with**

> Já falamos da importância de fechar o arquivo, certo? Veja o código abaixo que justamente usa a função close :

```py
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()
```

> Agora imagine que dê algum problema na hora da leitura quando chamarmos a função read(). Será que mesmo com erro o arquivo será fechado? Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim... Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só:

```py
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```

> Repare que o with usa a função open. Repare também que não fechamos o arquivo. Isso não é mais necessário pois o Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! Muito melhor não?

## 7. Melhorando o código e a apresentação

### **Organizando o código em funções**

Quando um código fica extenso, sua legibilidade fica mais difícil e cansativa. Para resolver isso, pode-se criar funções para bloco de códigos e chamar essas funções no bloco principal. Além de tornar o código mais legível, a função principal fica organizar para mostrar os passos do que esta sendo feito no programa.

Outra observação importante é que ao criar funções, elas podem ser acessadas como um link. Ao segurar `CTRL` e clicar na função, o programa percorre o código e mostra a função escolhida no clique.

> Quando declaramos uma função, é importante colocar os parênteses logo após o seu nome, é dentro dele que os parâmetros da função ficam. Inclusive toda função possui um bloco, em que podemos adicionar o código que quisermos que a função execute quando for chamada. Um bloco é caracterizado por tudo que fica após os dois pontos, indentado por quatro espaços. Tudo que estiver indentado por quatro espaços são instruções da função.

### **Boas práticas de código**

> Entre as boas práticas de código, está a divisão do código de uma função grande em funções pequenas. Pensando nisso, todas as afirmativas abaixo são verdadeiras, exceto uma. Qual?

<ol type="A">
    <li>Dividindo o código de uma função grande em funções pequenas, evitamos o problema das múltiplas responsabilidades em única grande função, afinal uma função só deve ter uma única responsabilidade.</li>
    <li>O código fica mais fácil de testar, pois com diversas pequenas funções, é muito mais fácil testá-las individualmente em busca de erros.</li>
    <li>A legibilidade do código fica prejudicada, visto que temos de ler diversas funções, em vez de apenas uma.</li>
    <li>Melhora a manutenção do código, já que é mais fácil você cuidar de vários pequenos blocos simples do que um grande bloco complexo.</li>
</ol>

A `letra C` não é uma boa prática, pois quebrar o código em pequenas partes aumenta a legibilidade. A leitura da função principal fica mais fluída e pode-se acessar as demais funções de forma simples. Verificando em separado tudo que foi feito passo a passo.

### **Parâmetros opcionais e nomeados**

Uma função pode ou não recebe parâmetros, eles são opcionais. Contudo, eles também podem ser nomeados.

```py
# parâmetro opcional
carrega_palavra_secreta()             # carrega o arquivo "palavras"
carrega_palavra_secreta("frutas.txt") # carrega o arquivo "frutas"

def carrega_palavra_secreta(nome_arquivos="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
```

Pode-se definir a partir de qual linha deve ser gerado o número.

```py
# aqui carrega a lista completa normalmente
def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


# aqui carrega a lista a partir da primeira linha válida
def carrega_palavra_secreta(primeira_linha_valida, nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    ….

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

Para definir a "primeira_linha_valida" basta que ela receba um valor, podendo ser incusive 0 (zero).

```py
def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    ….

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
```

No entando, é preciso sempre definir a "primeira_linha_valida", pois ao tentar "carregar_palavra_secreta" definindo, por exemplo, 5 como ponto de partida, ele fará isso com o arquivo, não com a linha.

```py
# incorreto
carrega_palavra_secreta(5)

# correto
carrega_palavra_secreta(primeira_linha_valida=5)

# pode-se definir ambos os parâmetros
carrega_palavra_secreta("frutas.txt", 5)

# forma longa do código acima
carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida= 5)

# a ordem dos parâmetros não altera o resultado obtido
carrega_palavra_secreta(primeira_linha_valida=5, nome_arquivo="frutas.txt")
```

⬆️ [Voltar ao topo](#avançando-na-linguagem-python) ⬆️