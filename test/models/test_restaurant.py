from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        expected_message = "Esse restaurante se chama Marcelo'S Restaraunt e serve hamburguer.\n" \
                           "Esse restaurante está servindo 0 consumidor(es) desde que está aberto."

        restaurante = Restaurant("marcelo's restaraunt", "hamburguer")
        descricao = restaurante.describe_restaurant()
        assert expected_message == descricao, "mensagem de descrição do resturante diferente da esperada"

    def test_open_restaurant(self):
        expected_response_to_is_open = True
        restaurante = Restaurant("marcelo's restaraunt", "hamburguer")
        restaurante.open_restaurant()
        resturante_status = restaurante.open
        assert expected_response_to_is_open == resturante_status, "status do restaurente diferente do esperado"

    def test_close_restaurant(self):
        expected_response_to_is_open = False
        restaurante = Restaurant("marcelo's restaraunt", "hamburguer")
        restaurante.open_restaurant()
        restaurante.close_restaurant()
        resturante_status = restaurante.open
        assert resturante_status == expected_response_to_is_open, "status do restaurente diferente do esperado"
    def test_set_number_served(self):
        expected_number_served = 10
        restaurante = Restaurant("marcelo's restaraunt", "hamburguer")
        restaurante.open_restaurant()
        restaurante.set_number_served(10)
        number_of_served = restaurante.number_served
        assert number_of_served == expected_number_served, "número de pessoas servidas diferente do esperado"

    def test_increment_number_served(self):
        expected_number_served = 15
        restaurante = Restaurant("marcelo's restaraunt", "hamburguer")
        restaurante.open_restaurant()
        restaurante.set_number_served(10)
        restaurante.increment_number_served(5)
        number_of_served = restaurante.number_served
        assert number_of_served == expected_number_served, "número de pessoas servidas diferente do esperado"
