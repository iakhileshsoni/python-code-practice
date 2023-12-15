"""  The difference between Array and Linked List  """

"""

Linked list:
------------
    A linked list is a data structure which contains a sequence of the elements where
    each element is linked to its next element. 
    There are two fields in an element of linked list. One is Data field, and other is link field.

Array vs Linked List:
---------------------
    The major difference between Array and Linked list regards to their structure.
    Arrays are Index based data structure where each element associated with an index.
    On the other hand, Linked list relies on references where each node consists of the data
    and the references to the previous and next element.

"""


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# Create a linked list from the given values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Display the linked list
def display_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Usage
obj = Solution()
head = create_linked_list([10, 60, 30, 40, 50])
result = obj.reverseList(head)
display_linked_list(result)
