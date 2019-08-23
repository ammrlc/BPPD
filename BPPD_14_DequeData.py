import collections

MyDeque = collections.deque("abcdef", 10)

print("Starting state:")
for Item in MyDeque:
   print(Item, end=" ")

print("\r\n\r\nAppending and extending right")
MyDeque.append("h")
MyDeque.extend("ij")
for Item in MyDeque:
   print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))

print("\r\nPopping right")
print("Popping {0}".format(MyDeque.pop()))
for Item in MyDeque:
   print(Item, end=" ")

print("\r\n\r\nAppending and extending left")
MyDeque.appendleft("a")
MyDeque.extendleft("bc")
for Item in MyDeque:
   print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))

print("\r\nPopping left")
print("Popping {0}".format(MyDeque.popleft()))
for Item in MyDeque:
   print(Item, end=" ")

print("\r\n\r\nRemoving")
MyDeque.remove("a")
for Item in MyDeque:
   print(Item, end=" ")
