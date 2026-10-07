class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.valor = preço

    def aplicar_desconto(self, percentual):
        desconto = self.valor * percentual / 100 
        preço_final = self.valor - desconto
        return preço_final

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preço, validade):
        super().__init__(nome, preço)
        self.validade = validade

produto1 = ProdutoAlimenticio("maça", 10, "10/2026")
resultado = produto1.aplicar_desconto(1)
print(resultado)
print(produto1.validade)