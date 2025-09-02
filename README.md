Esse código foi feito usando uma inteligencia artificial para detectar vagas livres e ocupadas em um estacionamento.

Códigos Poetry que foram usados:
poetry new detector_vagas
poetry add ultralystics opencv-python

Logo em seguida no arquivo "pyproject.toml" foi escrito no final do mesmo:
[tool.poetry.scripts]
detector_vagas = "detector_vagas.main:main"

Depois seguido pelos códigos:
poetry install
poetry run detector_vagas

Agora, novamente no terminal foi escrito "poetry build"

isso gerou os arquivos na pasta "dist" que podem ser baixados usando o comando "pip install NomeDoArquivo"
