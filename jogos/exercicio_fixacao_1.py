# Exercicio de fixação Renan Pereira Gonçalves
import random

n = random.randrange(1, 1001)
print(n)
i = 1
n_leds = 0

while i<=n:
    v = str(random.randrange(1, 10**100))
    print(v)
    for x in range(len(v)):
        if int(v[x]) == 1: # número 1
            n_leds = n_leds + 2
        elif int(v[x]) == 4:# número 4
            n_leds = n_leds + 4
        elif int(v[x]) == 7:# número 7
            n_leds = n_leds + 3
        elif int(v[x]) == 2 or int(v[x]) == 3 or int(v[x]) == 5:# números 2, 3 e 5
            n_leds = n_leds + 5
        elif int(v[x]) == 6 or int(v[x]) == 9 or int(v[x]) == 0:# números 6, 9 e 0
            n_leds = n_leds + 6
        else: # número 8
            n_leds = n_leds + 7
    i += 1

print("O numero de leds é: {}".format(n_leds))