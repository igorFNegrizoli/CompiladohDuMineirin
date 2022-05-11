import pandas as pd

producoes = {
    0:['X', 2],
    1:['A', 4],
    2:['A', 2],
    3:['B', 2],
    4:['B', 2],
    5:['B', 2],
    6:['B', 2],
    7:['B', 2],
    8:['B', 2],
    9:['B', 2],
    10:['C', 4],
    11:['D', 2],
    12:['D', 2],
    13:['E', 6],
    14:['E', 6],
    15:['F', 2],
    16:['F', 2],
    17:['F', 2],
    18:['G', 2],
    19:['G', 2],
    20:['H', 16],
    21:['H', 14],
    22:['I', 6],
    23:['I', 6],
    24:['I', 10],
    25:['I', 4],
    26:['J', 6],
    27:['J', 2],
    28:['J', 2],
    29:['L', 2],
    30:['L', 2],
    31:['M', 16],
    32:['M', 8],
    33:['N', 2],
    34:['N', 6],
    35:['N', 6],
    36:['O', 10],
    37:['O', 6],
    38:['O', 6],
    39:['O', 8],
    40:['O', 4],
    41:['O', 4],
    42:['P', 6],
    43:['P', 2],
    44:['P', 2],
    45:['R', 8],
    46:['S', 8],
    47:['S', 8],
    48:['T', 2],
    49:['T', 6],
    50:['T', 2],
    51:['U', 2],
    52:['U', 2],
    53:['U', 2]
}

dicionario_tokens = {
    "=": "eh",
    "opLogBin": "Operador Lógico Binário",
    "opLogUn": "neim",
    "opAritBin": "Operador Aritmético Binário",
    "opAritUn": "Operador Aritmético Unário",
    "opRel": "Operador Relacional",
    "elif": "e_tem_cabimento",
    "else": "num_tem_cabimento",
    "string": "String",
    "int": "Inteiro explícito",
    "real": "Real explícito",
    "bool": "Booleano explícito",
    "(": "(",
    ")": ")",
    "{": "{",
    ",": ",",
    "trem": "Variável",
    "type": "Tipo",
    "oia": "oia",
    "print": "espia_soh",
    "input": "xove",
    "while": "vai_toda_vida",
    "break": "pica_mula",
    "if": "tem_cabimento",
    "}": "}"
}

def read_token_file(token_list):
    f = open("tokens.txt")

    for line in f:
        token_end = 2
        for char in line[token_end:-2]:
            if char=="'":
                break
            token_end+=1
        token = line[2:token_end]

        value_end = token_end+4
        for idx in range(len(line)-2, value_end, -1):
            if line[idx]=="'":
                value_end = idx
                break
        value = line[token_end+4:value_end]

        line_number_start = value_end
        for char in line[line_number_start:-2]:
            if char==",":
                break
            line_number_start+=1
        line_number = line[line_number_start+2:-2]

        token_list.append([token, value, line_number])

    token_list.append(['$','$', token_list[-1][2]])

def empilha(pilha, num_celula, a):
    pilha.append(a)
    pilha.append(num_celula)

def reduz(pilha, num_celula, tabela_df):
    pilha = pilha[:-producoes[num_celula][1]]   #desempilha 2*|B|

    s = pilha[-1]              #s é topo da pilha

    pilha.append(producoes[num_celula][0])  #empilha A
    
    desvio = int(tabela_df.iloc[s][producoes[num_celula][0]])

    pilha.append(desvio)        #empilha desvio

    return pilha

def sintatico():
    token_list = []
    read_token_file(token_list)

    tabela_df = pd.read_csv("Tabelas.csv")
    pilha = [0]
    s = 0           #estado atual
    i = 0

    while(i < len(token_list)):
        s = pilha[-1]
        token_value_pair = token_list[i]

        a = token_value_pair[0]         #token lido do par

        celula = tabela_df.iloc[int(s)][a]

        cod_acao = celula[0]
        
        if cod_acao == 'E':
            num_celula = int(celula[1:])
            empilha(pilha, num_celula, a)
            i += 1
        elif cod_acao == 'R':
            num_celula = int(celula[1:])
            pilha = reduz(pilha, num_celula, tabela_df)
        elif cod_acao == 'A':
            i += 1
        elif cod_acao == 'X':
            i += 1
            print(f"ERRO NA LINHA {token_value_pair[2]}: Símbolo {token_value_pair[1]} inesperado!")
        elif cod_acao == 'Z':
            print(f"ERRO NA LINHA {token_value_pair[2]}: Símbolo {token_value_pair[1]} inesperado.")
            num_celula = int(celula[1:])
            pilha = reduz(pilha, num_celula, tabela_df)
        elif cod_acao == 'W':
            i += 1
            print(f"ERRO NA LINHA {token_value_pair[2]}: Símbolo {token_value_pair[1]} inesperado. {dicionario_tokens[celula[1:]]} faltante.")
        else:
            print("ERRO NO COMPILADOR!")
        
    print("-"*5+"Análise sintática finalizada!"+"-"*5)

if __name__ == '__main__':
    sintatico()      
