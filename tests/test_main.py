import pytest
from detector_vagas.main import main

def test_main_calcula_vagas(mocker, capsys):
    # substitui o modelo YOLO por um mock
    fake_model = mocker.Mock()

    # Simula resultados de detecção
    class FakeBoxes:
        def __init__(self, cls):
            self.cls = cls

    fake_results = [
        mocker.Mock(boxes=FakeBoxes(cls=[1, 0, 1, 0, 1]))
    ]

    fake_model.predict.return_value = fake_results

    mocker.patch("detector_vagas.main.YOLO", return_value=fake_model)

    main()

    captured = capsys.readouterr()
    assert "Total de vagas detectadas: 5" in captured.out
    assert "Vagas livres: 3 (60.0%)" in captured.out
    assert "Vagas ocupadas: 2 (40.0%)" in captured.out


def test_main_sem_vagas(mocker, capsys):
    fake_model = mocker.Mock()

    # Simulação para nenhuma vaga detectada
    class FakeBoxes:
        def __init__(self, cls):
            self.cls = cls

    fake_results = [mocker.Mock(boxes=FakeBoxes(cls=[]))]

    fake_model.predict.return_value = fake_results

    mocker.patch("detector_vagas.main.YOLO", return_value=fake_model)

    main()

    captured = capsys.readouterr()
    assert "Total de vagas detectadas: 0" in captured.out
    assert "Vagas livres: 0 (0.0%)" in captured.out
    assert "Vagas ocupadas: 0 (0.0%)" in captured.out
