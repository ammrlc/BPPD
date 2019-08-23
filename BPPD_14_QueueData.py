import queue

MyQueue = queue.Queue(3)

print(MyQueue.empty())
input("Press any key when ready...")

MyQueue.put(1)
MyQueue.put(2)
print(MyQueue.full())
input("Press any key when ready...")

MyQueue.put(3)
print(MyQueue.full())
input("Press any key when ready...")

print(MyQueue.get())
print(MyQueue.empty())
print(MyQueue.full())
input("Press any key when ready...")

print(MyQueue.get())
print(MyQueue.get())
