from queue import Queue
q= Queue()
q.put('a')
q.put('b')
q.put('c')
# print(list(q))
print(q.get())

if q.empty() is True:
    print('Q is empty')
else:
    print('q is not empty')
