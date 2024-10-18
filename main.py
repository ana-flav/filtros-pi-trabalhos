from PIL import Image

from filtros import aplicar_mascara, filtro_gradiente

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

    img = Image.open("imagem/teste.jpg")
    img = img.convert("L")

    sobel_1, sobel_2 = filtro_gradiente(img)

    resultado = Image.fromarray(sobel_1)
    resultado.save("imagem/resultado-sobel-1.png")
    resultado = Image.fromarray(sobel_2)
    resultado.save("imagem/resultado-sobel-2.png")

    for nome, (mascara, razao) in mascaras.items():
        resultado = aplicar_mascara(img, mascara, razao)
        salvar_imagem(resultado, f"imagem/resultado_{nome}.png")

if __name__ == "__main__":
    main()
