faturamento = 1200
custo = 300
lucro = faturamento - custo
margem_lucro = lucro / faturamento
email = "micaelbarbosa390@gmail.com"

print(f"faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}" )

# maiuscula e minuscula
email = email.upper()
print(email)

email = email.lower()
print(email)

# '@' in email
print(email.find("@"))  

#tamanho do texto

print(len(email)) 

# pegar um caractere especifico
print(email[2])

print(email[-2])

#pegar um  pedaco do texto

print(email[6:])

# trocar pedaco do texto

novo_email = email.replace("barbosa", "silva")
print(novo_email)


#trabalhar com nome

 
nome = "micael alves"

print(nome.capitalize())
print(nome.title())     

print(email[16:22])
print(nome[:7], nome[7:13])

#pegar o servidor
posicao_arroba = email.find("@") + 1 
servidor = email[posicao_arroba:]
print(servidor)  

# pegar o nome do usuario
usuario = nome.find(" ")
primeiro_nome = nome[:usuario] # inicio sempre inclui
segundo_nome = nome[usuario+1:]  # fim sempre exclui
print(primeiro_nome)
print(segundo_nome) 
 
#casos especiais - formatacao numerica em texto
margem_lucro = round(margem_lucro, 2)

print(f"faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro:.2%}" )
# f para formatacao de texto 
# : <- para formatacao 
# .2f <- duas casas decimais float
# .2% <- porcentagem com duas casas decimais 