#quinto ejemplo
while True:
    try:
        altura=int(input('cual es tu altura : '))
        if altura >= 180:
            print('eres altito')
        
        elif altura<180:
            print('eres bajito')
            
        else:
            print('finalizando programa')
            break
    except ValueError:

        print('finalizando programa')
        break