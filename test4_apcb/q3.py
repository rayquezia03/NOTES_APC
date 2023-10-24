import hashlib

def encriptar(texto):
    hash_obj = hashlib.sha256()
    hash_obj.update(texto.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()
    return hash_hex

path = 'q3.txt'
path2 = 'q3_cript.txt'

arquivo = open(path, 'r')
arquivo2 = open(path2, 'w')  # Alterado para abrir no modo de escrita ('w')

user_info = []

formated_text_by_user = arquivo.read().split("\n")
for a in formated_text_by_user:
    formated = a.split(',')
    if len(formated) >= 5:
        encripted_senha = encriptar(formated[4])  # Encriptar a senha correta
        user_info.append({'id': formated[0], 'nome': formated[1], 'celular': formated[2], 'email': formated[3], 'senha': encripted_senha})

        print({'id': formated[0], 'nome': formated[1], 'celular': formated[2], 'email': formated[3], 'senha': encripted_senha})

        n = str({'id': formated[0], 'nome': formated[1], 'celular': formated[2], 'email': formated[3], 'senha': encripted_senha})
        arquivo2.write(n + '\n')  

arquivo.close()
arquivo2.close()
