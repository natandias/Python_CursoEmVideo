import unidecode

preco = str(input("Digite o preço do produto: "))
preco = preco.replace(',', '.')
preco = float(preco)

pgto = str(input("Deseja em dinheiro, cheque ou cartão: ")).strip().upper()
pgto = unidecode.unidecode (pgto) #retira acento da palavra

#estrutura de controle de entrada do meio de pagamento
while (pgto != 'CARTAO' and pgto != 'DINHEIRO' and pgto != 'CHEQUE'):
    print ("Opção inválida!!! Verifique se digitou corretamente o meio de pagamento")
    pgto = str(input("Deseja em dinheiro, cheque ou cartão: ")).strip().upper()
    pgto = unidecode.unidecode (pgto)

if pgto == 'CARTAO':
    parcelas = int(input("Deseja dividir em quantas parcelas: "))
   #estrutura de controle de entrada da qtd de parcelas
    while  parcelas <=0 or parcelas > 12:
        print ("Quantidade inválida!!! Mínimo: 1 parcela, Máximo: 12 parcelas")
        parcelas = int(input("Deseja dividir em quantas parcelas: "))

    if parcelas == 1: 
        preco = preco - (preco*0.05)
        print (f"{parcelas} parcela de {preco/parcelas:.2f}")
        
    elif parcelas >= 3:
        preco = preco*1.20 
        
    if parcelas != 1:
        print (f"{parcelas} parcelas de {preco/parcelas:.2f}")

    print (f"O valor total da compra é: {preco:.2f}")

elif pgto == 'DINHEIRO' or pgto == 'CHEQUE':
    preco = preco - (preco*0.10)
    print (f"O valor total da compra é: {preco:.2f}")




