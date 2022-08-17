# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import starmap, zip_longest


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head = current = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            current.next = list1 or list2
            return head.next

        if not lists:
            return

        while len(lists) > 1:
            lists = list(starmap(mergeTwoLists, zip_longest(lists[::2], lists[1::2])))

        return lists[0]

    # from problem 21
