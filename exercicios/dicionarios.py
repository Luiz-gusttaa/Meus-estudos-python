alunos = [
   {"nome": "luiz", "idade": 26},
   {"nome": "ana", "idade": 25},
   {"nome": "gustavo", "idade": 30} 
]

maiores = []
for aluno in alunos:
    if aluno["idade"] >= 18:
        maiores.append(aluno['nome'])


print(maiores)
