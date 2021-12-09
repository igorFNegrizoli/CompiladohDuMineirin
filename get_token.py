#func(line, token_list, line_number)
#return updated_token_list
#token_list = [['trem','trem_Y'],['{',],]



def get_token(line, token_list, line_number):
    #arrumar o split para pegar (){} tambem
    token_candidate = line.split(' ', 1)[0]

    if token_candidate[0] == 'a':
        if token_candidate[1:] == 'junta':
            return token_list.append(['OpAritBin', token_candidate])
        elif token_candidate[1:] == 'rranca':
            return token_list.append(['OpAritBin', token_candidate])
        else:
            return token_list.append(['erro', token_candidate, line_number])

    if token_candidate[:2] == 'ca':
        if token_candidate[2:] == 'paz':
            return token_list.append(['OpLogBin', token_candidate])
        elif token_candidate[2:] == 'scah':
            return token_list.append(['OpAritBin', token_candidate])
        else:
            return token_list.append(['erro', token_candidate, line_number])
    
    if token_candidate[:2] == 'di':
        if token_candidate[2:] in ['_vera', '_contah', '_midih', '_prosa']:
            return token_list.append(['type', token_candidate])
        elif token_candidate[2:] in ['mais_da_conta', 'dimenos_da_conta']:
            return token_list.append(['opRel', token_candidate])
        else:
            return token_list.append(['erro', token_candidate, line_number])
     

    return token_list
        


if __name__ == '__main__':
    #line = "trem_A qui_nem trem_X"
    #token_list = [["{", ]]
    #print(get_token(line, token_list, line_number))
    print('ajunta'[:1])