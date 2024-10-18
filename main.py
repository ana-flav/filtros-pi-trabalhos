from PIL import Image
import numpy as np
from filtros import aplicar_mascara

def salvar_imagem(resultado, nome_arquivo):
    imagem = Image.fromarray(resultado)
    imagem.save(nome_arquivo)

def main():
    mascaras = {
        "gaussiano": ([[1, 2, 1], [2, 4, 2], [1, 2, 1]], 1 / 16),
        "media": ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1 / 9),
        "laplaciano_1": ([[0, 1, 0], [1, -4, 1], [0, 1, 0]], 1),
        "laplaciano_2": ([[1, 1, 1], [1, -8, 1], [1, 1, 1]], 1),
        "laplaciano_3": ([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], 1),
        "laplaciano_4": ([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], 1)
    }

    img = Image.open("imagem/imagem.png").convert("L")
    img_array = np.array(img)

    for nome, (mascara, razao) in mascaras.items():
        resultado = aplicar_mascara(img_array, mascara, razao)
        salvar_imagem(resultado, f"imagem/resultado_{nome}.png")

if __name__ == "__main__":
    main()
