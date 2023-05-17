import random



def jogar():
    print("**********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("**********************************")



    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    #para pegar uma palavra aleatotia, vamos pegar de um arquivo de palavras
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()
        #retrirando qualquer possibilidade de ter um espaço acidental na palavra

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                #com o .upper fazemos que tanto o chute quando a letra sempre esteja em maiuscula comparando maiuscula com maiuscula
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!!")
    print("Fim do jogo!!")

if (__name__ == "__main__"):
    jogar()


#Funçôes em strings: definição ""
# .find(), mostra o index da primeira letra correspondenteao solicitado
# .lower() tranforma todas a letras da string em letras minusculas
# .upper() tranforma todas a letras da string em letras maiusculas
# .strip() retira os espaços de uma string, e paragrafos
# .capitalize() torna a priemira letra como maiuscula

#Funções em list: definição []
#nim(lista), retorna o menor valor da lista, se a lista for de números
#max(lista), retorna o maior valor ada lista, se a lista for de números
#len(lista), retorna a quantidade de elementos da lista
#.append(elemento), adiciona elemento na lista
#x in lista, retorna true ou false, verifica se o elemento consta na lista
#print(lista.count(elemento)), retorna o numero de vezes que um determinado elemento se repete
#print(lista.index(elemento)), retorna o index correspondente do elemento
#palavra = list(tupla), transforma tupla em lista

# Funçôes em Tuple: difinição ()
#A tuple é imutavel, ou seja, n pode adicionar ou remover valores
#Podendo usar as funções que se usa na lista, que n alteram a mesma, como len, min, max etc.....
#palavra = tuple(list), transforma lista em tupla
#tuplas podem ser guardadas em listas
#Ex:
#instrutor1 = ("Nico", 39)
#instrutor2 = ("Flávio", 37)
#instrutores = [instrutor1, instrutor2]
#instrutores >>>>>> retorna [('Nico', 39), ('Flávio', 37)]
#instrutores[0] >>>>>> retorna  ('Nico', 39)
#instrutores[0][1]  >>>>>> retorna  39

#Funções em Dictionary: definição {}
#Atribui uma especie de lista com valores de cada index
#Ex:
#instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
# se for pedido o string flavio, instrutores['Flavio'] retorna 37


#Funções em List comprehension: definição list2 = [x for x in list1]
#Mas como é entendido?
#O primeiro termo é uma operação, pode ser nenhuma, como usar simplesmente x, mas pode ser uma operação como x**2, ou ate mesmo atribuir uma string.
#O segundo termo, é um elemento da list1 (terceiro termo)
#EX:
#list1 = [2,3,4,5,6]
#supondo que eu queria elevar ao quadrado os elementos de list1
#list2 = [x**2 for x in list1]
#Isso se le da seguinte forma,faça uma lista onde sera [elevado ao quadrado(x**2) para(for) cada elemento(x) da lista
#
#EX2:
#Fazer uma lista dos numeros pares que constão na seguinte lista:
#inteiros = [1,3,4,5,7,8,9]
#
#pares = [x for x in inteiros if x % 2 == 0]
#alem de colocar os elementos que ja tinam, pode se fazer um if ao mesmo tempo de forma que fique.
#Lendo: faça uma lista com x(ou seja, sem executar operação), para(for) cada elemento(x) de inteiros(lista), se(if) este elemento for par(divisão por 2 tiver resto 0)