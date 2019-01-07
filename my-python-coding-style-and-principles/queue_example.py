

from my_package.my_data_structure import my_queue


if __name__ == "__main__":
    queue = my_queue.Queue()

    queue.enqueue(10)
    queue.enqueue(3)
    queue.enqueue(14)

    print(f"size of the queue: {queue.size}")

    queue.dump()

    print()
    print(queue.dequeue())

    queue.dump()
    print()
    print(f"size of the queue: {queue.size}")