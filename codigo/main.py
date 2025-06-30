from bytebank import Funcionario

ana = Funcionario('Ana Bragança', '12/03/1980', 150000)
print(ana.nome)
print(ana.idade())
print(ana.sobrenome())
print(ana.decrementar_salario())
print(ana.calcular_bonus())