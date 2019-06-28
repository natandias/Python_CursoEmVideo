from datetime import date
dados = dict()

dados['Nome'] = str(input("Nome: "))
ano_nasc = int(input("Qual o ano de nascimento? "))
ano_atual = int(date.today().year)
idade = ano_atual-ano_nasc
dados['Idade'] = idade
print("Tecle 0 se não possui carteira de trabalho")
dados['CTPS'] = int(input("Num da carteira de trabalho: "))
if dados['CTPS'] != 0:
    dados['Ano_de_contratacao'] = int(input("Ano de contratação: "))
    dados['Salario'] = float(input("Salário: "))
    dados['Ano_aposentadoria'] = dados['Ano_de_contratacao'] + 35
    dados['Idade_aposentadoria'] = dados['Idade'] + (dados['Ano_aposentadoria'] - ano_atual)
  
print("\n")
print('=-'*20)
print("||Seus dados: ")
for k, v in dados.items():
    print(f"{k}: {v}")
