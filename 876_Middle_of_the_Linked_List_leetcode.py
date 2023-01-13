class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.__class__.__name__}{{val: {self.val}, next: {self.next}}}"

class Solution:

    def iter_to_node(self, lst: list) -> ListNode:
        last = None
        for el in lst:
            last = ListNode(el, last)
        return last

    def node_to_iter(self, lst_nd: ListNode) -> list:
        val = [lst_nd.val]
        while lst_nd.next:
            val.insert(0, lst_nd.next.val)
            lst_nd = lst_nd.next
        return val

    def middle_node(self, head: ListNode | None) -> ListNode | None:
        head = self.nodeToIter(head)
        if len(head)%2:
            return self.iterToNode(head[:len(head)//2+1])
        else:
            return self.iterToNode(head[:len(head)//2])

s = Solution()
print(s.middle_node(s.iterToNode([1,2,3,4,5])))
