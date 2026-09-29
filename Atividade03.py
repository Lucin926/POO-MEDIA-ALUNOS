class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media

    def mostrar_dados(self):
        media = self.calcular_media()

        print(f"Aluno: {self.nome}")
        print(f"Nota1: {self.nota1}")
        print(f"Nota2: {self.nota2}")
        print(f"Nota3: {self.nota3}")
        print(f"Média: {media}")


alunos = []

quantidade_alunos = int (input("Quantos alunos deseja lançar nota: "))

for i in range(0, quantidade_alunos):
    nome = str (input("Informe o nome: "))
    nota1 = float (input("Informe a 1º nota: "))
    nota2 = float (input("Informe a 2º nota: "))
    nota3 = float (input("Informe a 3º nota: "))

    aluno = Aluno(nome, nota1, nota2, nota3)
    alunos.append(aluno)

for aluno in alunos:
    aluno.mostrar_dados()
    
