def funcaozinha(listinha):
    del listinha[:-4]
    print(f"dentro da funcao {listinha}")

listinha = [1,2,3,4,5,6,7,8,9]

funcaozinha(listinha)
print(f"fora da funcao {listinha}")