#orientação a objetos: paradigma de programação

#Classes e Objetos

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




if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'Registro: {meu_veiculo.get_num_regisro()}\n')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()