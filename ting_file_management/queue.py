from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.list_row = []

    def __len__(self):
        return len(self.list_row)

    def enqueue(self, value):
        self.list_row.append(value)

    def dequeue(self):
        if (len(self.list_row) == 0):
            return None
        return self.list_row.pop(0)

    def search(self, index):
        try:
            if (index < 0):
                raise IndexError
            return self.list_row[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
