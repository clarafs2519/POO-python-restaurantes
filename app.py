from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('bollucio', 'pizza')
restaurante_tacos = Restaurante('mexican', 'mexicana')
restaurante_japones = Restaurante('sushisim', 'japones')

restaurante_pizza.receber_avaliacao('clara', 10)
restaurante_pizza.receber_avaliacao('maria', 8)
restaurante_pizza.receber_avaliacao('Ana', 2)




restaurante_japones.alternar_estado()



def main():
    Restaurante.listar_restaurantes()




if __name__ == '__main__':
    main()
