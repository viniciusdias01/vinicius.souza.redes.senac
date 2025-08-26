alunos = [
    {
      "nome": "vinicius",
      "idade": 19,
      "altura": 1.70,
      "ativo": True,
      "avaliacoes": [ 9.0, 8.0, 9.2] 
    },
    {
        "nome": "keven",
        "idade": 25,
        "altura": 1.70,
        "ativo": False,
        "avaliacoes": [ 8.2, 9.0, 8.9]
    }
]

def calcular_media(avaliacoes):
    return sum(avaliacoes) / len(avaliacoes)


def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"nome: {aluno['nome']}")
        print(f"idade: {aluno['idade']}")
        print(f"altura: {aluno['altura']}")
        print(f"ativo: {aluno['ativo']}")
        print(f"média avaliações: {calcular_media(aluno['avaliacoes']):.2f}")
        print("-"*20)
        
def listar_ativos(alunos):
    ativos = [aluno for aluno in alunos if aluno['ativo']]
    return ativos

exibir_alunos(alunos)