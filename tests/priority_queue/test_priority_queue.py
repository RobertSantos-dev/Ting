import pytest

from ting_file_management.file_process import process
from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.queue import Queue


def test_basic_priority_queueing():
    queue = Queue()
    priority_queue = PriorityQueue()
    process("statics/novo_paradigma_globalizado-min.txt", queue)
    process("statics/nome_pedro.txt", queue)
    process("statics/arquivo_teste.txt", queue)
    priority_queue.enqueue(queue.list_row[0])
    priority_queue.enqueue(queue.list_row[1])
    priority_queue.enqueue(queue.list_row[2])
    priority_queue.dequeue()

    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue) == 2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(10)

    assert priority_queue.search(0)['qtd_linhas'] == 3
