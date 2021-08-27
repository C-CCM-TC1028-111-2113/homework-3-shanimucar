
def main():
    #escribe tu código abajo de esta línea
    def is_bisiesto(year):
        if year%4 == 0 and year%100 != 0:
            return True
        else:
            return False
 
    year = int(input(''))
 
    is_bisiesto(year)
 
    print(is_bisiesto(year))

if __name__=='__main__':
    main()
