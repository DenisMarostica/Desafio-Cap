import re

senha = str(input('Digite sua senha: '))
div = list(senha)
cont = len(div)
cont1 = 6 - cont
flag = 0
while True:
    if len(senha) < 6:
        flag = -1
        break
    elif not re.search("[a-z]", senha):
        flag = -1
        break
    elif not re.search("[A-Z]", senha):
        flag = -1
        break
    elif not re.search("[0-9]", senha):
        flag = -1
        break
    elif not re.search("[!@#$%^&*()_+-]", senha):
        flag = -1
        break
    else:
        flag = 0
        print("Senha Válida")
        break

if flag == -1:
    print(cont1)
