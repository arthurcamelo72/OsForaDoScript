grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao = [[linha, coluna]]
    if orientacao == 'vertical':
        for i in range(tamanho-1):
            linha += 1
            posicao.append([linha, coluna])
    elif orientacao == 'horizontal':
        for j in range(tamanho-1):
            coluna += 1
            posicao.append([linha, coluna])
    return posicao

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)
    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    contador = 0
    for nome in frota:
        for navio in frota[nome]:
            afundou = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                contador += 1
    return contador

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                if posicao in novas:
                    return False
    return True

frota = {}

# cada item é [nome, tamanho, quantidade], na ordem do maior para o menor
navios = [
    ['porta-aviões', 4, 1],
    ['navio-tanque', 3, 2],
    ['contratorpedeiro', 2, 3],
    ['submarino', 1, 4],
]