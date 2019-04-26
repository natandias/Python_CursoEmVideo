import unidecode

preco = str(input("Digite o preço do produto: "))
pgto = str(input("Deseja em dinheiro, cheque ou cartão: ")).strip().upper()

preco = preco.replace(',', '.')
preco = float(preco)



pgto = unidecode.unidecode (pgto) #retira acento da palavra

if pgto == 'CARTAO':
    parcelas = int(input("Deseja dividir em quantas parcelas: "))
    if parcelas == 1: 
        preco = preco - (preco*0.05)
    if parcelas >= 3:
        preco = preco*1.20 
    print (f"{parcelas} parcelas de {preco/parcelas:.2f}")
    print (f"O valor total da compra é: {preco:.2f}")

elif pgto == 'DINHEIRO' or pgto == 'CHEQUE':
    preco = preco - (preco*0.10)
    print (f"O valor total da compra é: {preco:.2f}")




