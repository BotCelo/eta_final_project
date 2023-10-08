from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            #troque print por return
            #melhoria2 transformar os dois textos em apenas 1 e colocá-los no mesmo retorno, corrigir erros de digitação
            #print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            #for flavor in self.flavors:
            #    print(f"\t-{flavor}")
            message = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                message += f"\n\t-{flavor}"
            return message
        else:
            #troque print por return
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                #troque print por return
                #melhoria3: se o método deve verificar se o sabor está disponível, mensagem precisa ser melhorada, porque ela informa toda a lista de sabores.
                #print(f"Temos no momento {self.flavors}!")
                return "Sabor disponível"
            else:
                print(f"Não temos no momento {self.flavors}!")
        else:
            print("Estamos sem estoque atualmente!")

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #if self.flavors:
        #bug5: mesmo que não exista nenhum sabor disponível, deve ser possível adicionar novo sabor ao estoque
        if flavor in self.flavors:
            return "\nSabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
        #else:
        #    return"Estamos sem estoque atualmente!"
