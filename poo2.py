class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo): ## o __ antes é chamado encapsulamento
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Método Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro


    # Método Getter para acessar atributos dentro da classe
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    def get_num_regisro(self):
        return self.__num_registro



class Carro(Veiculo):
    # método __init__ será herdado

    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    def movimentar(self): #polimorfismo - o mesmo método se comporta de diferentes maneiras de acordo com a forma que ele é usado
        print(f'Corro muito! ')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo) #a classe da qual o avião herda, esses itens vem de veículo, assim não precisa cirar novas linhas pra modelo e categoria

    def get_categoria(self):
        return self.__cat


    def movimentar(self):
        print(f'Eu voo alto!')


if __name__ == '__main__':
    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()


    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'categoria: {meu_aviao.get_categoria()}')