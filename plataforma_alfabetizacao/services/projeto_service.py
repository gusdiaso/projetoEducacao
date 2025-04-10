from models.projeto import Projeto, Etapa

def construir_projeto(dados: dict) -> Projeto:
    projeto_dict = dados["projeto"]

    etapas = [Etapa(nome=e["nome"], atividades=e["atividades"]) for e in projeto_dict["etapas_projeto"]]

    return Projeto(
        nome=projeto_dict["nome"],
        objetivo_geral=projeto_dict["objetivo_geral"],
        objetivos_especificos=projeto_dict["objetivos_especificos"],
        modulos=projeto_dict["modulos"],
        requisitos_tecnicos=projeto_dict["requisitos_tecnicos"],
        etapas_projeto=etapas,
        documentacoes_complementares=projeto_dict["documentacoes_complementares"]
    )