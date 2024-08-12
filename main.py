# biblioteca
import os

# dicionario
usuario = {}
 
print('\nDADOS PESSOAIS\n')  
usuario['Nome'] = input('Informe o nome: ')
usuario['CPF'] = input('Informe seu CPF:  ')
usuario['RG'] = input('Informe seu RG: ')
usuario['Sexo'] = input('Informe seu sexo: ')
usuario['Signo'] = input('Informe seu signo: ')
usuario['Nome da mãe'] = input('Informe nome da mãe: ')
usuario['Nome do pai'] = input('Informe nome do pai: ')

os.system('cls')

print('\nOnline\n')
usuario['E-mail'] = input('Informe o e-mail: ')
usuario['Senha'] = input('Informe a senha: ')

os.system('cls')

print('\nENDEREÇO\n')
usuario['CEP'] = input('Informe seu CEP: ')
usuario['Endereço'] = input('Informe seu endereço: ')
usuario['Número'] = input('Informe seu número: ')
usuario['Bairro'] = input('Informe seu bairro: ')
usuario['Cidade'] = input('Informe a cidade: ')
usuario['Estado'] = input('Informe seu estado: ')

os.system('cls')

print('\nTELEFONES\n')
usuario['Telefone'] = input('Informe seu telefone: ')
usuario['Celular'] = input('Informe seu celular: ')

os.system('cls')

print('\nCARACTERÍSTICAS FÍSICAS\n')
usuario['Altura'] = input('Informe sua altura: ')
usuario['Peso'] = input('Informe seu peso: ')
usuario['Tipo sanguineo'] = input('Informe seu tipo sanguineo: ')

os.system('cls')



for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')