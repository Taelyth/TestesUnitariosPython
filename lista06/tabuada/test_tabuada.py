from tabuada import tabuada


class TesteTabuada:

    def test_tabuada(self):
        assert tabuada(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]