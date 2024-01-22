def setup():
    size(980, 590)
    #n = random(10)
    #print(n)
    fill(0)
    no_stroke()
    
    # primeira fileira
    for x in range(50, 930, 60):
        d = random(50)
        #ellipse(x, 50, d, d)
        circle(x, 50, d)
    
    # segunda fileira
    for x in range(50, 930, 55):
        i = random_int(1, 4)
        circle(x, 150, 10 + i * 9)
        
    # terceira com cores
    for x in range(50, 930, 40):
        
        d = random(25, 50)
        
        r = random_int(255)
        g = random_int(255)
        b = random_int(255)
        fill(r, g, b)
        circle(x, 250, d)
        
    # cores mais restritas
    for x in range(50, 930, 50):
        
        d = random(20, 50)
        
        r = 0 # não quero vermelho
        g = random_int(255)
        b = random_int(255)
        fill(r, g, b)
        circle(x, 350, d)
    
    # quinta fileira
    for x in range(50, 930, 50):
        
        d = random(10, 45)
        
        r = 0
        g = random_int(128, 255)
        b = 128
        fill(r, g, b)
        circle(x, 450, d)
        
    cores = [
        color(255, 200, 0),
        color(0, 128, 255),
        color(128, 255, 0),
        ]
    
    for x in range(50, 930, 50):
        fill(random_choice(cores))
        circle(x, 550, 35)
        
    save('imagens/07_funcao_random.png')