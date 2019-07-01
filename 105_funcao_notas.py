def notas(* nt, situacao=False):
    """
    Essa função analisa notas e retorna estatísticas sobre a situação do aluno
    :param nt: recebe como argumentos notas dos alunos
    :param situacao: opcional, indica se deve ou não retornar a situação do aluno
    :return: dicionário contendo análise feita
    """
    dados = {}
    dados['Qtd_Notas'] = len(nt)
    dados['Maior_Nota'] = max(nt)
    dados['Menor_Nota'] = min(nt)
    dados['Media'] = sum(nt)/len(nt)
    if situacao is True:
        if dados['Media'] >= 9:
            dados['Situação_Aluno'] = 'Excelente'
        elif dados['Media'] >= 7:
            dados['Situação_Aluno'] = 'Acima da média'
        elif dados['Media'] >= 5:
            dados['Situação_Aluno'] = 'Razoável'
        elif dados['Media'] >= 3:
            dados['Situação_Aluno'] = 'Ruim'
        elif dados['Media'] < 3:
            dados['Situação_Aluno'] = 'Péssimo'
    return dados     


a = notas(1.5, 1.5, 1.5, 6.5, situacao=True)
print(a)
