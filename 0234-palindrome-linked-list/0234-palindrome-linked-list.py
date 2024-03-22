# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next

        i = len(arr)/2

        for j in range(i):
            if arr[j] != arr[len(arr) - 1 - j]:
                return False
        return True
        