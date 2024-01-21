def setup():
    size(980, 980)
    background(30, 50, 120)
    #pts = [(200, 200), (500, 100),
           #(400, 400), (300, 200),
          #(100, 500)]
    star4(90, 90, 200, 100)
    star4(500, 400, 150, 50)
    star4(300, 600, 70, 25)
    
def star4(xc, yc, wa, wb):
    pts = [(-wa, -wa), (0, -wb), (wa, -wa),
           (wb, 0), (wa, wa), (0, wb),
           (-wa, wa), (-wb, 0)]
    
    begin_shape()
    for x, y in pts:
        vertex(xc + x, yc + y)
    
    end_shape(CLOSE)
    
    save('imagens/06_estrela.png')