from codigo.bytebank import Funcionario
from pytest import mark, raises

class TestClass:
    def test_quando_idade_recebe_13_03_2020_deve_retornar_25(self):
        # Given-Contexto
        entrada_data_nascimento = "13/03/2000"
        esperado = 25

        funcionario_teste = Funcionario("Teste", entrada_data_nascimento, 1111)
        # When-Ação
        resultado = funcionario_teste.idade()

        # Then-Verificação
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        # Given-Contexto
        entrada_nome = " Lucas Carvalho "
        esperado = "Carvalho"

        lucas = Funcionario(entrada_nome, "11/11/2000", 1111)
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

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 # given-contexto
        esperado = 100

        funcionario_teste = Funcionario("teste", "11/11/2000", entrada_salario)
        resultado = funcionario_teste.calcular_bonus() # when-ação

        assert resultado == esperado # then-verificação
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_dev_retornar_exception(self):               
        with raises(ValueError):
            entrada_salario = 1000000 # given-contexto

            funcionario_teste = Funcionario("teste", "11/11/2000", entrada_salario) # when-ação
            assert funcionario_teste.calcular_bonus() # then-verificação

    def test_quando_retornar_str_deve_retornar_nome_completo(self):
        entrada_nome, entrada_data_nascimento, entrada_salario = "Teste", "11/11/2000", 1111 # Given-Contexto
        esperado = "Funcionario(Teste, 11/11/2000, 1111)"

        funcionario_teste = Funcionario(entrada_nome, entrada_data_nascimento, entrada_salario)
        resultado = funcionario_teste.__str__() # When-Ação

        assert resultado == esperado # Then-Verificação