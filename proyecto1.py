print('hola mundo soy aldair aguirre')
print('hola mundo 1')

#soy un comentario
print('hola mundo 2')

'''
texto que no se va interpretar
'''

# variables
texto = 'proyecto1 de python jueves 7'
nombre = 'Aldair Aguirre'
altura = '175cm'
year = '2022'

print(f'{texto} - {nombre} - {altura} - {str(year)}')
#print(texto +' - ' + nombre +' - '+altura + ' - ' + str+(year)) otra forma de concanetar

# condiciones
altura = int( input('¿cual es tu altura?: '))

if altura >= 180:
    print('eres una persona alta')
else:
    print('eres bajito')
    

# Listas
personas = ['juan', 'pedro', 'lucas']
print(personas[0])

for personas in personas:
    print('-'+ personas)

