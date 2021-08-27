
def main():
    #escribe tu código abajo de esta línea
    
    def num_tarjetas(papel, plumones):
        cant_papel = papel * 12
        cant_plumones = plumones * 35
        if cant_papel > cant_plumones:
            print('El número máximo de tarjetas que se pueden hacer es:', cant_plumones)
        elif cant_papel < cant_plumones:
            print('El número máximo de tarjetas que se pueden hacer es:', cant_papel)
        elif cant_papel == cant_plumones:
            print('El número máximo de tarjetas que se pueden hacer es:', cant_plumones)
            
    papel = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))

num_tarjetas(papel, plumones)

if __name__=='__main__':
    main()
