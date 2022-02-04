# TestesUnitariosPython
Projeto criado para acompanhar as aulas do curso [Formação em Teste de Software][Iterasys] em **Python**.

Neste projeto temos os exercícios de **Testes Unitários** e **Testes de API**. Assim como Ler arquivos CSV e Json.

---

### Pré-Requisitos
- As bibliotecas que deverão ser instaladas para rodar os códigos são:

```
pytest
requests
```

---

### Glossário

`main.py` Arquivo onde foi feito um teste unitário simples de uma calculadora, para usar massa de teste parametrizada com o `@pytest.mark.parametrize`

`lista06` Diretório contendo os testes unitários de 2 aplicações feitas utilizando o console da IDE, que são:

- `fosforos.py` que é uma calculadora simples da quantidade de fósforos em uma caixa, onde 1 caixa = 40 fósforos.
- `tabuada.py` uma aplicação simples que mostra os 10 primeiros números da tabuada de um número escolhido.

`lista07` Diretório com exemplos dos testes unitários anteriores utilizando massa de testes com `@pytest.mark.parametrize` e `Leitura em CSV`.

`TestesApiPetstore.py` Arquivo contendo os testes de API do swagger [Petstore][Petstore] também é utilizada a leitura de um arquivo `.json`.

`json` Diretório de armazenagem do arquivo `.json` utilizado no teste acima.

`usuario.py` Arquivo contendo os testes de API utilizando a documentação [Regres][Regres] como base e também a leitura csv do arquivo `usuarios.csv`.

`lista08` Mais alguns exercícios de teste em API do swagger [Petstore][Petstore] com leitura de Json, variáveis e Dicionário.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/
[Petstore]: https://petstore.swagger.io/
[Regres]: https://reqres.in/

<!-- imagens -->
[Iterasys-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)