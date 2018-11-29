import csv
import this


class Funcionarios:
    def __init__(self, nme, rg, sexo, datanasc, telefone, endereco, cargo):
        self.nme = nme
        self.rg = rg
        self.sexo = sexo
        self.datanasc = datanasc
        self.tel = telefone
        self.end = endereco
        self.cargo = cargo

    def inserir(self, func):
        func.nme = input("Nome: ")
        func.rg = int(input("RG: "))
        func.sexo = input("Sexo: ")
        func.datanasc = input("Data de Nascimento(dd/mm/aaaa): ")
        func.tel = int(input("Telefone: "))
        func.end = input("Endereço: ")
        func.cargo = input("Cargo: ")
        with open('FuncionarioDados - Pagina1.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([func.nme, func.rg, func.sexo, func.datanasc, func.tel, func.end, func.cargo])
    def alterar(self):
        print("Alterar dados aqui")

    def pesquisar(self):
        print("Pesquisar Funcionarios aqui")

    def deletar(self):
        print("Deletar Funcionários aqui")
