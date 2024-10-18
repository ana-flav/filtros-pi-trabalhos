from PIL import Image

from filtros import aplicar_mascara


def main():
    # Mascara gaussiana
    gaussiano_mascara = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    gaussiano_razao = 1 / 16

    media_mascara = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    media_razao = 1 / 9  


    laplaciano_mascara_1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    laplaciano_mascara_2 = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
    laplaciano_mascara_3 = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    laplaciano_mascara_4 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]


    
    img = Image.open("imagem/imagem.png")
    img = img.convert("L")

    resultado = aplicar_mascara(img, gaussiano_mascara, gaussiano_razao)
    resultado_media = aplicar_mascara(img, media_mascara, media_razao)
    resultado_laplaciano_1 = aplicar_mascara(img, laplaciano_mascara_1)
    resultado_laplaciano_2 = aplicar_mascara(img, laplaciano_mascara_2)
    resultado_laplaciano_3 = aplicar_mascara(img, laplaciano_mascara_3)
    resultado_laplaciano_4 = aplicar_mascara(img, laplaciano_mascara_4)

    

    resultado = Image.fromarray(resultado)
    resultado.save("imagem/resultado.png")


if __name__ == "__main__":
    main()
