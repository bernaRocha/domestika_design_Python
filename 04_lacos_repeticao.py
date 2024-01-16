"""
Sequências ordenadas
"""

def setup():
    size(900, 900)
    background(240)
    
    frutas = ["kiwi", "açaí", "banana"] # lista
    #numbers = [10, 20, 30, 40, 70]
    #p = (200, 100) # tupla
    
    for n in range(10, 120, 2):
        line(n * 10, 100, n * 3, 400)
    
    margin = 40
    for i in range(20):
        line(margin + i * 8, 150, i * 16, 600)
    