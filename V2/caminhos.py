import os
import sys

def obter_pasta_base():
    """Descobre em qual pasta o programa está rodando."""
    if getattr(sys, 'frozen', False):
        # Está rodando como .exe (empacotado pelo PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # Está rodando como script .py normal
        return os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(obter_pasta_base(), "rpg.db")