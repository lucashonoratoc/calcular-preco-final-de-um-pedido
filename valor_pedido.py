valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

total_harmburguer = valorHamburguer * quantidadeHamburguer

total_bebida = valorBebida * quantidadeBebida

total = total_bebida + total_harmburguer

troco = valorPago - total

mensagem = f'O preço final do pedido é R$ {total:.2f}. Seu troco é R$ {troco:.2f}.'
print(mensagem)