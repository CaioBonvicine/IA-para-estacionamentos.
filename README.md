# Detector de Vagas de Estacionamento

Este projeto é um sistema de **detecção de vagas de estacionamento** utilizando o modelo YOLO da biblioteca `ultralytics`. Ele analisa imagens e retorna o total de vagas detectadas, assim como a quantidade de vagas livres e ocupadas.

---

## Funcionalidades

- Detecta vagas livres e ocupadas em imagens de estacionamento.
- Calcula a porcentagem de vagas livres e ocupadas.
- Pode ser facilmente testado com **Pytest** utilizando mocks para o modelo YOLO.

---

## Tecnologias Utilizadas

- Python 3.11+
- [Ultralytics YOLO] para detecção de objetos
- [Pytest] para testes unitários
- [Poetry] para gerenciamento de dependências

---

## Etapas para Rodar

1. Clone o repositório e rode:

    -poetry install
    -Configure o caminho da imagem e do modelo YOLO no main.py.
    -poetry run python main.py
    -poetry run pytest (para testes).


    Exemplo de saída:

    Resultado da análise:
    Total de vagas detectadas: 5
    Vagas livres: 3 (60.0%)
    Vagas ocupadas: 2 (40.0%)

