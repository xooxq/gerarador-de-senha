from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from os import system
from time import sleep
from sys import exit
from random import choice

def limpar(a):
    system("cls")
    print(a)
    sleep(1)
    system('cls')

while True:
    system("cls")
    senha = ascii_lowercase+ascii_uppercase+digits+punctuation
    l=[]
    while True:
        try:
            x=int(input("Quantos digitos você deseja (0 para cancelar)?: "))
            if x==0:
                exit()
            break
        except ValueError:
            limpar("Digite apenas números!")
    for c in range(x):
        l.append(choice(senha))
    system('cls')
    print(f"Senha: {''.join(l)}")
    sleep(2)
    z = input("\n\nDeseja abaixar mais coisas (s/n) ?: ").strip().upper()
    while z not in "SN":
        limpar("Digite apenas 's' ou 'n'.")
        z = input("Deseja abaixar mais coisas (s/n) ?: ").strip().upper()
    if z == 'N':
        system('cls')
        print('Fim do programa. Volte logo\n')
        break
    