def setup():
    size(400, 600) # largura, altura
    background(90, 30, 30) # fundo em RGB
    rect_mode(CENTER) # ponto de inserção
    fill(120, 90, 90)   #preenchimento da figura
    stroke(100, 20, 60) # cor do traço da figura
    stroke_weight(4)    # peso do traço
    rect(width / 3, height / 2, 200, 50)
    no_stroke()    # para que não tnha traço
    fill(255)      # 255 branco 0 preto 128 cinza
    ellipse(100, 150, 70, 30)