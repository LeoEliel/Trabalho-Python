import csv
from Funcionarios import Funcionarios

CadFuncionarios = []
n = int(input("Criar Funcionarios\n Insira qtd de Funcionarios: "))
i = 0
op = 'a'

for i in range(0, n):
    aux = Funcionarios(None, None, None, None, None, None, None)
    CadFuncionarios.append(aux)
    aux = None

while op != 'S':
    op = input("Selecionar opção: \n[I]nserir Dados\n[A]lterar Dados\n[P]esquisar Dados\n[D]eletar Dados\n[S]air\n")
    op = op.upper()
    if op == 'I':
        x = int(input("Informar Id do Funcionário: "))
        CadFuncionarios[x].inserir(CadFuncionarios[x])
    elif op == 'A':
        x = int(input("Informar Id do Funcionário: "))
        CadFuncionarios[x].alterar(CadFuncionarios[x])
    elif op == 'P':
        x = int(input("Informar Id do Funcionário: "))
        CadFuncionarios[x].pesquisar(CadFuncionarios[x])
    elif op == 'D':
        x = int(input("Informar Id do Funcionário: "))
        CadFuncionarios[x].deletar(CadFuncionarios[x])
    elif op == 'S':
        break
    else:
        print("Opção Não listada...")
    x = None