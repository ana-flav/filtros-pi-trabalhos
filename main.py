from PIL import Image

from filtros import aplicar_mascara, filtro_gradiente


def main():
    # Mascara gaussiana
    gaussiano_mascara = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    gaussiano_razao = 1 / 16

    media_mascara = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    media_razao = 1 / 9

    img = Image.open("imagem/teste.jpg")
    img = img.convert("L")

    # img.save("imagem/teste.jpg")
    resultado = aplicar_mascara(img, gaussiano_mascara, gaussiano_razao)
    resultado_media = aplicar_mascara(img, media_mascara, media_razao)
    sobel_1, sobel_2 = filtro_gradiente(img)

    resultado = Image.fromarray(sobel_1)
    resultado.save("imagem/resultado-sobel-1.png")
    resultado = Image.fromarray(sobel_2)
    resultado.save("imagem/resultado-sobel-2.png")


if __name__ == "__main__":
    main()
