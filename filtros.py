import numpy as np

def verificar_mascara_laplaciana(mascara):
   
    laplaciano_4_vizinhos_neg = np.array([[ 0,  1,  0],
                                          [ 1, -4,  1],
                                          [ 0,  1,  0]])

    laplaciano_8_vizinhos_neg = np.array([[ 1,  1,  1],
                                          [ 1, -8,  1],
                                          [ 1,  1,  1]])

    laplaciano_4_vizinhos_pos = np.array([[ 0,  1,  0],
                                          [ 1,  4,  1],
                                          [ 0,  1,  0]])

    laplaciano_8_vizinhos_pos = np.array([[ 1,  1,  1],
                                          [ 1,  8,  1],
                                          [ 1,  1,  1]])

    return (np.array_equal(mascara, laplaciano_4_vizinhos_neg) or 
            np.array_equal(mascara, laplaciano_8_vizinhos_neg) or 
            np.array_equal(mascara, laplaciano_4_vizinhos_pos) or 
            np.array_equal(mascara, laplaciano_8_vizinhos_pos))

def aplicar_mascara(imagem, mascara_matriz: list[list[int]], mascara_razao: int = 1) -> np.matrix:
    imagem = np.array(imagem)
    linhas, colunas = imagem.shape
    imagem = [[int(imagem[i][j]) for j in range(colunas)] for i in range(linhas)]
    nova_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            # Tratamento das bordas:
            if i == 0 or i == len(imagem) - 1:
                continue

            if j == 0 or j == len(imagem[0]) - 1:
                continue

            novo_valor = (
                mascara_matriz[1][1] * imagem[i][j]
                + mascara_matriz[0][0] * imagem[i - 1][j - 1]
                + mascara_matriz[0][1] * imagem[i - 1][j]
                + mascara_matriz[0][2] * imagem[i - 1][j + 1]
                + mascara_matriz[1][0] * imagem[i][j - 1]
                + mascara_matriz[1][2] * imagem[i][j + 1]
                + mascara_matriz[2][0] * imagem[i + 1][j - 1]
                + mascara_matriz[2][1] * imagem[i + 1][j]
                + mascara_matriz[2][2] * imagem[i + 1][j + 1]
            )
            novo_valor = max(0, round(novo_valor * mascara_razao))
            nova_matriz[i][j] = novo_valor

        if verificar_mascara_laplaciana(np.array(mascara_matriz)):
            imagem_original = np.array(imagem, dtype=np.int16) 
            nova_matriz = imagem_original - nova_matriz

            for i in range(linhas):
                for j in range(colunas):
                    if nova_matriz[i, j] < 0:
                        nova_matriz[i, j] = 0  
                    elif nova_matriz[i, j] > 255:
                        nova_matriz[i, j] = 255  

    return np.matrix(nova_matriz).astype(np.uint8)
