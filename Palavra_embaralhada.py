import random
from time import sleep
lista_palavras = []
arquivo = open("palavras.txt", 'r')
for palavra in arquivo:
    #Pegando lista de palavras doarquivo.txt e adicionando a lista de palavras 
    lista_palavras.append(palavra.replace('\n', '').lower())
arquivo.close()


linha = '=-' * 50
linha_ = '=' *100
titulo = 'VAMOS COMEÇAR!!!!'
#Vai retornar um numero aleatorio de 0 ate o tamanho da lista 
escolhe_palavra = random.randint(0, len(lista_palavras))
#Vai embaralhar a palavra escolhida 
embaralhar_palavra = random.sample(lista_palavras[escolhe_palavra], len(lista_palavras[escolhe_palavra]))

palavra = ''
for c in embaralhar_palavra:#Vai adicionar a palavra já embaralhada em uma variavel
    palavra += c.upper()

print()
tentativas = 6
print()
print(linha_)
print(titulo.center(100))
print(linha_)
while tentativas > 0:
    print('TENTE ADVINHAR QUAL A PALAVRA, VAMOS LÁ. ')
    print(f'TOTAL DE VIDAS: {tentativas}')
    print(f'PALAVRA: {palavra}')
    print()
    tentativa_palavra = str(input('Qual palavra você acha que é: ')).lower()
    if tentativa_palavra == lista_palavras[escolhe_palavra]:
        print()
        print('ACERTOOOU!')
        sleep(2)
        break
    else:
        tentativas -= 1
        print()
        print(f'EROOOU!!! -1 vida')
        print(linha)
        sleep(2)
print()
if tentativas == 0:
    print('Infelizmente suas vidas acabaram e você não acertou a palavra. :(')
    print(f'A PALAVRA ERA {lista_palavras[escolhe_palavra]}')
else:
    print('Você acertou a palavra YUUUP!!!! Parabens:)')
print()
