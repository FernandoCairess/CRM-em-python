from disciplina import Disciplina

class Aluno:
    def __init__(self, nome_param, matricula, curso):
        self.nome=nome_param
        self.matricula =matricula
        self.curso=curso
        self.disciplinas = []   #lista de objetos do itpo disciplina
        self.notas_por_disciplina={}    #dict>> {nome_da_disciplina : [XX,YY]}


    def get_nome(self):
        return self.nome


    def matricular(self,disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome,[])

    def adicionar_nota(self,disciplina:Disciplina, nota:float):
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_por_disciplina(self,disciplina:Disciplina) -> float:
        notas= self.notas_por_disciplina.get(disciplina.nome,[])
        return  sum(notas)/len(notas)


    def exbir_boletim(self):
        print(self.disciplinas)
        print(self.notas_por_disciplina)

        for disciplna in self.disciplinas:
            media_disciplina = self.media_por_disciplina(disciplna)
            print(f"Média do aluno em {disciplna.nome}: {media_disciplina}")

