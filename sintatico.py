import pandas as pd

producoes = {
    0: ['X', 2, ''],
    1: ['A', 4, ''],
    2: ['A', 2, ''],
    3: ['B', 2, ''],
    4: ['B', 2, ''],
    5: ['B', 2, ''],
    6: ['B', 2, ''],
    7: ['B', 2, ''],
    8: ['B', 2, ''],
    9: ['B', 2, 'A'],
    10:['C', 4, ''],
    11:['D', 2, 'B'],
    12:['D', 2, ''],
    13:['E', 6, 'C'],
    14:['E', 6, 'C'],
    15:['F', 2, 'L'],
    16:['F', 2, 'L'],
    17:['F', 2, 'L'],
    18:['G', 2, 'L'],
    19:['G', 2, 'L'],
    20:['H', 16, ''],
    21:['H', 14, ''],
    22:['I', 6, 'G'],
    23:['I', 6, 'G'],
    24:['I', 10, 'F'],
    25:['I', 4, 'H'],
    26:['J', 6, 'M'],
    27:['J', 2, 'L'],
    28:['J', 2, 'L'],
    29:['L', 2, 'L'],
    30:['L', 2, 'L'],
    31:['M', 16, ''],
    32:['M', 8 , ''],
    33:['N', 2 , ''],
    34:['N', 6, 'E'],
    35:['N', 6, 'E'],
    36:['O', 10, 'F'],
    37:['O', 6, 'G'],
    38:['O', 6, 'G'],
    39:['O', 8, 'I'],
    40:['O', 4, 'J'],
    41:['O', 4, 'J'],
    42:['P', 6, 'M'],
    43:['P', 2, 'L'],
    44:['P', 2, 'L'],
    45:['R', 8, ''],
    46:['S', 8, ''],
    47:['S', 8, 'D'],
    48:['T', 2, 'L'],
    49:['T', 6, 'K'],
    50:['T', 2, 'L'],
    51:['U', 2, 'L'],
    52:['U', 2, 'L'],
    53:['U', 2, 'L']
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

buffer_semantico = []

def is_bool(tipo):
    tipos_booleanos = ['di_vera', 'bool']
    return tipo in tipos_booleanos

def is_number(tipo):
    tipos_numericos = ['di_contah', 'di_midih', 'int', 'real']
    return tipo in tipos_numericos

def is_int(tipo):
    tipos_inteiros = ['di_contah', 'int']
    return tipo in tipos_inteiros

def is_real(tipo):
    tipos_reais = ['di_midih', 'real']
    return tipo in tipos_reais

def is_string(tipo):
    tipos_string = ['di_prosa', 'string']
    return tipo in tipos_string

def is_type(tipo):
    tipos = ['di_contah', 'di_midih', 'int', 'real', 'di_prosa', 'string', 'di_vera', 'bool']
    return tipo in tipos

def find_in_tab_simb(nome, tabela_simbolos):
    #retorna tipo, valor, indice na tabela
    for i in range(len(tabela_simbolos)):
        simb = tabela_simbolos[i]
        if nome == simb[0]:
            return simb[1], simb[2], i
    
    return  '', '', -1

def print_atrib_incompativel(linha):
    buffer_semantico.append(f"ERRO NA LINHA {linha}. ATRIBUIÇÃO NÃO COMPATÍVEL PARA AS VARIÁVEIS UTILIZADAS.")

def passagem_valor(var_esquerda, tipo_esquerda, var_direita, tabela_simbolos, linha, var_declarada):
    tipo_direita, valor_direita, indice_direita = find_in_tab_simb(var_direita, tabela_simbolos)
    indice_esq = 0

    if valor_direita == '':
        buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {var_direita} NÃO TEM VALOR DEFINIDO.")
        return ''    

    if tipo_esquerda=='':
        tipo_esquerda, tab_valor_esq, indice_esq = find_in_tab_simb(var_esquerda, tabela_simbolos)
    if indice_esq == -1:
        buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {var_esquerda} NÃO DECLARADA.")
        return ''
    if indice_direita == -1:
        buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {var_direita} NÃO DECLARADA.")
        return ''
    else:
        if is_string(tipo_esquerda):
            return str(valor_direita)
        elif is_bool(tipo_esquerda):
            if is_bool(tipo_direita):
                return valor_direita
            else:
                print_atrib_incompativel(linha)
                return ''
        elif is_int(tipo_esquerda):
            if valor_direita.replace('.','',1).isdigit():
                if valor_direita == 'input':
                    return str(valor_direita)
                else:
                    return str(int(valor_direita))
            else:
                print_atrib_incompativel(linha)
                return ''
        elif is_real(tipo_esquerda):
            if valor_direita.replace('.','',1).isdigit():
                if valor_direita == 'input':
                    return str(valor_direita)
                else:
                    return str(float(valor_direita))
            else:
                print_atrib_incompativel(linha)
                return ''
        else:
            buffer_semantico.append("ERRO NO COMPILADOR. PASSAGEM DE VALOR.")
            return ''
        
def ad_tab_simb(nome, tipo, valor, tabela_simbolos, linha):
    tipo_tab, valor_tab, i = find_in_tab_simb(nome, tabela_simbolos)
    var_declarada = (i!=-1)

    if valor[:4]=='trem':
        valor = passagem_valor(nome, tipo, valor, tabela_simbolos, linha, var_declarada)

    if not var_declarada:
        if tipo == '':
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome} NÃO FOI DECLARADA.")
            return '', ''
        else:
            #Adição de novo símbolo
            tabela_simbolos.append([nome, tipo, valor])
    else:
        #Atualização de símbolo
        if tipo=='':
            tipo = tipo_tab
        if valor=='':
            valor = valor_tab
        tabela_simbolos[i] = [nome, tipo, valor]
    return '', ''

def print_tipo_nao_suportado(linha, tipo, operador):
    buffer_semantico.append(f"ERRO NA LINHA {linha}. TIPO {tipo} NÃO SUPORTADO PARA OPERAÇÃO {operador}.")

def print_variavel_sem_valor(linha, nome):
    buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome} NÃO TEM VALOR DEFINIDO.")

def bool_to_minerin(bool):
    if bool:
        return 'v'
    else:
        return 'f'

def opUn(operador, valor, tipo_operando, tabela_simbolos, linha):
    #VERIFICAR O QUE ACONTECE COM LITERAIS
    nome = valor
    if tipo_operando=='':
        tipo_operando, valor, _ = find_in_tab_simb(nome, tabela_simbolos)
        if valor == '':
            print_variavel_sem_valor(linha, nome)
            return '', ''
    if operador=='neim':
        if is_bool(tipo_operando):
            if valor == 'v':
                return 'f', 'bool'
            else:
                return 'v', 'bool'
        else:
            print_tipo_nao_suportado(linha, tipo_operando, operador)
    elif operador=='mais_um_cadin':
        if is_number(tipo_operando):
            if valor == 'input':
                return 'input' 
            elif is_int(tipo_operando):
                return str(int(valor)+1), 'int'
            else:
                return str(float(valor)+1.0), 'real'
        else:
            print_tipo_nao_suportado(linha, tipo_operando, operador)
    elif operador=='menos_um_cadin':
        if is_number(tipo_operando):
            if valor == 'input':
                return 'input'  
            elif is_int(tipo_operando):
                return str(int(valor)-1), 'int'
            else:
                return str(float(valor)-1.0), 'real'
        else:
            print_tipo_nao_suportado(linha, tipo_operando, operador)
    else:
        buffer_semantico.append("ERRO NO COMPILADOR. OPERAÇÃO UNÁRIA.")
    
    return '', ''

def opBin(operador, valor1, valor2, tipo_valor1, tipo_valor2, tabela_simbolos, linha):
    nome1 = valor1
    if tipo_valor1=='':
        tipo_valor1, valor1, indice1 = find_in_tab_simb(nome1, tabela_simbolos)
        if indice1 == -1:
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome1} NÃO DECLARADA.")
            return '', ''
        elif valor1 == '':
            print_variavel_sem_valor(linha, nome1)
            return '', ''
    
    nome2 = valor2
    if tipo_valor2=='':
        tipo_valor2, valor2, indice2 = find_in_tab_simb(nome2, tabela_simbolos)
        if indice2 == -1:
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome2} NÃO DECLARADA.")
            return '', ''
        elif valor2 == '':
            print_variavel_sem_valor(linha, nome2)
            return '', ''

    operadores_logicos = ['i', 'ou', 'capaz']
    operadores_aritmeticos = ['ajunta', 'arranca', 'veiz', 'cascah', 'sobra']
    operadores_relacionais_numericos = ['maioh', 'menoh', 'maioh_qui_nem', 'menoh_qui_nem', 'dimais_da_conta', 'dimenos_da_conta']
    operadores_relacionais = ['qui_nem', 'num_eh']
    
    if operador in operadores_logicos:
        if not is_bool(tipo_valor1):
            print_tipo_nao_suportado(linha, tipo_valor1, operador)
        elif not is_bool(tipo_valor2):
            print_tipo_nao_suportado(linha, tipo_valor2, operador)
        else:
            if operador=='i':
                return bool_to_minerin(valor1=='v' and valor2=='v'), 'bool'
            elif operador=='ou':
                return bool_to_minerin(valor1=='v' or valor2=='v'), 'bool'
            else:
                return bool_to_minerin(valor1 != valor2), 'bool'
    elif operador in operadores_aritmeticos:
        if not is_number(tipo_valor1):
            print_tipo_nao_suportado(linha, tipo_valor1, operador)
        elif not is_number(tipo_valor2):
            print_tipo_nao_suportado(linha, tipo_valor2, operador)
        else:
            if is_int(tipo_valor1) and is_int(tipo_valor2):
                if valor1=='input' or valor2=='input':
                    return 'input', 'int'
                elif operador=='ajunta':
                    return str(int(valor1)+int(valor2)), 'int'
                elif operador=='arranca':
                    return str(int(valor1)-int(valor2)), 'int'
                elif operador=='veiz':
                    return str(int(valor1)*int(valor2)), 'int'
                elif operador=='cascah':
                    return str(int(valor1)//int(valor2)), 'int'
                else:
                    return str(int(valor1)%int(valor2)), 'int'
            else:
                #Se uma variável é Int, converte Int para Float
                if valor1=='input' or valor2=='input':
                    return 'input', 'real'
                elif operador=='ajunta':
                    return str(float(valor1)+float(valor2)), 'real'
                elif operador=='arranca':
                    return str(float(valor1)-float(valor2)), 'real'
                elif operador=='veiz':
                    return str(float(valor1)*float(valor2)), 'real'
                elif operador=='cascah':
                    return str(float(valor1)/float(valor2)), 'real'
                elif is_real(tipo_valor1):
                    print_tipo_nao_suportado(linha, tipo_valor1, operador)
                else:
                    print_tipo_nao_suportado(linha, tipo_valor2, operador)
    elif valor1=='input' or valor2=='input':
        return 'input', 'bool'
    elif operador in operadores_relacionais_numericos:
        if not is_number(tipo_valor1):
            print_tipo_nao_suportado(linha, tipo_valor1, operador)
        elif not is_number(tipo_valor2):
            print_tipo_nao_suportado(linha, tipo_valor2, operador)
        else:
            if operador=='maioh':
                return bool_to_minerin(float(valor1)>float(valor2)), 'bool'
            elif operador=='menoh':
                return bool_to_minerin(float(valor1)<float(valor2)), 'bool'
            elif operador=='maioh_qui_nem':
                return bool_to_minerin(float(valor1)>=float(valor2)), 'bool'
            elif operador=='menoh_qui_nem':
                return bool_to_minerin(float(valor1)<=float(valor2)), 'bool'
            elif operador=='dimais_da_conta':
                return bool_to_minerin(float(valor1)>(100*float(valor2))), 'bool'
            else:
                return bool_to_minerin(float(valor1)<(100*float(valor2))), 'bool'
    elif operador in operadores_relacionais:
        if is_real(tipo_valor1):
            if is_number(tipo_valor2) or valor2.replace('.','',1).isdigit():
                if operador=='qui_nem':
                    return bool_to_minerin(float(valor1)==float(valor2)), 'bool'
                elif operador=='num_eh':
                    return bool_to_minerin(float(valor1)!=float(valor2)), 'bool'
            else:
                print_tipo_nao_suportado(linha, tipo_valor2, operador)
        elif is_int(tipo_valor1):
            if is_number(tipo_valor2) or valor2.replace('.','',1).isdigit():
                if operador=='qui_nem':
                    return bool_to_minerin(float(valor1)==float(valor2)), 'bool'
                elif operador=='num_eh':
                    return bool_to_minerin(float(valor1)!=float(valor2)), 'bool'
            else:
                print_tipo_nao_suportado(linha, tipo_valor2, operador)
        else:
            if is_real(tipo_valor2):
                valor2 = str(float(valor2))
            elif is_int(tipo_valor2):
                valor2 = str(int(valor2))
            if operador=='qui_nem':
                return bool_to_minerin(valor1==valor2), 'bool'
            elif operador=='num_eh':
                return bool_to_minerin(valor1!=valor2), 'bool'
        
    else:
        buffer_semantico.append("ERRO NO COMPILADOR. OPERAÇÃO BINÁRIA.")

    return '', ''
        
def concat(val1, val2):
    return val1+val2, 'string'

def find_while(pilha, linha):
    for ele in pilha[::-1]:
        if type(ele) != int:
            if ele[0] == 'while':
                return '', ''
    buffer_semantico.append(f"ERRO NA LINHA {linha}. pica_mula FORA DE UM vai_toda_vida.")   
    return '', ''

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

def checa_variavel(pilha, tabela_simbolos, linha):
    if pilha[-2][0] == 'trem':
        tipo, valor, indice = find_in_tab_simb(pilha[-2][1], tabela_simbolos)
        if indice == -1:
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {pilha[-2][1]} NÃO DECLARADA.")
            return '', ''
        elif valor == '':
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {pilha[-2][1]} NÃO TEM VALOR DEFINIDO.")
            return '', ''

    return pilha[-2][1], pilha[-2][2]

def aplica_regra_semantica(pilha, tabela_simbolos, regra_semantica, linha):
    if regra_semantica=='A':
        return find_while(pilha, linha)
    elif regra_semantica=='B':
        return ad_tab_simb(pilha[-2][1], pilha[-4][1], '', tabela_simbolos, linha)
    elif regra_semantica=='C':
        if is_type(pilha[-8][1]):
            return ad_tab_simb(pilha[-6][1], pilha[-8][1], pilha[-2][1], tabela_simbolos, linha)
        else:
            return ad_tab_simb(pilha[-6][1], '', pilha[-2][1], tabela_simbolos, linha)
    elif regra_semantica=='D':
        return ad_tab_simb(pilha[-4][1], '', 'input', tabela_simbolos, linha)
    elif regra_semantica=='E':
        return ad_tab_simb(pilha[-6][1], '', pilha[-2][1], tabela_simbolos, linha)
    elif regra_semantica=='F':
        return opBin(pilha[-4][1], pilha[-8][1], pilha[-2][1], pilha[-8][2], pilha[-2][2], tabela_simbolos, linha)
    elif regra_semantica=='G':
        return opBin(pilha[-4][1], pilha[-6][1], pilha[-2][1], pilha[-6][2], pilha[-2][2], tabela_simbolos, linha)
    elif regra_semantica=='H':
        return opUn(pilha[-4][1], pilha[-2][1], pilha[-2][2], tabela_simbolos, linha)
    elif regra_semantica=='I':
        return opUn(pilha[-2][1], pilha[-6][1], pilha[-6][2], tabela_simbolos, linha)
    elif regra_semantica=='J':
        return opUn(pilha[-2][1], pilha[-4][1], pilha[-4][2], tabela_simbolos, linha)
    elif regra_semantica=='K':
        return concat(pilha[-6][1], pilha[-2][1])
    elif regra_semantica=='L':
        return checa_variavel(pilha, tabela_simbolos, linha)
    elif regra_semantica=='M':
        return pilha[-4][1], pilha[-4][2]

def empilha(pilha, num_celula, a):
    pilha.append(a)
    pilha.append(num_celula)

def reduz(pilha, num_celula, tabela_df, tabela_simbolos, linha):
    producao = producoes[num_celula]

    regra_semantica = producao[2]
    if regra_semantica!='':
        value, tipo = aplica_regra_semantica(pilha, tabela_simbolos, regra_semantica, linha)
    else:
        value, tipo = '', ''
    
    pilha = pilha[:-producao[1]]   #desempilha 2*|B|

    s = pilha[-1]              #s é topo da pilha

    pilha.append([producao[0], value, tipo])  #empilha A e seu valor
    
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

    tabela_simbolos = []

    while(i < len(token_list)):
        s = pilha[-1]
        token_value_pair = token_list[i]

        a = token_value_pair[0]         #token lido do par
        value = token_value_pair[1]     #valor lido do par
        tipo = ''
        if a == 'int' or a=='real' or a=='bool':
            tipo = a

        celula = tabela_df.iloc[int(s)][a]

        cod_acao = celula[0]
        
        if cod_acao == 'E':
            num_celula = int(celula[1:])
            empilha(pilha, num_celula, [a, value, tipo])
            i += 1
        elif cod_acao == 'R':
            num_celula = int(celula[1:])
            pilha = reduz(pilha, num_celula, tabela_df, tabela_simbolos, token_value_pair[2])
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
            if celula[1:] == '$':
                print(f"ERRO NA LINHA {token_value_pair[2]}: Símbolo {token_value_pair[1]} inesperado.")
            else:
                print(f"ERRO NA LINHA {token_value_pair[2]}: Símbolo {token_value_pair[1]} inesperado. {dicionario_tokens[celula[1:]]} faltante.")
        else:
            print("ERRO NO COMPILADOR!")
        
    print("-"*5+"Análise sintática finalizada!"+"-"*5)

    for erro in buffer_semantico:
        print(erro)

    print("-"*5+"Análise semântica finalizada!"+"-"*5)

if __name__ == '__main__':
    sintatico()      
