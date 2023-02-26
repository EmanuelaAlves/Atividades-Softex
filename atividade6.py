#variavéis
turmaA = []
turmaB = []
turmaC = []
turmaD = []
maiorNota = 0
alunoMaiorNota = ""

#nome e nota dos alunos
for i in range(1,100):
        nome = input("Digite o nome do aluno" + str(i) + ": ")
        nota = float(input("Digite a nota do aluno" + str(i) + ": "))
        
        if nota >= 7:
            if i <= 25:
                turmaA.append((nome, nota)) 
            if i <= 25:
                turmaB.append((nome, nota))           
            if i <= 25:
                turmaC.append((nome, nota))      
            if i <= 25:
                turmaD.append((nome, nota))  
                
        if nota > maiorNota:
            maiorNota = nota
            alunosMaiorNota = nome  
            
#número de aprovados e maior nota em cada turma
print("Turma A:") 
print("Número de aprovados:", len(turmaA))  
if turmaA:
    print("Maior nota:", max(turmaA, Key=lambda x: x[1])[1])    
print() 

print("Turma B:") 
print("Número de aprovados:", len(turmaB))  
if turmaB:
    print("Maior nota:", max(turmaB, Key=lambda x: x[1])[1])    
print() 

print("Turma C:") 
print("Número de aprovados:", len(turmaC))  
if turmaC:
    print("Maior nota:", max(turmaC, Key=lambda x: x[1])[1])    
print() 

print("Turma D:") 
print("Número de aprovados:", len(turmaD))  
if turmaD:
    print("Maior nota:", max(turmaD, Key=lambda x: x[1])[1])    
print() 

#Aluno com maior nota de todas
print("Aluno com maior nota de todas:", alunoMaiorNota, "nom nota", maiorNota)





