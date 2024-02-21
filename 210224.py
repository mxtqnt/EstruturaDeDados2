# Utilizando a noção de Hash, preencha os comentários do código disponibilizado em scanuto.com/hash1.c 
# para 5 alunos cujas matrículas se iniciam em 5538 e terminam em 5542. Não crie nenhum vetor ou estrutura 
# adicional para armazenar matrículas e notas.
# 5538 5539 5540 5541 5542

hash = [0, 0, 0, 0, 0]

def posicaohash(matricula):
  posicao = matricula - 5538
  print(posicao)
  return int(posicao)

for nota in hash:
  matricula = int(input("Matricula: "))
  nota = float(input("Nota: "))
  # print("A nota do aluno de matricula " + matricula + " é " + nota)

  # insira aqui o código para preencher o hash
  hash[posicaohash(matricula)] = nota

# insira aqui o código para imprimir todas  matriculas/notas
for item in hash:
  print("A nota do aluno de matricula " + str(hash.index(item) + 5538) + " é " + str(item))

