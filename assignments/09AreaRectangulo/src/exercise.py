
def main():
    #escribe tu código abajo de esta línea
    import math
    
    def area_rect(base, profundidad):
        area = base * profundidad
        print('El área del rectángulo es:', area)
    

    base = float(input('Dame la base: '))
    altura = float(input('Dame la altura: '))

 
    area_rect(base, altura)

if __name__=='__main__':
    main()
