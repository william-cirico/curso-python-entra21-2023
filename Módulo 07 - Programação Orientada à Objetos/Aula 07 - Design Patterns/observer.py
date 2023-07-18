"""
Observer - Padrão Comportamental

É um padrão de design comportamental que permite a comunicação entre objetos de forma
desacoplada. É útil quando há uma dependência entre objetos, mas você deseja evitar 
o acoplamento direto entre eles. 
"""

from abc import ABC, abstractmethod

class IObserver(ABC):
    """Interface de um Observer."""
    @abstractmethod
    def atualizar(self, temperatura: float):
        """Atualiza o observer"""

class DisplayFahrenheit(IObserver):
    """Observer concreto."""
    def atualizar(self, temperatura: float):
        temperatura_fahrenheit = (temperatura * (9 / 5)) + 32
        print(f"A temperatura atual em ºF é: {temperatura_fahrenheit:.2f}")

class DisplayCelsius(IObserver):
    """Observer concreto."""
    def atualizar(self, temperatura: float):
        print(f"A temperatura atual em ºC é: {temperatura:.2f}")

class EstacaoPrevisaoTempo:
    """Subject ou Observable."""
    def __init__(self) -> None:
        self.observers = []
        self.temperature = None

    def registrar_observer(self, observer: IObserver) -> None:
        """Registra um observer.
        
        Args:
            observer (IObserver): O observer.
        """
        self.observers.append(observer)

    def desregistrar_observer(self, observer: IObserver) -> None:
        """Cancela o registro de um observer.
        
        Args:
            observer (IObserver): O Observer.
        """
        self.observers.remove(observer)

    def noticar_observers(self) -> None:
        """Notifica todos os observers da classe."""
        for observer in self.observers:
            observer.update(self.temperature)
    
    def mudar_temperatura(self, temperatura: float):
        """Modifica a temperatura e notifica os observers.
        
        Args:
            temperatura (float): Nova temperatura em ºC."""
        self.temperature = temperatura
        self.noticar_observers()

if __name__ == "__main__":
    display_fahrenheit = DisplayFahrenheit()
    display_celsius = DisplayCelsius()

    estacao_previsao_tempo = EstacaoPrevisaoTempo()
    estacao_previsao_tempo.registrar_observer(display_fahrenheit)
    estacao_previsao_tempo.registrar_observer(display_celsius)

    estacao_previsao_tempo.mudar_temperatura(25)

    estacao_previsao_tempo.desregistrar_observer(display_celsius)

    estacao_previsao_tempo.mudar_temperatura(30)
