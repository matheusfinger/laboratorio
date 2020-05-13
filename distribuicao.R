#recebendo arquivo em um vetor numérico
lengths = scan(file = "resultado.txt", what = numeric(), sep = "")

#analisando as frequências de cada tamanho com a função table
frequencias <- table(lengths)

#plotando as frequências para analisar a distribuição
plot(frequencias)

#analisando a porcentagem de íntrons que serão considerados pelo padrão do tophat
subset.introns <- subset(lengths, lengths >= 70 & lengths <=500000)
length(subset.introns)
