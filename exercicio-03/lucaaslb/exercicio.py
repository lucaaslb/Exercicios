# -*- coding: UTF-8 -*-

daily = open('diario.txt', 'a')

text = input("Digite seu texto para escrever no arquivo ou 'exit' para finalizar\n")
while text != 'exit':
        daily.write(text + ' ')
        text = input()
daily.close()
