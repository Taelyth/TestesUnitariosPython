from fosforos import calcular_fosforos


class TesteFosforo:

    def test_calcular_fosforos_positivo(self):
        assert calcular_fosforos(2) == 80

    def test_calcular_fosforos_negativo(self):
        assert calcular_fosforos(-1) == 'Você NÃO pode colocar números negativos'

    def test_calcular_fosforos_zero(self):
        assert calcular_fosforos(0) == 'Com 0 Caixas você NÃO possui fósforos'

    def test_calcular_fosforos_vazio(self):
        assert calcular_fosforos("") == 'Só aceito Números Inteiros!'

    def test_calcular_fosforos_letras(self):
        assert calcular_fosforos("b") == 'Só aceito Números Inteiros!'

    def test_calcular_fosforos_decimal(self):
        assert calcular_fosforos(0.2) == 'Só aceito Números Inteiros!'
