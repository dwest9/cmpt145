import MyQueue as Q
import Stack as S


def show_queue(aqueue):
    print(aqueue.data)


def rev(aqueue):
    # the reversed queue we will return
    rev_queue = Q.Queue()
    # a temporary queue to hold the original order of aqueue
    temp_queue = Q.Queue()
    # a stack to effectively reverse the queue
    temp_stack = S.Stack()

    while not aqueue.is_empty():
        value = aqueue.dequeue()
        temp_queue.enqueue(value)
        temp_stack.push(value)

    while not temp_stack.is_empty():
        aqueue.enqueue(temp_queue.dequeue())
        rev_queue.enqueue(temp_stack.pop())

    return rev_queue


values = [1, 2, 3, 4]
some_queue = Q.Queue()
for v in values:
    some_queue.enqueue(v)

print('Before:   ', end='')
show_queue(some_queue)
rev_queue = rev(some_queue)
print('After:    ', end='')
show_queue(some_queue)
print('Returned: ', end='')
show_queue(rev_queue)
