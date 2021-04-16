def opcoes():
    print('1 - Inserir salário')
    print('2 - Horas trabalhadas')
    print('3 - Sálario bruto')
    print('4 - Pagamento ao INSS')
    print('5 - Pagamento ao sindicato')
    print('6 - Sálario líquido')
    print('7 - Sair')
    item = input('\nEscolha uma opção: ')
    return item

def verificador(salario_total, horas):
    verifica = False
    if salario_total > 0 and horas > 0:
        retorno_verifica = True
        return retorno_verifica
    else:
        verifica = False
        return verifica

def mensagem():
    print('\nNÃO HÁ DADOS SUFICIENTES\n')

def opcao_1():
    salario = float(input('\nInsira quanto você ganha por hora: '))
    if salario == 0:
        salario_total = 0
        verificador(salario_total, 0)
        verifica = False
        print('\nINSIRA O DADO CORRETAMENTE!')
        return verifica
    else:
        salario_total = salario
        verificador(salario_total, 0)
        return salario_total

def opcao_2():
    horas_trabalhadas = int(input('\nInsira o número de horas trabalhadas: '))
    if horas_trabalhadas == 0:
        horas = 0
        verificador(0, horas)
        verifica = False
        print('\nINSIRA O DADO CORRETAMENTE!')
        return verifica
    else:
        horas = horas_trabalhadas
        verificador(0, horas)
        return horas

def opcao_3():
        salario_bruto = salario_total * horas
        salario_duro = salario_bruto
        print('R${:.2f}'.format(salario_duro))
        return salario_duro

def opcao_4():
    inss = salario_duro * 0.11
    print(inss)
    return inss

def opcao_5():
    sind = salario_duro * 0.02
    print(sind)
    return sind

def opcao_6():
    if Inss == 0 or Sind == 0:
        mensagem()
    else:
        liquid = salario_duro - Inss - Sind
        print(liquid)
        return liquid

escolha = '0'
salario_total = 0
horas = 0
salario_duro = 0
Inss = 0
Sind = 0
Liquid = 0

while escolha != '7':
    retorno_verifica = verificador(salario_total, horas)
    escolha = opcoes()
    if escolha == '1':
        salario_total = opcao_1()
    elif escolha == '2':
        horas = opcao_2()
    elif escolha == '3':
        if retorno_verifica == True:
            salario_duro = opcao_3()
        else:
            mensagem()
    elif escolha == '4':
        if retorno_verifica == True and salario_duro > 0:
            Inss = opcao_4()
        else:
            mensagem()
    elif escolha == '5':
        if retorno_verifica == True and salario_duro > 0:
            Sind = opcao_5()
        else:
            mensagem()
    elif escolha == '6':
        if retorno_verifica == True:
            Liquid = opcao_6()
        else:
            mensagem()
    elif escolha == '7':
        print('\nSaindo...\n')   
    else:
        print('\nOpção desconhecida!\n')
    
    input('Pressione ENTER para continuar')