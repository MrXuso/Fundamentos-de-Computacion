"""******************************************************'''
 *                  Tabla de multiplicar                  *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

print('\n\t\t\t\t  Tabla de multiplicar\n\t\t\t\t   ================== \n\n')

'''Mostramos los numeros por los que multiplicamos'''
print(' '*7, end='')
for numero in range (1,10+1):
    print('%5d' % numero, end='')

'''Mostramosla barra divisora'''
print('\n_______' + '_____'*10 + '___')

'''Mostramos la tabla de multiplicar'''
for multiplicador in range (2,10+1,2):
    print('%5d' % multiplicador,'|', end='')                #añadimos el número del que hacemos la tabla '    1|' por ejemplo
    for multiplicando in range (1,10+1):
        print('%5d' % (multiplicador*multiplicando), end='')
    print('\n')
