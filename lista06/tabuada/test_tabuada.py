from tabuada import tabuada, checagem_de_caracteres


class TesteTabuada:

    def test_tabuada(self):
        assert tabuada(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    def test_checagem_de_caracteres_positivo(self):
        assert checagem_de_caracteres(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    def test_checagem_de_caracteres_letras(self):
        assert checagem_de_caracteres('a') == 'Só aceito Números Inteiros!'

    def test_checagem_de_caracteres_negativo(self):
        assert checagem_de_caracteres(-1) == 'Você NÃO pode colocar números negativos'

    def test_checagem_de_caracteres_vazio(self):
        assert checagem_de_caracteres('') == 'Só aceito Números Inteiros!'

    def test_checagem_de_caracteres_decimal(self):
        assert checagem_de_caracteres(0.9) == 'Só aceito Números Inteiros!'

    def test_checagem_de_caracteres_zero(self):
        assert checagem_de_caracteres(0) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
