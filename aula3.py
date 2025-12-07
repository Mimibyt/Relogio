email = input("escreva seu email: ")
nome = input("escreva seunome: ") \

print(nome, email)

faturamento = float(input("escreva o faturamento: "))

imposto = faturamento * 0.1
print(imposto)

print(f"{nome}, verifique seu email {email} que enviamos um link da verificacao")

# aula 2 - f para formatacao de texto

#listas

vendas = [1500, 2500, 3000, 5000 ]

#soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

#pegar posicao

print(vendas[3])  #5000
print(vendas[-1]) #5000   #indice -1 puxa o ultimo elemento


lista_produtos = ["camiseta","camiseta","camiseta", "calca", "tenis", "tenis", "tenis", "tenis", "blusao","blusao","blusao", "meia"]

# produto_procurado = input("qual produto voce esta procurando?  ")
#produto_procurado = produto_procurado.lower()


#adicionar itens na lista
lista_produtos.append("boné")
print(lista_produtos)

#remover itens da lista
lista_produtos.remove("meia")
print(lista_produtos)

lista_produtos.pop(2)  #remove pelo indice, se vazio remove o ultimo
print(lista_produtos)

#editar itens da lista
precos = [1000, 200, 350, 200]
precos[0] =  precos[0] * 1.5  #aumenta 20% do preco do primeiro item
print(precos)
#contar itens na lista
print(lista_produtos.count("camiseta"))

#ordenar a lista

lista_produtos.sort(reverse=True)  #ordem alfabetica reversa
print(lista_produtos)    

precos.sort(reverse=True)  #ordem crescente
print(precos)