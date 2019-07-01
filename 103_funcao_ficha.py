def ficha(nm='erro', gs=0):
    if gs.isnumeric() is True:
        int(gs)
    else:
        gs = '<nenhum dado inserido>'
    if nm == '':
        nm = '<nenhum dado inserido>'
    print(f'O jogador {nm} fez {gs} gols')


ficha(str(input('Nome do jogador: ')).strip(),
      str(input('Numero de gols marcados por ele: ')).strip())    
