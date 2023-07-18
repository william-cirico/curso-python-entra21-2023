"""
Adapter - Padrão Estrutural

Permite que objetos com interfaces incompatíveis trabalhem juntos. Ele atua como
uma espécie de "adaptador" entre duas classes ou componentes.
"""
from abc import ABC, abstractmethod

class IProcessadorPagamento(ABC):
    """Interface para processar pagamentos."""
    @abstractmethod
    def processar_pagamento(self, amount: float) -> None:
        """Processa o pagamento de um valor.

        Args:
            amount (float): Valor do pagamento.
        """

class BibliotecaPagamentoAntiga:
    """Biblioteca antiga para processar pagamentos."""
    def make_payment(self, amount: float) -> None:
        """Processa o pagamento de um valor.

        Args:
            amount (float): Valor do pagamento.
        """
        print(f"Pagamento de {amount} realizado com a biblioteca de pagamento antiga")

class BibliotecaPagamentoNova:
    """Biblioteca nova para processar pagamentos."""
    def pay(self, amount: float) -> None:
        """Processa o pagamento de um valor.

        Args:
            amount (float): Valor do pagamento.
        """
        print(f"Pagamento de {amount} realizado com a biblioteca de pagamento nova")

class AdaptadorBibliotecaPagamento(IProcessadorPagamento):
    """Adaptador para processar pagamentos."""
    def __init__(self, library) -> None:
        self.library = library

    def processar_pagamento(self, amount) -> None:
        if isinstance(self.library, BibliotecaPagamentoAntiga):
            self.library.make_payment(amount)
        elif isinstance(self.library, BibliotecaPagamentoNova):
            self.library.pay(amount)


def processar_pagamento(processador_pagamento: IProcessadorPagamento) -> None:
    """Utiliza um processador de pagamento para processar um pagamento de R$ 100.
    
    Args:
        processador_pagamento (IProcessadorPagamento): Processador do pagamento.
    """
    processador_pagamento.processar_pagamento(100)

if __name__ == "__main__":
    biblioteca_antiga = BibliotecaPagamentoAntiga()
    adapter = AdaptadorBibliotecaPagamento(biblioteca_antiga)
    processar_pagamento(adapter)

    biblioteca_nova = BibliotecaPagamentoNova()
    adapter = AdaptadorBibliotecaPagamento(biblioteca_nova)
    processar_pagamento(adapter)
