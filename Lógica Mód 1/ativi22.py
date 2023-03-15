class Aluno:
    quantidade_alunos = 0

    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
        Aluno.incrementar_quantidade()
    @staticmethod
    def incrementar_quantidade():
        Aluno.quantidade_alunos += 1
        
    def imprimir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")

aluno1 = Aluno("João", "0000001", "Pedagogia")
aluno2 = Aluno("Maria", "0000002", "Letras")
aluno3 = Aluno("Bruno", "0000003", "Medicina")


aluno1.imprimir_info()
aluno2.imprimir_info()
aluno3.imprimir_info()

print(f"Quantidade de alunos cadastrados: {Aluno.quantidade_alunos}")