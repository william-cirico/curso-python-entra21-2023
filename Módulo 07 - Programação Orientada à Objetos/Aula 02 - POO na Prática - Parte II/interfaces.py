"""
Uma interface é um contrato formal que define um conjunto de métodos que uma classe
deve implementar. Uma interface especifica quais métodos devem estar presentes em 
uma classe, mas não fornece implementações detalhadas desses métodos. Em vez disso, 
ela serve como um guia para as classes que a implementam.

Em Python, a herança múltipla é uma característica que permite que uma classe herde 
de múltiplas classes base. Isso significa que uma classe derivada pode herdar atributos 
e métodos de várias classes base.
"""

from mago import Mago
from guerreiro import Guerreiro
from arqueiro import Arqueiro

guerreiro = Guerreiro("Conan", 10, 100, 50)
mago = Mago("Gandalf", 10, 80, 80)
arqueiro = Arqueiro("Legolas", 10, 90, 70)

guerreiro.usar_habilidade_especial()
mago.usar_habilidade_especial()
arqueiro.usar_habilidade_especial()
