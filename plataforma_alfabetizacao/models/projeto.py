from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Etapa:
    nome: str
    atividades: List[str]

@dataclass
class Projeto:
    nome: str
    objetivo_geral: str
    objetivos_especificos: List[str]
    modulos: Dict[str, List[str]]
    requisitos_tecnicos: Dict[str, List[str]]
    etapas_projeto: List[Etapa]
    documentacoes_complementares: List[str]