def setup():
    size(980, 980)
    background(40, 30, 160)
    
    star(700, 700, 200, 100, 12)
    star(350, 350, 150, 50, 9)
    star(200, 150, 30, 30, 4)
    star(600, 350, 70, 20, 10)
    
    save('imagens/061_estrelas.png')

def star(cx, cy, ra, rb, np, start_ang=0):
    step = TWO_PI / np # passo
    begin_shape()
    for i in range(np):
        ang = start_ang + step * i + frame_count / 50.0
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)