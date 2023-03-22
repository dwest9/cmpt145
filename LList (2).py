# doe869
# 11298443
# cmpt 145 CRN: 41442
# lab Section L05
# Shane Giroux


# CMPT 145 Course material
# Copyright (c) 2017-2021 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#     Defines the List ADT
#

#     Defines the List ADT
#



class node(object):
    """ A version of the node class with *public* attributes.
        This makes the use of node objects a bit more convenient for
        implementing LList class.

        IMPORTANT: Since there are no setters and getters, we use the attributes directly.

        This is safe because the node class is defined in this module.
        No one else will use this version of the class.
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data: Any data value to be stored in the node
            next: Another node (or None, by default)
        """
        self.data = data
        self.next = next

    # Note: use the attributes directly; no setters or getters!


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty LList object
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None

    def is_empty(self):
        """
        Purpose
            Checks if the given LList object has no data in it
        Return:
            :return True if the LList object has no data, or False otherwise
        """
        return self._size == 0  # returns True if size if 0

    def size(self):
        """
        Purpose
            Returns the number of data values in the given LList object
        Return:
            :return The number of data values in the LList object
        """
        return self._size  # returns size

    def add_to_front(self, value):
        """
        Purpose
            Insert value at the front of the LList object
        Preconditions:
            :param value:   a value of any kind
        Post-conditions:
            The LList object increases in size.
            The new value is at index 0.
            The values previously in the LList object appear after the new value.
        Return:
            :return None
        """
        if self.is_empty():  # if linked list is empty
            self._head = node(value, self._head)  # add new node to head
            self._tail = self._head  # head and tail are same

        else:  # if linked  list is not empty
            self._head = node(value, self._head)  # add new node to head

        self._size += 1  # increase size by 1

    def add_to_back(self, value):
        """
        Purpose
            Insert value at the end of the LList object
        Preconditions:
            :param value:   a value of any kind
        Post-conditions:
            The LList object increases in size.
            The new value is last in the LList object.
        Return:
            :return None
        """
        if self.is_empty():  # if linked list is empty
            self._head = node(value, self._head)  # add node to head
            self._tail = self._head  # head and tail are same
            self._size += 1  # increase siz of linked list by 1
        else:  # if linked list is not empty
            current = self._tail  # get the present tail node
            self._tail = node(value)  # point tail to new node
            current.next = self._tail  # set the next value to the new tail node
            self._size += 1  # increase size of linked list by 1

    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value
        Post-conditions:
            The LList object decreases in size.
            The returned value is no longer in in the LList object.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if not self.is_empty():  # if linked list is not empty
            current = self._head  # get head node
            self._head = current.next  # set new head node
            self._size -= 1  # decrease size by 1
            return (True, current.data)
        else:

            return (False, None)

    def get_index_of_value(self, value):
        """
        Purpose
            Return the smallest index of the given value.
        Preconditions:
            :param value:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, index if the value appears in self
            :return False, None if the value does not appear in self
        """
        i = 0  # index counter
        currentNode = self._head  # get head node
        while (currentNode):  # while node is not None
            if currentNode.data == value:  # if node data is equal to value
                return (True, i)
            currentNode = currentNode.next  # go to next node
            i += 1  # increase index by 1

        return (False, None)

    def value_is_in(self, value):
        """
        Purpose
            Check if the given value is in the LList object
        Preconditions:
            :param value:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True if the value is in the LList object, False otherwise
            :return (False if the LList object is empty)
        """
        currentNode = self._head  # get head node
        while (currentNode):  # while node is not None
            if currentNode.data == value:  # if node data is equal to value
                return True
            currentNode = currentNode.next  # go to next node

        return False

    def retrieve_data_at_index(self, index):
        """
        Purpose
            Return the value stored at the index
        Preconditions:
            :param index:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, value) if value is stored at index and index is valid
            :return (False, None) if the index is not valid for the LList object
        """
        i = 0
        currentNode = self._head
        if index >= 0 and index <= self._size:
            while (currentNode):
                if i == index:        # if i is equal to index
                    return (True, currentNode.data)
                currentNode = currentNode.next
                i += 1  # this increases i by 1

        return (False, None)

    def set_data_at_index(self, index, value):
        """
        Purpose
            Store value at the index
        Preconditions:
            :param value:   a value of any kind
            :param index:   a non-negative integer
        Post-conditions:
            The value stored at index changes to value
        Return:
            :return True if the index was valid, False otherwise
        """
        i = 0
        currentNode = self._head
        if index >= 0 and index <= self._size:  # if index is within valid range
            while (currentNode):
                if i == index:  # if i is equal to index
                    currentNode.data = value  # modify node data
                    return True
                currentNode = currentNode.next
                i += 1

        return False

    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The LList object decreases in size.
            The returned value is no longer in in the LList object.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        if not self.is_empty():  # if linked list is not empty
            if self._size == 1:  # if only one node is present
                last = self._tail  # get node
                self._head, self._tail = None, None  # remove node from linked list

            else:  # if linked list has more than one node
                i = 0
                secondLastIndex = self._size - 2  # get second last index
                first = self._head
                last = self._tail  # get tail node
                while (first):
                    if i == secondLastIndex:  # if i is equal to second last index
                        first.next = None  # set the next node to None
                        self._tail = first  # set new tail node
                        break  # break from loop
                    first = first.next
                    i += 1

            self._size -= 1  # decrease size by 1
            return (True, last.data)

        return (False, None)

    def insert_value_at_index(self, value, index):
        """
        Purpose
            Insert value at index
        Preconditions:
            :param value:   a value of any kind
            :param index:   a valid index for the LList object
        Post-conditions:
            The LList object increases in size.
            The new value is at index.
            The values previously in the LList object at index or later appear after the new value.
        Return:
            :return If the index is valid, insert_value_at_index returns True.
            :return If the index is not valid, insert_value_at_index returns False.
        """
        if index >= 0 and index <= self._size :  # if index in valid range
            if index == 0:  # if node is inserted at the beginning
                self.add_to_front(value)  # use add_to_front()
            else:  # if node is inserted somewhere in the middle
                i = 0
                currentNode = self._head
                self._size += 1  # increase size by 1
                while (currentNode):
                    if i == index - 1:  # if previous index reached
                        currentNode.next = node(value, currentNode.next)  # set the next node to new node
                        break  # breaks from loop
                    currentNode = currentNode.next
                    i += 1
            return True
        else:
            return False


    def delete_item_at_index(self, index):
        """
        Purpose
            Delete the value at index.
        Preconditions:
            :param index:   a non-negative integer
        Post-conditions:
            The LList object decreases in size if the index is valid
            The value at index is no longer in the LList object.
        Return:
            :return True if index was valid, False otherwise
        """
        if index >= 0 and index < self._size:  # if index in valid range
            if index == 0:  # if node is removed form the beginning
                self.remove_from_front()  # use remove_from_front()
            elif index == self._size - 1:  # if node is removed from the end
                self.remove_from_back()  # user remove_from_back()
            else:
                i = 0
                emp = self._head
                self._size -= 1  # decrease size of linked list by 1
                while (emp):
                    if i == index - 1:  # if previous index reached
                        a = emp.next  # get the next node
                        emp.next = emp.next.next  # set the next node to next then to next node
                        del a  # delete the node at given index
                        break  # exit loop

                    emp = emp.next
                    i += 1

            return True

        return False


