def anagramas(palavra):
    if len(palavra) <= 1:
        return palavra
    else:
        tmp = []
        for aux in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                tmp.append(aux[:i] + palavra[0:1]+aux[i:])
        return tmp
palavra = str(input('Digite uma palavra: '))
cont = len(anagramas(palavra))
print(cont)
