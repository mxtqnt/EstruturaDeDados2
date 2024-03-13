from nomes import NOMES

def valor_string(string):
    valor = 7
    for char in string:
        valor = 31 * valor + ord(char)
    return valor

mod = 9
tabelahash = [[]] * mod

for index, nome in enumerate(NOMES, start=1):
    valor = valor_string(nome)
    resultado = valor % mod
    tabelahash[resultado].append((index, nome))

def printtabela(tabela):
    for index, item in enumerate(tabela, start=0):
        with open('060324//resultado.txt', 'a', encoding='utf-8') as file:
            file.write('Posição ' + str(index) + ':')
            file.write(str(item))

printtabela(tabelahash)