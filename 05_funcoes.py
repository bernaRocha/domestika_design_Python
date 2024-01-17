def setup():
    size(880, 660)
    background(0, 100, 220)
    #eye(200, 400, 50, 20)
    #eye(300, 100, 150, 49)
    #eye(600, 600, 200, 150)
    #eye(100, 300, 250, 255)
    #eye(800, 190, 300, 0)
    for y in range(90, 600, 70):
        eye(width / 2, y, 160, 20)
    save('imagens/resultado.png')
    
    
    
def eye(x, y, w, cor):
    no_stroke()
    fill(200)
    ellipse(x, y, w, w / 3)
    fill(155, 0, 0)
    ellipse(x, y, w / 4, w / 4)
    fill(cor)
    ellipse(x, y, w * 0.1, w * 0.1)