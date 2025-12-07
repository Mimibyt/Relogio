venda = 5000
meta = 4000


 # > maior que
 # < menor que
 # >= maior ou igual 
 # <= menor ou igual
 # == igual
 # != diferente

if venda >= meta:
    print("funcionario bateu a meta de vendas!")
    print("bonificacao de 500 reais")
    bonus = 0.2 * venda
    print(f"bonus de vendas: R${bonus:.2f}")   
else:
     print("funcionario nao bateu a meta de vendas.")
     print("sem bonificacao")

print("fim do programa ")

# segundo exemplo
venda1 = 5000
vendas_empresa = 20000
meta_empresa = 15000
meta1 = 10000
meta2 = 7000
meta3 = 3000 

if venda1 >= 7000 and vendas_empresa >= meta_empresa:
     bonus = 0.1 * venda1
elif venda1 >= 3000 and vendas_empresa >= meta_empresa:
        bonus = 0.5 * venda1
else:
        bonus = 0        
print("bonus:", bonus)


lista_produtos = ["camiseta","calca","tenis","blusao"]
produto_procurado = input("qual produto voce esta procurando?  ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print(f"produto {produto_procurado} disponivel para venda")
else: 
    print(f"produto {produto_procurado} nao disponivel em estoque")

    #if tudo que acontece se a condicao for verdadeira
    #else tudo que acontece se a condicao for falsa
    #in verifica se um elemento esta presente na lista
    #and condicao 1 e condicao 2 precisam ser verdadeiras