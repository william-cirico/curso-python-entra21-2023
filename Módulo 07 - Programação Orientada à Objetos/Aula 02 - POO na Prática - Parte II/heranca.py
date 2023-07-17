"""
Herança é o termo utilizado na OOP para compartilhar atributos e métodos entre duas ou mais classes.
A superclasse ou classe mãe disponibiliza os atributos e métodos que serão herdados pela subclasse ou classe filha.

Classe abstrata é uma classe que não pode ser instanciada, apenas herdada.
"""

from mago import Mago
from guerreiro import Guerreiro
from arqueiro import Arqueiro

guerreiro = Guerreiro("Conan", 10, 100, 50)
mago = Mago("Gandalf", 10, 80, 80)
arqueiro = Arqueiro("Legolas", 10, 90, 70)

guerreiro.atacar()
guerreiro.equipar_escudo()
print()

mago.atacar()
mago.equipar_cajado()
print()

arqueiro.atacar()
arqueiro.equipar_arco()
