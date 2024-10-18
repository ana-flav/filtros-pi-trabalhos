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

    laplaciano_mascara_1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    laplaciano_mascara_2 = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
    laplaciano_mascara_3 = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    laplaciano_mascara_4 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    # img.save("imagem/teste.jpg")
    resultado = aplicar_mascara(img, gaussiano_mascara, gaussiano_razao)
    resultado_media = aplicar_mascara(img, media_mascara, media_razao)
    sobel_1, sobel_2 = filtro_gradiente(img)

    print('oi')
    resultado_laplaciano_1 = aplicar_mascara(img, laplaciano_mascara_1)
    print('oi')
    resultado_laplaciano_2 = aplicar_mascara(img, laplaciano_mascara_2)
    print('oi')
    resultado_laplaciano_3 = aplicar_mascara(img, laplaciano_mascara_3)
    print('oi')
    resultado_laplaciano_4 = aplicar_mascara(img, laplaciano_mascara_4)
    print('oi')

    # resultado = Image.fromarray(sobel_1)
    # resultado.save("imagem/resultado-sobel-1.png")
    # resultado = Image.fromarray(sobel_2)
    # resultado.save("imagem/resultado-sobel-2.png")

    print('oi')
    resultado = Image.fromarray(resultado_laplaciano_1)
    resultado.save("imagem/resultado-lapla-1.png")
    print('oi')
    resultado = Image.fromarray(resultado_laplaciano_2)
    resultado.save("imagem/resultado-lapla-2.png")
    print('oi')
    resultado = Image.fromarray(resultado_laplaciano_3)
    resultado.save("imagem/resultado-lapla-3.png")
    print('oi')
    resultado = Image.fromarray(resultado_laplaciano_4)
    resultado.save("imagem/resultado-lapla-4.png")
    print('oi')


if __name__ == "__main__":
    main()
