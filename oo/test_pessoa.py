'''Trabalhando com unitest'''
'''
Utilizando o unitest devemos praticamente utilizar, em todo o código, a palavra test
Comando para testar no terminal

python3 -m unittest discover diretorio

'''


from unittest  import TestCase
from pessoa   import Pessoa


class PessoaTestCase(TestCase):
    jardel = Pessoa('Jardel')
    def testando_a_quantidade_de_olhos(self):
        self.assertEqual(2, self.jardel.olhos) # OK

    def testando_nome(self):
        self.assertEqual('Jardel', self.jardel.nome) # OK