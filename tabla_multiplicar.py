"""******************************************************'''
 *                    ESTACIÓN DEL MES                    *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

print('\n\t\t\t\tTabla de multiplicar\n\t\t\t\t ================== \n\n')

print('\t   ', end='')
for numero in range (1,10+1):
    print('%5d'%numero, end='')

print('\n_______' + '_____'*10 + '___')

for multiplicador in range (2,10+1,2):
    print('%5d'%multiplicador,'|', end='')
    for multiplicando in range (1,10+1):
        print('%5d'%(multiplicador*multiplicando), end='')
    print('\n')