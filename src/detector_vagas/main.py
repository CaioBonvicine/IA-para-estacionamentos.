import cv2
from ultralytics import YOLO
from pathlib import Path

def main():
    # 1. Carrega o modelo treinado
    model = YOLO(
        'C:/detector_vagas/runs/detect/treinamento_vagas/weights/best.pt' # Substitua pelo caminho do seu modelo
    )

    # 2. Faz a detecção em uma imagem
    results = model.predict(
        'SuaImagem.jpg',  # Substitua pelo caminho da sua imagem
        save=True, conf=0.1
    )

    # 3. Processa os resultados
    for result in results:
        vagas_livres = sum(c == 1 for c in result.boxes.cls)
        vagas_ocupadas = sum(c == 0 for c in result.boxes.cls)
        total_vagas = vagas_livres + vagas_ocupadas

        if total_vagas > 0:
            perc_livres = (vagas_livres / total_vagas) * 100
            perc_ocupadas = (vagas_ocupadas / total_vagas) * 100
        else:
            perc_livres = perc_ocupadas = 0.0

        print("\nResultado da análise:")
        print(f"Total de vagas detectadas: {total_vagas}")
        print(f"Vagas livres: {vagas_livres} ({perc_livres:.1f}%)")
        print(f"Vagas ocupadas: {vagas_ocupadas} ({perc_ocupadas:.1f}%)")

if __name__ == "__main__":
    main()
