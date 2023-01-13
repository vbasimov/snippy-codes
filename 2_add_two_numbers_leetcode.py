class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.__class__.__name__}{{val: {self.val}, next: {self.next}}}"

class Solution:

    def add_two_numbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        return self.iterToNode(str(
            self.nodeToInt(l1) + self.nodeToInt(l2)
        ))

    def node_to_int(self, lstNd: ListNode) -> list:
        val = f"{lstNd.val}"
        while lstNd.next:
            val = f'{lstNd.next.val}{val}'
            lstNd = lstNd.next
        return int(val)

    def iter_to_node(self, lst: list) -> ListNode:
        last = None
        for el in lst:
            last = ListNode(el, last)
        return last

if __name__ == '__main__':
    s = Solution()
    l1 = s.iterToNode([2,4,3][::-1])
    l2 = s.iterToNode([5,6,4][::-1])
    print(s.addTwoNumbers(l1, l2))
    