
def main():
    #escribe tu código abajo de esta línea
    import math
    
    def area_rect(base, profundidad):
        area = base * profundidad
        return area
    
    def volumen_prisma(area, altura):
        volumen = (area)*(altura)
        print('El volumen del prisma es: ', volumen)

    base = float(input('Dame la base: '))
    altura = float(input('Dame la altura: '))
    profundidad = float(input('Dame la profundidad: '))
 
    area = area_rect(base, profundidad)
    volumen_prisma(area, altura)
                   
                       

if __name__=='__main__':
    main()
