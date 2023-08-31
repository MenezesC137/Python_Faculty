class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.nota_p1 = 0
        self.nota_p2 = 0
        self.nota_trabalho = 0

    def adicionar_notas(self, nota_p1, nota_p2, nota_trabalho):
        self.nota_p1 = nota_p1
        self.nota_p2 = nota_p2
        self.nota_trabalho = nota_trabalho

    def calcular_media(self):
        return (self.nota_p1 + self.nota_p2 + self.nota_trabalho) / 3

def main():
    num_disciplinas = int(input("Quantas disciplinas você possui neste semestre? "))
    media_aprovacao = float(input("Qual é a média mínima para aprovação? "))
    
    disciplinas = []
    
    for _ in range(num_disciplinas):
        nome_disciplina = input("Digite o nome da disciplina: ")
        disciplina = Disciplina(nome_disciplina)
        
        nota_p1 = float(input(f"Nota da P1 em {nome_disciplina}: "))
        nota_p2 = float(input(f"Nota da P2 em {nome_disciplina}: "))
        nota_trabalho = float(input(f"Nota do Trabalho em {nome_disciplina}: "))
        
        disciplina.adicionar_notas(nota_p1, nota_p2, nota_trabalho)
        disciplinas.append(disciplina)
    
    nome_aluno = input("Digite o nome do aluno: ")
    
    print("\nBoletim de Notas")
    print(f"Aluno: {nome_aluno}\n")
    
    for disciplina in disciplinas:
        media_disciplina = disciplina.calcular_media()
        status = "Aprovado" if media_disciplina >= media_aprovacao else "Reprovado"
        
        print(f"Disciplina: {disciplina.nome}")
        print(f"Média: {media_disciplina:.2f}")
        print(f"Status: {status}\n")

if __name__ == "__main__":
    main()


    