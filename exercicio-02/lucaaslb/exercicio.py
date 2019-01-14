'''
#######################################################
# @author Lucas Lacerda                               #
# @github Lucaaslb                                    #
# @references                                         #
#     https://www.python-course.eu/lambda.php         #
#######################################################
'''

vtr =  [int(num) for num in input('Digite alguns números separados por espaço: \n').split()]

pares = filter(lambda x: x%2 == 0,vtr)
impares = filter(lambda x: x%2 == 1,vtr)

print('PARES:')
for i in pares:
	print(i)

print ('\n')

print('ÍMPARES:')
for i in impares:
	print(i)