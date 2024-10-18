from PIL import Image

from filtros import aplicar_mascara


def main():
    # Mascara gaussiana
    gaussiano_mascara = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    gaussiano_razao = 1 / 16

    media_mascara = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    media_razao = 1 / 9  


    img = Image.open("imagem/imagem.png")
    img = img.convert("L")

    resultado = aplicar_mascara(img, gaussiano_mascara, gaussiano_razao)
    resultado_media = aplicar_mascara(img, media_mascara, media_razao)

    resultado = Image.fromarray(resultado)
    resultado.save("imagem/resultado.png")


if __name__ == "__main__":
    main()
