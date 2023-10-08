class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        #melhoria1: alterar print para return
        #bug1: self.cuisine_type sendo exibido após string que descreve nome do restaurente, deveria ser exibido o self.restaurant_name
        #melhoria2: tranformar esses dois prints em apenas um return de uma string utilizando quebra de linha (/n)
        #melhoria3: corrigir typos, manter string em apenas um idioma, alteração de alguns tempos verbais para mensagem ficar mais coerente com a regra de negócio.
        #print(f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        #print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")
        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}.\n" \
               f"Esse restaurante está servindo {self.number_served} consumidor(es) desde que está aberto."
    def open_restaurant(self):
        """Retorne uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            #bug2: self.open deve receber True, caso não esteja aberto. pois o método abre o restaurante
            self.open = True
            #bug3: o correto é atribuir zero ao number served quando o resturante é aberto
            self.number_served = 0
            #substituir print por return
            #print(f"{self.restaurant_name} agora está aberto!")
            return f"{self.restaurant_name} agora está aberto!"
        else:
            #substituir print por return
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Retorne uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            # substituir print por return
            return f"{self.restaurant_name} agora está fechado!"
        else:
            # substituir print por return
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            #melhoria4: adicionar return para indicar que número de clientes foi atualizado
            return f"Número de clientes alterado para {total_customers}"
        else:
            # substituir print por return
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante.
            retorna mensagem indicando quandos usuários foram incrementados.
            Caso restaurante esteja fechado, é retornada mensagem indicando que ele está fechado
        """
        if self.open:
            # bug4: se é incremento, deve ser adicionado o valor ao total de number_served, não atribuir novo valor. subtituir por +=
            # substituir print por return
            self.number_served += more_customers
            return f"Número de clientes servidos incrementado em {more_customers}"
        else:
            # substituir print por return
            return f"{self.restaurant_name} está fechado!"
