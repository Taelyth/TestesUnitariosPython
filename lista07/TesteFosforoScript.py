import pytest

from lista06.fosforos.fosforos import calcular_fosforos


class TesteFosforoScript:

    # parametro , resultado_esperado
    massa_fosforo = [
        (2, 80),
        (-1, 'Você NÃO pode colocar números negativos'),
        (0, 'Com 0 Caixas você NÃO possui fósforos'),
        ('', 'Só aceito Números Inteiros!'),
        ('a', 'Só aceito Números Inteiros!'),
        (0.2, 'Só aceito Números Inteiros!')
    ]

    @pytest.mark.parametrize('parametro, resultado_esperado', massa_fosforo)
    def testar_fosforos_script(self, parametro, resultado_esperado):
        assert calcular_fosforos(parametro) == resultado_esperado
