from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        expected_message = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t-amendoim\n\t-abacaxi"
        sorveteria = IceCreamStand('sorveteria do celo', "sorvete", ['amendoim', 'abacaxi'])
        sabores_disponiveis = sorveteria.flavors_available()
        assert expected_message == sabores_disponiveis

    def test_find_flavor(self):
        resposta_esperada = "Sabor disponível"
        sorveteria = IceCreamStand('sorveteria do celo', "sorvete", ['amendoim', 'abacaxi'])
        resposta = sorveteria.find_flavor('amendoim')
        assert resposta_esperada == resposta

    def test_add_flavor(self):
        resposta_esperada = "amendoim adicionado ao estoque!"
        sorveteria = IceCreamStand('sorveteria do celo', "sorvete", [])
        resposta = sorveteria.add_flavor('amendoim')
        assert resposta == resposta_esperada