import pandas as pd

temp_var_counter, label_var_counter, if_counter = 0,0,0
label_queue = []
gen_buffer = []
in_block = []
while_label_stack = []

producoes = {
    0: ['X', 2, ''],
    1: ['A', 4, 'S'],
    2: ['A', 2, 'S'],
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
    21:['H', 14, 'R'],
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
    36:['O', 10, 'P'],
    37:['O', 6, 'Q'],
    38:['O', 6, 'Q'],
    39:['O', 8, 'I'],
    40:['O', 4, 'J'],
    41:['O', 4, 'J'],
    42:['P', 6, 'M'],
    43:['P', 2, 'L'],
    44:['P', 2, 'L'],
    45:['R', 8, 'T'],
    46:['S', 8, 'N'],
    47:['S', 8, 'D'],
    48:['T', 2, 'L'],
    49:['T', 6, 'K'],
    50:['T', 2, 'O'],
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
        if is_type(tipo_esquerda):
            return str(valor_direita)
        else:
            buffer_semantico.append("ERRO NO COMPILADOR. PASSAGEM DE VALOR.")
            return ''
        
def ad_tab_simb(pilha, nome, tipo, valor, tabela_simbolos, linha):
    for ele in pilha[::-1]:
        if type(ele) != int:
            if ele[0] == 'while' and tipo != '':
                buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome} DECLARADA DENTRO DE LAÇO DE REPETIÇÃO.")
                return '', ''
    
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
        else:
            buffer_semantico.append(f"ERRO NA LINHA {linha}. VARIAVEL {nome} JÁ DECLARADA PREVIAMENTE.")
            return '', ''
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
                #return str(int(valor)+1), 'int'
                return '', 'int'
            else:
                #return str(float(valor)+1.0), 'real'
                return '', 'real'
        else:
            print_tipo_nao_suportado(linha, tipo_operando, operador)
    elif operador=='menos_um_cadin':
        if is_number(tipo_operando):
            if valor == 'input':
                return 'input'  
            elif is_int(tipo_operando):
                #return str(int(valor)-1), 'int'
                return '', 'int'
            else:
                #return str(float(valor)-1.0), 'real'
                return '', 'real'
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
                    #return str(int(valor1)+int(valor2)), 'int'
                    return '', 'int'
                elif operador=='arranca':
                    #return str(int(valor1)-int(valor2)), 'int'
                    return '', 'int'
                elif operador=='veiz':
                    #return str(int(valor1)*int(valor2)), 'int'
                    return '', 'int'
                elif operador=='cascah':
                    #return str(int(valor1)//int(valor2)), 'int'
                    return '', 'int'
                else:
                    #return str(int(valor1)%int(valor2)), 'int'
                    return '', 'int'
            else:
                #Se uma variável é Int, converte Int para Float
                if valor1=='input' or valor2=='input':
                    return 'input', 'real'
                elif operador=='ajunta':
                    #return str(float(valor1)+float(valor2)), 'real'
                    return '', 'real'
                elif operador=='arranca':
                    #return str(float(valor1)-float(valor2)), 'real'
                    return '', 'real'
                elif operador=='veiz':
                    #return str(float(valor1)*float(valor2)), 'real'
                    return '', 'real'
                elif operador=='cascah':
                    #return str(float(valor1)/float(valor2)), 'real'
                    return '', 'real'
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
                #return bool_to_minerin(float(valor1)>float(valor2)), 'bool'
                return '', 'bool'
            elif operador=='menoh':
                #return bool_to_minerin(float(valor1)<float(valor2)), 'bool'
                return '', 'bool'
            elif operador=='maioh_qui_nem':
                #return bool_to_minerin(float(valor1)>=float(valor2)), 'bool'
                return '', 'bool'
            elif operador=='menoh_qui_nem':
                #return bool_to_minerin(float(valor1)<=float(valor2)), 'bool'
                return '', 'bool'
            elif operador=='dimais_da_conta':
                #return bool_to_minerin(float(valor1)>(100*float(valor2))), 'bool'
                return '', 'bool'
            else:
                #return bool_to_minerin(float(valor1)<(100*float(valor2))), 'bool'
                return '', 'bool'
    elif operador in operadores_relacionais:
        if is_real(tipo_valor1):
            if is_number(tipo_valor2) or valor2.replace('.','',1).isdigit():
                if operador=='qui_nem':
                    #return bool_to_minerin(float(valor1)==float(valor2)), 'bool'
                    return '', 'bool'
                elif operador=='num_eh':
                    #return bool_to_minerin(float(valor1)!=float(valor2)), 'bool'
                    return '', 'bool'
            else:
                print_tipo_nao_suportado(linha, tipo_valor2, operador)
        elif is_int(tipo_valor1):
            if is_number(tipo_valor2) or valor2.replace('.','',1).isdigit():
                if operador=='qui_nem':
                    #return bool_to_minerin(float(valor1)==float(valor2)), 'bool'
                    return '', 'bool'
                elif operador=='num_eh':
                    #return bool_to_minerin(float(valor1)!=float(valor2)), 'bool'
                    return '', 'bool'
            else:
                print_tipo_nao_suportado(linha, tipo_valor2, operador)
        else:
            if is_real(tipo_valor2):
                valor2 = str(float(valor2))
            elif is_int(tipo_valor2):
                valor2 = str(int(valor2))
            if operador=='qui_nem':
                #return bool_to_minerin(valor1==valor2), 'bool'
                return '', 'bool'
            elif operador=='num_eh':
                #return bool_to_minerin(valor1!=valor2), 'bool'
                return '', 'bool'
        
    else:
        buffer_semantico.append("ERRO NO COMPILADOR. OPERAÇÃO BINÁRIA.")

    return '', ''
        
def concat(val1, val2, tabela_simbolos):
    tipo1, valor1, indice1 = find_in_tab_simb(val2, tabela_simbolos)
    return val1+'\nprintf '+valor1, 'string'
    

def find_while(pilha, linha):
    for ele in pilha[::-1]:
        if type(ele) != int:
            if ele[0] == 'while':
                gen(f"goto LW{len(while_label_stack)}")
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

def get_valor(operando):
    if operando.tipo == 'bool':
        if operando.valor == 'v':
            operando.valor = 1
        else:
            operando.valor = 0
    
    return operando

def three_add_producao_opAritUn(nome1, operador, tabela_simbolos):
    global temp_var_counter
    tipo1, valor1, indice1 = find_in_tab_simb(nome1, tabela_simbolos)

    if indice1 != -1:
        nome1 = nome1[5:]  
    if operador == 'mais_um_cadin':
        gen(f"t{temp_var_counter} = {nome1}++")  
    elif operador == 'menos_um_cadin':
        gen(f"t{temp_var_counter} = {nome1}--")  
    temp_var_counter += 1
    return 't'+str(temp_var_counter-1) 

def three_add_producao_opLogUn(nome1, tabela_simbolos):
    global temp_var_counter
    tipo1, valor1, indice1 = find_in_tab_simb(nome1, tabela_simbolos)

    if nome1 == 'v':
        nome1 = 1
    elif nome1 == 'f':
        nome1 = 0

    if indice1 != -1:
        nome1 = nome1[5:]    
    gen(f"t{temp_var_counter} = !{nome1}")
    temp_var_counter += 1
    return 't'+str(temp_var_counter-1)

def three_add_producao_opBin(nome1, nome2, operacao, tabela_simbolos):
    global temp_var_counter
    operadores_logicos = ['i', 'ou', 'capaz']
    operadores_aritmeticos = ['ajunta', 'arranca', 'veiz', 'cascah', 'sobra']
    operadores_relacionais_numericos = ['maioh', 'menoh', 'maioh_qui_nem', 'menoh_qui_nem']
    operadores_relacionais = ['qui_nem', 'num_eh']

    dict_op = {
        'i': '&&',
        'ou': '||',
        'capaz': '^',
        'ajunta': '+',
        'arranca': '-',
        'veiz': '*',
        'cascah': '/',
        'sobra': '%',
        'maioh': '>',
        'menoh': '<',
        'maioh_qui_nem': '>=',
        'menoh_qui_nem': '<=',
        'qui_nem': '==',
        'num_eh': '!='
    }

    tipo1, valor1, indice1 = find_in_tab_simb(nome1, tabela_simbolos)
    tipo2, valor2, indice2 = find_in_tab_simb(nome2, tabela_simbolos)
    if nome1 == 'v':
        nome1 = 1
    elif nome1 == 'f':
        nome1 = 0
    
    if nome2 == 'v':
        nome2 = 1
    elif nome2 == 'f':
        nome2 = 0

    if indice1 != -1:
        nome1 = nome1[5:]
    if indice2 != -1:
        nome2 = nome2[5:]

    if operacao in operadores_logicos:
        gen(f"t{temp_var_counter} = {nome1} {dict_op[operacao]} {nome2}")
        temp_var_counter += 1
        return 't'+str(temp_var_counter-1)
    elif operacao == 'dimais_da_conta':
        if is_real(tipo1) and is_int(tipo2):
            gen(f"t{temp_var_counter} = (float) {nome2}")
            nome2 = f't{temp_var_counter}' 
            temp_var_counter += 1
        elif is_real(tipo2) and is_int(tipo1):
            gen(f"t{temp_var_counter} = (float) {nome1}")
            nome1 = f't{temp_var_counter}' 
            temp_var_counter += 1
        gen(f"t{temp_var_counter} = 100 * {nome2}")
        temp_var_counter += 1
        gen(f"t{temp_var_counter} = {nome1} > t{temp_var_counter-1}")
        temp_var_counter += 1
        return 't'+str(temp_var_counter-1)
    elif operacao == 'dimenos_da_conta':
        if is_real(tipo1) and is_int(tipo2):
            gen(f"t{temp_var_counter} = (float) {nome2}")
            nome2 = f't{temp_var_counter}' 
            temp_var_counter += 1
        elif is_real(tipo2) and is_int(tipo1):
            gen(f"t{temp_var_counter} = (float) {nome1}")
            nome1 = f't{temp_var_counter}' 
            temp_var_counter += 1
        gen(f"t{temp_var_counter} = 100 * {nome1}")
        temp_var_counter += 1
        gen(f"t{temp_var_counter} = t{temp_var_counter-1} < {nome2}")
        temp_var_counter += 1
        return 't'+str(temp_var_counter-1)
    elif operacao in operadores_relacionais_numericos or operacao in operadores_aritmeticos:
        if is_real(tipo1) and is_int(tipo2):
            gen(f"t{temp_var_counter} = (float) {nome2}")
            nome2 = f't{temp_var_counter}' 
            temp_var_counter += 1
        elif is_real(tipo2) and is_int(tipo1):
            gen(f"t{temp_var_counter} = (float) {nome1}")
            nome1 = f't{temp_var_counter}' 
            temp_var_counter += 1
        gen(f"t{temp_var_counter} = {nome1} {dict_op[operacao]} {nome2}")
        temp_var_counter += 1
        return 't'+str(temp_var_counter-1)
    elif operacao in operadores_relacionais:
        if (is_real(tipo1) and is_int(tipo2)) or (is_string(tipo2) and is_real(tipo1)):
            gen(f"t{temp_var_counter} = (float) {nome2}")
            nome2 = f't{temp_var_counter}' 
            temp_var_counter += 1
        elif is_real(tipo2) and is_int(tipo1):
            gen(f"t{temp_var_counter} = (float) {nome1}")
            nome1 = f't{temp_var_counter}' 
            temp_var_counter += 1
        elif is_string(tipo2) and is_int(tipo1):
            gen(f"t{temp_var_counter} = (int) {nome2}")
            nome2 = f't{temp_var_counter}' 
            temp_var_counter += 1
        
        gen(f"t{temp_var_counter} = {nome1} {dict_op[operacao]} {nome2}")
        temp_var_counter += 1
        return 't'+str(temp_var_counter-1)

    pass

def three_add_producao_e(trem1, trem2, tabela_simbolos, tipo2temp=''):
    tipo1, valor1, indice1 = find_in_tab_simb(trem1, tabela_simbolos)
    tipo2, valor2, indice2 = find_in_tab_simb(trem2, tabela_simbolos)
    if tipo2 == '':
        tipo2 = tipo2temp

    cast = ''
    if is_int(tipo1) and (is_real(tipo2) or is_string(tipo2)):
        cast = ' (int)'
    elif is_real(tipo1) and (is_int(tipo2) or is_string(tipo2)):
        cast = ' (float)'
    elif is_string(tipo1) and not is_string(tipo2):
        cast = ' (string)'

    if indice2 == -1:
        if trem2 == 'v':
            valor = 1
        elif trem2 == 'f':
            valor = 0
        else:
            valor = trem2
    else:
        valor = trem2[5:]

    global temp_var_counter
    if tipo2temp == '':
        gen(f"t{temp_var_counter} ={cast} {valor}")
        gen(f"{trem1[5:]} = t{temp_var_counter}")
        temp_var_counter += 1
    else:
        gen(f"{trem1[5:]} = {trem2}")

    pass

def three_add_input(trem):
    global temp_var_counter
    gen(f"t{temp_var_counter} = scanf")
    gen(f"{trem[5:]} = t{temp_var_counter}")
    temp_var_counter += 1

def three_add_print(T):
    gen(f"printf {T}")
    gen("printf \\n")

def three_add_input_trem(trem, tabela_simbolos):
    tipo1, valor1, indice1 = find_in_tab_simb(trem, tabela_simbolos)
    if indice1!=-1:
        return valor1
    else:
        return trem

def three_add_fim_if():
    global gen_buffer, label_var_counter
    for i in range(len(gen_buffer),0,-1):
        if gen_buffer[i-1] == 'goto LX\n':
            gen_buffer[i-1] = f"goto L{label_var_counter-1}\n"
        elif gen_buffer[i-1] == 'goto LXIF\n':
            gen_buffer[i-1] = f"goto L{label_var_counter-1}\n" 
            break   

def three_add_fim_while():
    global gen_buffer, label_var_counter

    for i in range(len(gen_buffer),0,-1):
        if gen_buffer[i-1] == f"goto LW{len(while_label_stack)}\n":
            gen_buffer[i-1] = f"goto L{label_var_counter}\n"

def has_B_in_block(pilha):
    has_B = False
    for i in range(len(pilha)-1,0,-2):
        token = pilha[i-1]
        if token[0]=='{':
            if has_B:
                return has_B
            else:
                return has_B
        elif token[0]=='B':
            has_B = True
    return False

def three_add_reducao_while():
    global in_block, label_var_counter, while_label_stack

    three_add_fim_while()
    gen(f"goto L{while_label_stack.pop(-1)}")
    in_block.pop(-1)
    gen(f"L{label_var_counter}:")
    label_var_counter += 1
    

def three_add_end_block():
    global label_queue, in_block, label_var_counter,if_counter,while_label_stack
    if len(in_block)>0:
        if in_block[-1]=='if':
            label = label_queue[if_counter-1].pop(0)
            gen(f"goto LXIF")
            gen(f"L{label}:")
            in_block.pop(-1)
        elif in_block[-1]=='elif':
            label = label_queue[if_counter-1].pop(0)
            gen(f"goto LX")
            gen(f"L{label}:")
            in_block.pop(-1)
        elif in_block[-1]=='else':
            gen(f"goto L{label_var_counter}")
            gen(f"L{label_var_counter}:")
            label_var_counter += 1
            in_block.pop(-1)
            three_add_fim_if()
            

def gen(linha_add):
    gen_buffer.append(linha_add + '\n')

def aplica_regra_semantica(pilha, tabela_simbolos, regra_semantica, linha):
    if regra_semantica=='A':
        return find_while(pilha, linha)
    elif regra_semantica=='B':
        return ad_tab_simb(pilha, pilha[-2][1], pilha[-4][1], '', tabela_simbolos, linha)
    elif regra_semantica=='C':
        if is_type(pilha[-8][1]):
            ad_tab_simb(pilha, pilha[-6][1], pilha[-8][1], pilha[-2][1], tabela_simbolos, linha)
        else:
            ad_tab_simb(pilha, pilha[-6][1], '', pilha[-2][1], tabela_simbolos, linha)
        three_add_producao_e(pilha[-6][1], pilha[-2][1], tabela_simbolos)
        return '', ''
    elif regra_semantica=='D':
        ad_tab_simb(pilha, pilha[-4][1], '', 'input', tabela_simbolos, linha)
        three_add_input(pilha[-4][1])
        return '', ''
    elif regra_semantica=='E':
        ad_tab_simb(pilha, pilha[-6][1], '', pilha[-2][1], tabela_simbolos, linha)
        three_add_producao_e(pilha[-6][1], pilha[-2][1], tabela_simbolos, pilha[-2][2])
        return '', ''
    elif regra_semantica=='F':
        #operacao logica prod 24
        valorx, tipo = opBin(pilha[-4][1], pilha[-8][1], pilha[-2][1], pilha[-8][2], pilha[-2][2], tabela_simbolos, linha)
        valor = three_add_producao_opBin(pilha[-8][1], pilha[-2][1], pilha[-4][1], tabela_simbolos)
        if valor == None:
            valor = valorx
        return valor, tipo
    elif regra_semantica=='G':
        #operaçao logica prod 22 e 23
        valorx, tipo = opBin(pilha[-4][1], pilha[-6][1], pilha[-2][1], pilha[-6][2], pilha[-2][2], tabela_simbolos, linha)
        valor = three_add_producao_opBin(pilha[-6][1], pilha[-2][1], pilha[-4][1], tabela_simbolos)
        if valor == None:
            valor = valorx
        return valor, tipo
    elif regra_semantica=='H':
        #prod logica prod 25
        _, tipo = opUn(pilha[-4][1], pilha[-2][1], pilha[-2][2], tabela_simbolos, linha)
        valor = three_add_producao_opLogUn(pilha[-2][1], tabela_simbolos)
        return valor, tipo
    elif regra_semantica=='I':
        #operçao aritmetica prod 39
        valor, tipo = opUn(pilha[-2][1], pilha[-6][1], pilha[-6][2], tabela_simbolos, linha)
        valor = three_add_producao_opAritUn(pilha[-6][1], pilha[-2][1], tabela_simbolos)
        return valor, tipo
    elif regra_semantica=='J':
        #operacao aritmetica prod 40 e 41
        valor, tipo = opUn(pilha[-2][1], pilha[-4][1], pilha[-4][2], tabela_simbolos, linha)
        valor = three_add_producao_opAritUn(pilha[-4][1], pilha[-2][1], tabela_simbolos)
        return valor, tipo
    elif regra_semantica=='K':
        return concat(pilha[-6][1], pilha[-2][1], tabela_simbolos)
    elif regra_semantica=='L':
        return checa_variavel(pilha, tabela_simbolos, linha)
    elif regra_semantica=='M':
        return pilha[-4][1], pilha[-4][2]
    elif regra_semantica=='N':
        three_add_print(pilha[-4][1])
        return '',''
    elif regra_semantica=='O':
        valor, tipo = checa_variavel(pilha, tabela_simbolos, linha)
        if valor[1] == 'r':
            valor = valor[5:]
        return valor, 'string'
    elif regra_semantica=='P':
        #operacao aritmetica prod 36
        valorx, tipo = opBin(pilha[-4][1], pilha[-8][1], pilha[-2][1], pilha[-8][2], pilha[-2][2], tabela_simbolos, linha)
        valor = three_add_producao_opBin(pilha[-8][1], pilha[-2][1], pilha[-4][1], tabela_simbolos)
        if valor == None:
            valor = valorx
        return valor, tipo
    elif regra_semantica=='Q':
        #op aritmetica prod 37 e 38
        valorx, tipo = opBin(pilha[-4][1], pilha[-6][1], pilha[-2][1], pilha[-6][2], pilha[-2][2], tabela_simbolos, linha)
        valor = three_add_producao_opBin(pilha[-6][1], pilha[-2][1], pilha[-4][1], tabela_simbolos)
        if valor == None:
            valor = valorx
        return valor, tipo
    elif regra_semantica=='R':
        three_add_fim_if()
        return '',''
    elif regra_semantica=='S':
        three_add_end_block()
        return '',''
    elif regra_semantica=='T':
        three_add_reducao_while()
        return '',''

def empilha(pilha, num_celula, a):
    global label_var_counter, label_queue, in_block, if_counter
    if a[0]=='if':
        in_block.append('if')
        if_counter += 1
        label_queue.append([])
    elif a[0]=='elif':
        in_block.append('elif')
    elif a[0]=='else':
        in_block.append('else')
        if_counter -= 1
    elif a[0]=='while':
        in_block.append('while')
    elif a[0]=='{' and in_block[-1]=='if':
        gen(f"if t{temp_var_counter-1} goto L{label_var_counter}")
        gen(f"goto L{label_var_counter+1}")
        gen(f"L{label_var_counter}:")
        label_var_counter += 1
        label_queue[if_counter-1].append(label_var_counter)
        label_var_counter += 1
    elif a[0]=='{' and in_block[-1]=='elif':
        gen(f"if t{temp_var_counter-1} goto L{label_var_counter}")
        gen(f"goto L{label_var_counter+1}")
        gen(f"L{label_var_counter}:")
        label_var_counter += 1
        label_queue[if_counter-1].append(label_var_counter)
        label_var_counter += 1
    elif a[0]=='{' and in_block[-1]=='while':
        gen(f"L{label_var_counter}:")
        while_label_stack.append(label_var_counter)
        label_var_counter += 1
    pilha.append(a)
    pilha.append(num_celula)

def reduz(pilha, num_celula, tabela_df, tabela_simbolos, linha):
    producao = producoes[num_celula]

    regra_semantica = producao[2]
    if regra_semantica!='':
        value, tipo = aplica_regra_semantica(pilha, tabela_simbolos, regra_semantica, linha)
    else:
        value, tipo = '', ''

    #generate_3add
    
    pilha = pilha[:-producao[1]]   #desempilha 2*|B|

    s = pilha[-1]              #s é topo da pilha

    pilha.append([producao[0], value, tipo])  #empilha A e seu valor
    
    desvio = int(tabela_df.iloc[s][producoes[num_celula][0]])

    pilha.append(desvio)        #empilha desvio

    return pilha

def sintatico():
    open('output_code.txt','w').close()
    
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

    with open("output_code.txt", 'a') as outuput_code: 
        for line in gen_buffer:
            outuput_code.write(line)

    print("-"*5+"Análise semântica finalizada!"+"-"*5)

if __name__ == '__main__':
    sintatico()      
