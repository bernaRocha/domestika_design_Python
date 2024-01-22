def setup():
    size(980, 390)
    fill(0)
    no_stroke()
    rect_mode(CENTER)
    
    for x in range(50, 930, 100):
        v = random_int(2, 5)
        if v == 1:
            circle(x, 250, 50)
        elif v == 2:
            square(x, 250, 50)
        else:
            r = random_choice((10, 25, 40))
            star(x, 250, r, 30, v)
    save('imagens/071_estrelas_aleatorias.png')
        
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