
class Pessoa(object):
    # Atributo da classe: quando for comum a todos os objetos
    olhos = 2

    def __init__(self, nome=None):
        self.nome = nome

    def metodo_da_instancia(self):
        return 'Método da instância'

    # Criando método de classe
    @staticmethod
    def metodo_de_classe():
        return 'Método de classe'

    # Criando método de classe através do decorator @classemethod
    @classmethod
    def metodo_de_classe_2(cls):
        return '{}'.format(cls.olhos)


## Herança

class Homem(Pessoa):
    pass




if __name__ == '__main__':
    obj = Pessoa('Jardel')
    print(obj.nome)
    print(obj.metodo_de_classe())
    print(Pessoa.metodo_de_classe())
    try:
        print()
        #print(Pessoa.metodo_da_instancia())
    except:
        print('Esse não é um método de classe')

    print(Pessoa.metodo_de_classe_2())

    # Verificando a instância
    print(isinstance(Pessoa, Homem)) # False
    print(isinstance(Homem, Pessoa))



