# -*- coding: utf-8 -*-
"""Oitava_questão

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G-5lp1urFv5SYIwuhHX1Ef0Edck2wkIl
"""

nomes = []
idades = []
mais_trinta = []
menos_trinta = []
dic = {}
for i in range (5):
  nome_novo = input(f"nome novo do dic: ")
  idade_nova = int(input(f"idade do dic: "))
  
  dic.update({nome_novo:idade_nova})

for nome in dic.keys():
  if(dic[nome] > 30):
    mais_trinta.append(nome)
  else:
    menos_trinta.append(nome)

print(f"acima de trinta: {mais_trinta}")
print(f"abaixo de trinta: {menos_trinta}")