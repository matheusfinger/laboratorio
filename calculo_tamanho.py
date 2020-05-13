#recebendo o arquivo bed com as posições dos íntrons
arquivo = open("introns.bed")
introns = arquivo.readlines()
arquivo.close()
#criando um arquivo para receber o resultado
resultado = open("resultado.txt","w")
#percorrendo o arquivo bed
for linha in introns:
    #separando os elementos da linha
    elementos = linha.split("\t")
    #diminuindo a posição final pela inicial (chequei e dá certinho o tamanho do íntron)
    tamanho = int(elementos[2]) - int(elementos[1])
    #adicionando o tamanho do íntron no arquivo criado
    resultado.write("%d\n" % tamanho)
resultado.close()
