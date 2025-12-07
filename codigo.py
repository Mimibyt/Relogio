faturamento = 1200 # tipo: int - numero inteiro
custo = 700.32  # tipo: float -> numerom casa decimal
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto


margem_lucro = lucro / faturamento

print("o faturamento foi de ", faturamento)
print("o custo foi de ", custo) 
print("o lucro foi de ", lucro)  
print("A margem de lucro foi de",round(margem_lucro, 2))

mensagem = "O faturamento da loja foi de" #tipo string -> texto
email = "emailqualquer@gmail.com"

teve_lucro =True #variavel tipo 

# mod -> % resto divisao

print(10 % 3)
tempo_contrato = 170 
tempo_anos = 170 / 12
print("tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12 
print("tempo em meses", tempo_meses) 