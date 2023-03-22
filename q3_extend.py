# or import from wherever you stored LList
from quiz3.LList import LList


# add following method definition to your LList class
def extend(self, another_llist):
    walker = self._head
    while walker.next != None:
        walker = walker.next
    walker.next = another_llist._head
    return None


a_llist = LList()
for i in [0, 1, 2, 3]:
    a_llist.add_to_back(i)

# show it
print(a_llist.to_string())

# create another LList object with other values
b_llist = LList()
for i in [4, 5, 6, 7, 8, 9]:
    b_llist.add_to_back(i)

# show it
print(b_llist.to_string())

# extend the first list by adding the values of the second
a_llist.extend(b_llist)

# show it
print(a_llist.to_string())
