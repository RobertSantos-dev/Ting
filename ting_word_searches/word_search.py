def exists_word(word, instance):
    list_file = instance.list_row[0]
    list_result = [{
        'palavra': word,
        'arquivo': list_file['nome_do_arquivo'],
        'ocorrencias': [],
    }]
    for i in range(len(instance.list_row[0]['linhas_do_arquivo'])):
        if (word in list_file['linhas_do_arquivo'][i].lower()):
            list_result[0]['ocorrencias'].append({'linha': i + 1})
    if (not list_result[0]['ocorrencias']):
        return []
    return list_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
