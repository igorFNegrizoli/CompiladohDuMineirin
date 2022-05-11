from get_token import get_token 

write_to_file = True
symbols = ['{','}','(',')',',']
token_list = []

def get_number(line, line_number):
    is_real = False
    line_finished = True
    for idx in range(len(line[1:])):
        if line[idx].isnumeric():
            continue
        elif line[idx] == '.' and not is_real:
            is_real = True
        else:
            line_finished = False
            break

    if line_finished:
        if is_real:
            token_list.append(['real', line[:idx+1], line_number])
        else:
            token_list.append(['int', line[:idx+1], line_number])
    else:
        if is_real:
            token_list.append(['real', line[:idx], line_number])
        else:
            token_list.append(['int', line[:idx], line_number])
    
    pass

def get_string(line, line_number):
    if line[0]=='"':
        quote_idx = line[1:].find('"')+1
    else:
        quote_idx = line[1:].find("'")+1

    if quote_idx == 0:
        print(f"ERRO NA LINHA {line_number}. Fechamento de aspas não encontrado.")
        token_list.append(['erro', line, line_number])
        return -1
    else:
        token_list.append(['string', line[:quote_idx+1], line_number])
        return 0

def check_line(line, line_number):
    new_token = False
    new_token_idx = 0
    for idx in range(len(line)):
        #prints para debuggar
        #print(f"idx: {idx} char: {line[idx]} new_token: {new_token}")
        #print(token_list)

        if not new_token:
            if line[idx].isalpha():
                status = get_token(line[idx:], token_list, line_number)
                if status == -1:
                    print(f"ERRO NA LINHA {line_number}. Símbolo não reconhecido pela linguagem: {token_list[-1][1]}")
                if token_list[-1][0]=='oia':
                    break
                elif len(token_list[-1][1])!=1:
                    new_token = True
                    new_token_idx = 1
            elif line[idx].isnumeric():
                get_number(line[idx:], line_number)
                if len(token_list[-1][1])!=1:
                    new_token = True
                    new_token_idx = 1                
            elif line[idx] == "'" or line[idx]=='"':
                get_string(line[idx:], line_number)==0
                new_token = True
                new_token_idx = 1
                
            elif line[idx] in symbols:
                token_list.append([line[idx], line[idx], line_number])
            elif line[idx] == ' ' or line[idx] == '\t' or line[idx]=='\n':
                continue
            else:
                print(f"ERRO NA LINHA {line_number}. Símbolo não reconhecido pela linguagem: {line[idx]}")
        
        else: 
        #é um new_token
            if line[idx] == token_list[-1][1][new_token_idx]:
            #if que percorre tokens já adicionados à lista
                if new_token_idx==len(token_list[-1][1])-1:
                    new_token = False
                    new_token_idx = 0
                else:
                    new_token_idx += 1
            else:
                print("ERRO DESCONHECIDO.")
                pass
        
def lexico(ask_input, source_code_file, option):
    if ask_input:
        print("Insira o nome do arquivo .uai a ser analisado lexicamente")
        print("Ex: sample_code.uai")

        source_code_file = input()

        print("Deseja visualizar os tokens no terminal ou em um arquivo?")
        print("Arquivo: 0, Terminal: 1")
        option = input()
    
        while option != '0' and option!='1':
            print("Opção não reconhecida.")
            print("Deseja visualizar os tokens no terminal ou em um arquivo?")
            print("Arquivo: 0, Terminal: 1")
            option = input()

    source_code = open(source_code_file)

    line_number = 1
    for line in source_code:
        check_line(line,line_number)
        line_number+=1

    idx = 0
    for i in range(len(token_list)):
        if token_list[idx][0] == 'erro':
            token_list.pop(idx)
        else:
            idx+=1

    if option=='0':
        f = open("tokens.txt", "w")
        for token in token_list:
            f.write(str(token)+"\n")
        f.close
    else:
        for token in token_list:
            print(str(token))
    
    print("-"*6+"Análise léxica finalizada!"+"-"*7)

if __name__ == '__main__':
    lexico(True, "", "")