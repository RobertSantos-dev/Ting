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
    if (len(instance.list_row) == 0):
        sys.stdout.write('Não há elementos\n')
    else:
        re = instance.dequeue()
        sys.stdout.write(
            f'Arquivo {re["nome_do_arquivo"]} removido com sucesso\n'
        )


def file_metadata(instance, position):
    try:
        element_search = instance.search(position)
    except IndexError:
        sys.stderr.write('Posição inválida')
    else:
        sys.stdout.write(str(element_search))
