from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._list_row = []

    def __len__(self):
        return len(self._list_row)

    def enqueue(self, value):
        self._list_row.append(value)

    def dequeue(self):
        if (len(self._list_row) == 0):
            return None
        return self._list_row.pop(0)

    def search(self, index):
        try:
            if (index < 0):
                raise IndexError
            return self._list_row[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
