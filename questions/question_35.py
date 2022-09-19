#!/usr/bin/python
# -*- coding: utf-8 -*-

# 35. Escreva um programa que leia um número inteiro de 1 a 7 e informe o dia da
# semana correspondente, sendo domingo o dia de número 1. Se o número não
# corresponder a um dia da semana, mostre uma mensagem de erro.

ativaAviso = 0

diaNumero = input("Insira o valor númerico referente ao dia da semana: ")

if (int(diaNumero) == 1):
    diaSemana = "domingo"
elif (int(diaNumero) == 2):
    diaSemana = "segunda-feira"
elif (int(diaNumero) == 3):
    diaSemana = "terça-feira"
elif (int(diaNumero) == 4):
    diaSemana = "quarta-feira"
elif (int(diaNumero) == 5):
    diaSemana = "quinta-feira"
elif (int(diaNumero) == 6):
    diaSemana = "sexta-feira"
elif (int(diaNumero) == 7):
    diaSemana = "sábado"
else:
    aviso = "Opção inválida!"
    ativaAviso = 1

if (int(ativaAviso) == 1):
    print("\n" + str(aviso))
else:
    print("\nO valor númerico corresponde a(o) " + diaSemana)
    
 n1 = (input('1 '))
n2 = int(input('2: '))
n3 = int(input('2:'))
soma = 1 + 2 + 2

int main() {
int n, aux, primo = 1;
printf("Digite um numero inteiro: ");
scanf("%d", &n);
for (aux = 2; primo && (aux <= n/2); aux++)
if ((n % aux) == 0)
primo = 0;
if (primo)
printf("Numero primo\n");
else
printf("Numero composto\n");
return 0;
    

  
