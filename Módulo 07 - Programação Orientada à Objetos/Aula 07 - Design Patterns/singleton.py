"""
Singleton - Padrão Criacional

Tem como objetivo garantir que uma classe possua apenas uma instância e fornecer um 
ponto global de acesso a essa instância.
"""
class GerenciadorLogs:
    """Classe responsável pelo gerenciamento de logs"""
    _instance = None

    def __init__(self) -> None:
        self.arquivo_log = open("logs.txt", "a", encoding="utf-8")

    @staticmethod
    def get_instance():
        """Método para obter a instância do gerenciador de logs"""
        if not GerenciadorLogs._instance:
            GerenciadorLogs._instance = GerenciadorLogs()
        
        return GerenciadorLogs._instance
    
    def log(self, mensagem):
        """Mètodos utilizado para logar uma mensagem"""
        self.arquivo_log.write(f"{mensagem}\n")
        self.arquivo_log.flush()

if __name__ == "__main__":
    gerenciador_logs1 = GerenciadorLogs.get_instance()
    gerenciador_logs2 = GerenciadorLogs.get_instance()

    print(gerenciador_logs1 is gerenciador_logs2)

    gerenciador_logs1.log("Log do gerenciador 1")
    gerenciador_logs2.log("Log do gerenciador 2")
