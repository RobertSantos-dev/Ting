import sys


def txt_importer(path_file: str):
    try:
        if (path_file[-4:] != '.txt'):
            raise FileExistsError

        with open(path_file) as file:
            file_txt = file.read().split('\n')
            return file_txt

    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    except FileExistsError:
        sys.stderr.write('Formato inválido')
