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

Clone o repositório e execute os seguintes passos:

```bash
# Instalar as dependências
poetry install

# Configurar o caminho da imagem e do modelo YOLO no arquivo main.py

# Rodar o programa
poetry run python main.py

# Executar os testes
poetry run pytest

