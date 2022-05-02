def get_token(line, token_list, line_number):
    token_candidate = line.split(' ', 1)[0]
    token_candidate = token_candidate.split('(', 1)[0]
    token_candidate = token_candidate.split(')', 1)[0]
    token_candidate = token_candidate.split('{', 1)[0]
    token_candidate = token_candidate.split('}', 1)[0]
    token_candidate = token_candidate.split('\n', 1)[0]
    token_candidate = token_candidate.split('\t', 1)[0]

    if token_candidate[0] == 'a':
        if token_candidate[1:] == 'junta':
            token_list.append(['opAritBin', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'rranca':
            token_list.append(['opAritBin', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1

    elif token_candidate[:2] == 'ca':
        if token_candidate[2:] == 'paz':
            token_list.append(['opLogBin', token_candidate, line_number])
            return 0
        elif token_candidate[2:] == 'scah':
            token_list.append(['opAritBin', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1
    
    elif token_candidate[:2] == 'di':
        if token_candidate[2:] in ['_vera', '_contah', '_midih', '_prosa']:
            token_list.append(['type', token_candidate, line_number])
            return 0
        elif token_candidate[2:] in ['mais_da_conta', 'menos_da_conta']:
            token_list.append(['opRel', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1

    elif token_candidate[0] == 'e':
        if token_candidate[1:] == 'h':
            token_list.append(['=', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == '_tem_cabimento':
            token_list.append(['elif', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'spiah_soh':
            token_list.append(['print', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1
    
    elif token_candidate == 'f':
        token_list.append(['bool', token_candidate, line_number])
        return 0
        
    elif token_candidate == 'i':
        token_list.append(['opLogBin', token_candidate, line_number])
        return 0

    elif token_candidate[0] == 'm':
        if token_candidate[1:] in ['ais_um_cadin', 'enos_um_cadin']:
            token_list.append(['opAritUn', token_candidate, line_number])
            return 0
        elif token_candidate[1:] in ['aioh', 'enoh', 'aioh_qui_nem', 'enoh_qui_nem']:
            token_list.append(['opRel', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1

    elif token_candidate[0] == 'n':
        if token_candidate[1:] == 'eim':
            token_list.append(['opLogUn', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'um_eh':
            token_list.append(['opRel', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'um_tem_cabimento':
            token_list.append(['else', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1
    
    elif token_candidate[0] == 'o':
        if token_candidate[1:] == 'u':
            token_list.append(['opLogBin', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'ia':
            token_list.append(['oia', line, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1

    elif token_candidate == 'pica_mula':
        token_list.append(['break', token_candidate, line_number])
        return 0
    
    elif token_candidate == 'qui_nem':
        token_list.append(['opRel', token_candidate, line_number])
        return 0
    
    elif token_candidate == 'sobra':
        token_list.append(['opAritBin', token_candidate, line_number])
        return 0

    elif token_candidate[0] == 't':
        if token_candidate[1:] == 'em_cabimento':
            token_list.append(['if', token_candidate, line_number])
            return 0
        elif token_candidate[1:5] == 'rem_':
            token_list.append(['trem', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1  

    elif token_candidate == 'v':
        token_list.append(['bool', token_candidate, line_number])
        return 0

    elif token_candidate[0] == 'v':
        if token_candidate[1:] == 'eiz':
            token_list.append(['opAritBin', token_candidate, line_number])
            return 0
        elif token_candidate[1:] == 'ai_toda_vida':
            token_list.append(['while', token_candidate, line_number])
            return 0
        else:
            token_list.append(['erro', token_candidate, line_number])
            return -1

    elif token_candidate == 'xove':
        token_list.append(['input', token_candidate, line_number])
        return 0

    else:
        token_list.append(['erro', token_candidate, line_number])
        return -1  