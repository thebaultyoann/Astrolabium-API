queue = []
queue_numbers = 0
def handle_connexions():
    numero_queue = get_in_queue()
    print(numero_queue)
    while not check_queue(numero_queue):
        numero_queue=numero_queue
        drop_from_queue()
    return "sucess"


def get_in_queue():
    global queue_numbers
    queue_numbers=(queue_numbers+1)%10000
    queue.append(queue_numbers)
    return queue_numbers

def check_queue(numero_queue):
    return queue[0]==numero_queue

def drop_from_queue():
    queue.pop(0)

def test():
    drop_from_queue()
    return 

handle_connexions()


