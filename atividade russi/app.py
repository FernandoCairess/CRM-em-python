from aluno import Aluno
from disciplina import Disciplina
#criar um aluno
rafael = Aluno("Rafael", "563567", "Engenharia de Software")
rafael_nome = rafael.get_nome()
print(rafael_nome)

#crias disciplinas
front= Disciplina("Front-End","Alexandre Russi")
calculo= Disciplina("Cálculo","Prof Erick")

#matricular os alunos nas disciplinas
rafael.matricular(front)
rafael.matricular(calculo)

#adicionar notas do aluno em cada disciplina
rafael.adicionar_nota(front,2)
rafael.adicionar_nota(front,9)
rafael.adicionar_nota(calculo,10)
rafael.adicionar_nota(calculo,5)


rafael.exbir_boletim()