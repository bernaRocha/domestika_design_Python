def setup():
    size(360, 360) #largura e altura do desenho
    background(30, 60, 120) #RGB
    rect_mode(CENTER) #usando o centro como referência
    # cor da forma
    fill(4, 78, 200)
    no_stroke()

    #rect(0, 0, 200, 40) #posição x, posição y, largura, altura
    rect(width / 2, height / 2, 30, 30)