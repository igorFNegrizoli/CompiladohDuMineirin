from get_token import get_token 

letras = ['a','c','d','e','f','i','m','n','o','p','q','s','t','v','x']
symbols = ['{','}','(',')',',']
token_list = []


def get_number(line, line_number):
    is_real = False
    for idx in range(len(line[1:])):
        if line[idx].isnumeric():
            continue
        elif line[idx] == '.' and not is_real:
            is_real = True
        else:
            break

    if is_real:
        token_list.append(['real', line[:idx+1]])
    else:
        token_list.append(['int', line[:idx+1]])
    
    pass

def get_string(line, line_number):
    if line[0]=='"':
        quote_idx = line[1:].find('"')+1
    else:
        quote_idx = line[1:].find("'")+1

    if quote_idx == 0:
        print(f"ERRO NA LINHA {line_number}. Fechamento de aspas não encontrado.")
        token_list.append(['erro', line])
        return -1
    else:
        token_list.append(['string', line[:quote_idx+1]])
        return 0

def check_line(line, line_number):
    new_token = False
    new_token_idx = 0
    for idx in range(len(line)):
        #print(f"idx: {idx} char: {line[idx]} new_token: {new_token}")
        #print(token_list)
        if not new_token:
            if line[idx] in letras:
                get_token(line[idx:], token_list, line_number)
                if token_list[-1][0]=='oia':
                    break
                elif len(token_list[-1][1])!=1:
                    new_token = True
                    new_token_idx = 1
            elif line[idx].isnumeric():
                get_number(line[idx:], line_number)
                new_token = True
                new_token_idx = 1                
            elif line[idx] == "'" or line[idx]=='"':
                get_string(line[idx:], line_number)==0
                new_token = True
                new_token_idx = 1
                
            elif line[idx] in symbols:
                token_list.append([line[idx],''])
            elif line[idx] == ' ' or line[idx] == '\t' or line[idx]=='\n':
                continue
            else:
                print(f"ERRO NA LINHA {line_number}. Símbolo não reconhecido pela linguagem: {line[idx]}")
        
        else: 
        #é um new_token
            #print(f"new_token_idx: {new_token_idx}")
            if line[idx] == token_list[-1][1][new_token_idx]:
                #print("entrou no if")
            #if que percorre tokens já adicionados à lista
                if new_token_idx==len(token_list[-1][1])-1:
                    new_token = False
                    new_token_idx = 0
                else:
                    new_token_idx += 1
            else:
                #print("ERRO")
                pass
        
source_code = open("sample_code.uai.txt")

#line = source_code.readline()
#check_line(line,1)

line_number = 1
for line in source_code:
    check_line(line,line_number)
    line_number+=1
    print(token_list)