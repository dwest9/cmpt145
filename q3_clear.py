# or import from wherever you stored LList
from quiz3.LList import LList


# add following method definition to your LList class
def clear(self):
    self._size = 0
    self._head = None
    self._tail = None


values = [1, 2, 3, 4]
some_llist = LList()
for v in values:
    some_llist.add_to_back(v)

print("Before:", some_llist.to_string())
some_llist.clear()
print("After: ", some_llist.to_string())

