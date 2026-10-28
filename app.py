from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_almoco = Restaurante('almoco', 'comida')
restaurante_tacos = Restaurante('mexican', 'mexicana')
restaurante_japones = Restaurante('sushisim', 'japones')
# restaurante_pizza.receber_avaliacao('Ana', 2)
# restaurante_japones.alternar_estado()

bebida_suco = Bebida('Suco de Laranja', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 30.0, 'O melhor prato da região')
prato_feijoada.aplicar_desconto()
restaurante_almoco.adicionar_item_no_cardapio(bebida_suco)
restaurante_almoco.adicionar_item_no_cardapio(prato_feijoada)


def main():
    restaurante_almoco.exibir_cardapio
    



if __name__ == '__main__':
    main()
