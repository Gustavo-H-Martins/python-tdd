from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = ' Lucas Carvalho ' # Given-Contexto
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_9000(self):
        entrada = 100000 # Given-Contexto
        esperado = 90000 # When-ação
        
        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        funcionario_teste.decressimo_salario() # When-ação

        resultado = funcionario_teste.salario

        assert resultado == esperado # Then-desfecho