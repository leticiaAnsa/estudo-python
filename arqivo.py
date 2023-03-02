def arquivoExiste(nome):
    try:
        a = open(nome, 'irt')
        a.close()
    except FileNotFoundError:
        return False
    else: