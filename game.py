from random import randint as ri
#jogador vai escolher sua opcao
player = input('tijolo (t), papel de embrulhar prego (p) ou facão (f)? ')

print(' ')
# print(player, "versus", end=' ')

#o computador vai gerar um numero aleatorio entre um e três
chosen = ri(1,3)

"""
print(chosen)

"""

if chosen == 1:
    computer = 't'
elif chosen ==2:
    computer = 'p'
else:
    computer = 'f'

# print(computer)


if player == computer:
    print(player, "versus", computer)
    print("EMPATE!")
elif player == 't' and computer =='f':
    print(player, "versus", computer)
    print("Se lascou! Levou facada de um robô")
elif player == 't' and computer == 'p':
    print(player, "versus", computer)
    print("Tu é arretada mermo! Ganhasse, visse?")
elif player == 'p' and computer == 't':
    print(player, "versus", computer)
    print("Se lascou! Levou tijolada de um robô")
elif player == 'p' and computer == 'f':
    print(player, "versus", computer)
    print("Tu é arretada mermo! Ganhasse, visse?")
elif player == 'f' and computer == 't':
    print(player, "versus", computer)
    print("Tu é arretada mermo! Ganhasse, visse?")
elif player == 'f' and computer == 'p':
    print(player, "versus", computer)
    print("Se lascou! Fosse embrulhado pelo robô")
else:
    print(player+"??? é o quê, mia fia??!?")