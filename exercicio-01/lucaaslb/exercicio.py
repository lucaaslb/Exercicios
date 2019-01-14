#!/usr/bin/python3

'''
#############################
# @author Lucas Lacerda     #
# @github Lucaaslb          #
#############################
'''

from random import randint

vtrInt = [] 

print ('5 numeros gerados aleatoriamente ...')
for num in range(5):
    vtrInt.append(randint(0, 250))

print ('Lendo vetor: ')   
for num in vtrInt:
    print(num)    