# Palestra Pyladies - Hands On 

## O que faremos: 

![](tijolo, papel e facao.gif)

### Passo a passo do joguinho:

**1** - Primeiro, importe a biblioteca randint e em seguida deixe o jogador escolher entre Tijolo, Papel de embrulhar prego e Facão, digitando as iniciais de cada um:
``` python
  $ from random import randint

  $ jogador = input(player = input('tijolo (t), papel de embrulhar prego (p) ou facão (f)? '))
```

**2** - Agora imprima a escolha do jogador:
``` python
  $ print(jogador, 'versus')
```

**3** - Rodada do computador. Agora vamos usar a função que importamos __randint__ para gerar um número aleatório para decidir entre as três opções Tijolo, Papel de embrulhar prego e Facão:
```python
  $ escolhido = randint(1,3)
  $ print(escolhido)
```
**4** - 
