from random import randint
from time import sleep
pc = randint(0,10)
contador = 0
print("Vou pensar em um número, tente adivinhar!! Você tem apenas 3 chances.")
sleep(1)
print('Vou te dar alguns segundos!!')
sleep(3)
while contador < 3:
    jogador = int(input("Em que número pensei? . . .  "))
    if jogador == pc:
        print("Parabéns, você acertou!")
        exit()
    else:
        print("Você errou, tente novamente!")
        contador += 1

print(f'Você errou e excedeu o número de tentativas. O número escolhido foi {pc}')