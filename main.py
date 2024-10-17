from PIL import Image

from filtros import aplicar_mascara


def main():
    # Mascara gaussiana
    gaussiano_mascara = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    gaussiano_razao = 1 / 16

    img = Image.open("imagem/imagem.png")
    img = img.convert("L")

    resultado = aplicar_mascara(img, gaussiano_mascara, gaussiano_razao)

    resultado = Image.fromarray(resultado)
    resultado.save("imagem/resultado.png")


if __name__ == "__main__":
    main()
