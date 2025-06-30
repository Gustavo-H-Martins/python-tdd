from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2020_deve_retornar_25(self):
        # Given-Contexto
        entrada = "13/03/2000"
        esperado = 25
        
        funcionario_teste = Funcionario("Teste", entrada, 1111)
        # When-Ação
        resultado = funcionario_teste.idade()

        # Then-Verificação
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        # Given-Contexto
        entrada = " Lucas Carvalho "
        esperado = "Carvalho"

        lucas = Funcionario(entrada, "11/11/2000", 1111)
        # When-Ação
        resultado = lucas.sobrenome()

        # Then-Verificação
        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_9000(self):
        entrada_salario = 100000 # Given-Contexto
        entrada_nome = "Paulo Bragança"
        esperado = 90000 # When-ação

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrementar_salario() # When-ação

        resultado = funcionario_teste.salario

        assert resultado == esperado # Then-desfecho