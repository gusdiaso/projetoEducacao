from utils.yaml_loader import carregar_estrutura_projeto
from services.projeto_service import construir_projeto

if __name__ == "__main__":
    caminho_arquivo = "estrutura_projeto_alfabetizacao.yaml"
    dados_yaml = carregar_estrutura_projeto(caminho_arquivo)
    projeto = construir_projeto(dados_yaml)

    print(f"Nome do Projeto: {projeto.nome}")
    print(f"Objetivo Geral: {projeto.objetivo_geral}")
    print("Módulos disponíveis:")
    for modulo, funcionalidades in projeto.modulos.items():
        print(f"- {modulo}: {len(funcionalidades)} funcionalidades")