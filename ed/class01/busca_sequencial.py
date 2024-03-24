def quebrar_senha():
    senha_correta = input("Digite a senha de 4 dígitos numéricos: ")

    for i in range(10000):

        senha_tentativa = '{:04}'.format(i)
        senha_tentativa_2 = i
        print('====')
        print(senha_tentativa,'===',senha_tentativa_2)
        
        # Verifica se a senha tentativa é igual à senha correta
        if senha_tentativa == senha_correta:
            print(f"A senha foi quebrada! A senha é: {senha_tentativa}")
            return
    
    print("Não foi possível quebrar a senha.")


quebrar_senha()
