import yaml

def carregar_estrutura_projeto(caminho_arquivo: str) -> dict:
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)