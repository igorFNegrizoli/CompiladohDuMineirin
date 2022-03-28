import token

def read_token_file(token_list):
    f = open("tokens.txt")

    for line in f:
        token_end=2
        for char in line[2:-2]:
            if char=="'":
                break
            token_end+=1

        token = line[2:token_end]
        value = line[token_end+4:-3]

        token_list.append([token,value])

token_list = []
read_token_file(token_list)

for token_value_pair in token_list:
    pass