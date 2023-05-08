import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for value in instance.list_row:
        if (value['nome_do_arquivo'] == path_file):
            return
    list_row_file = txt_importer(path_file)
    new_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(list_row_file),
        'linhas_do_arquivo': list_row_file
    }
    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
