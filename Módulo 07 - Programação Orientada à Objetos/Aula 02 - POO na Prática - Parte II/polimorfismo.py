"""
Polimorfismo nos permite tratar objetos de diferentes classes como se fossem da mesma 
classe base, desde que essas classes derivadas implementem métodos com a mesma assinatura 
(nome e parâmetros), porém com comportamentos diferentes.
"""

from guerreiro import Guerreiro
from mago import Mago
from combate import Combate

guerreiro = Guerreiro("Conan", 10, 100, 50)
mago = Mago("Gandalf", 10, 80, 80)

combate = Combate(guerreiro, mago)
combate.iniciar_combate()
